#!/usr/bin/env python3
"""
Side-by-side comparison of transformers vs MLX predictions.
Includes numerical analysis, tolerance checks, and top-k overlap.

Two sources for the HF-side reference:
  - Live forward pass (default): runs transformers locally. Requires the
    full custom-code stack to be installable + runnable on this machine.
  - Precomputed safetensors via --reference-from: skips transformers
    entirely on the HF side, loads tokens + logits from disk. Used when
    the HF reference can only run on CUDA (e.g. trust_remote_code models
    with fla / mamba_ssm / triton-only kernels).

Usage:
    python compare_predictions.py <model_path> [prompt]
    python compare_predictions.py <model_path> [prompt] --trust-remote-code
    python compare_predictions.py <model_path> --reference-from ref.safetensors
"""

import argparse
import gc

import numpy as np
import mlx.core as mx
from transformers import AutoTokenizer
from mlx_lm import load


def load_hf_reference_from_file(path):
    """Load (input_ids, logits, metadata) from a precomputed safetensors.

    The file shape must match what compute_reference.py writes:
      - input_ids: int64 [seq_len]
      - logits:    float32 [seq_len, vocab]
    Logits are returned with a batch dim added so they match a live
    transformers forward pass shape [1, seq_len, vocab].
    """
    from safetensors import safe_open
    with safe_open(path, framework="numpy") as f:
        input_ids = f.get_tensor("input_ids").tolist()
        logits = f.get_tensor("logits")
        metadata = f.metadata() or {}
    return input_ids, logits[None, ...], metadata


def collect_hf_live(model_path, prompt, tokenizer, trust_remote_code):
    """Run a live transformers forward pass and return (tokens, logits)."""
    import torch
    from transformers import AutoModelForCausalLM

    print("Loading transformers model...")
    hf_model = AutoModelForCausalLM.from_pretrained(
        model_path,
        torch_dtype=torch.float32,
        trust_remote_code=trust_remote_code,
    )
    hf_tokens = tokenizer.encode(prompt)
    hf_inputs = torch.tensor([hf_tokens])
    with torch.no_grad():
        hf_outputs = hf_model(hf_inputs)
        hf_logits = hf_outputs.logits.numpy()
    del hf_model
    gc.collect()
    return hf_tokens, hf_logits


def compare_predictions(
    model_path: str,
    prompt: str = "The",
    trust_remote_code: bool = False,
    reference_from: str = None,
):
    print("=== TRANSFORMERS vs MLX COMPARISON ===")
    print(f"Model: {model_path}")
    print(f"Prompt: '{prompt}'")
    print(f"trust_remote_code: {trust_remote_code}")
    if reference_from:
        print(f"reference_from: {reference_from}")
    print()

    # Tokenizer is needed in both modes (for top-k pretty-printing and, in
    # the live mode, to encode the prompt). Cheap to load — even
    # trust_remote_code tokenizers typically resolve to PreTrainedTokenizerFast.
    hf_tokenizer = AutoTokenizer.from_pretrained(
        model_path, trust_remote_code=trust_remote_code
    )
    if hf_tokenizer.pad_token is None:
        hf_tokenizer.pad_token = hf_tokenizer.eos_token

    if reference_from:
        hf_tokens, hf_logits_np, metadata = load_hf_reference_from_file(
            reference_from
        )
        print(f"Loaded reference: {len(hf_tokens)} tokens, "
              f"logits shape {hf_logits_np.shape}")
        if metadata:
            print(f"Reference metadata: {metadata}")
        # Sanity: the reference's prompt must match what we're testing against.
        ref_prompt = metadata.get("prompt")
        if ref_prompt is not None and ref_prompt != prompt:
            print("WARNING: Reference prompt does not match the prompt passed "
                  "to this script. Comparison results will be meaningless.")
    else:
        hf_tokens, hf_logits_np = collect_hf_live(
            model_path, prompt, hf_tokenizer, trust_remote_code,
        )

    # Load MLX model
    print("Loading MLX model...")
    mlx_tokenizer_config = {"trust_remote_code": True} if trust_remote_code else None
    mlx_model, mlx_tokenizer = load(model_path, tokenizer_config=mlx_tokenizer_config)

    # Tokenize and forward pass - MLX
    mlx_tokens = mlx_tokenizer.encode(prompt)
    mlx_inputs = mx.array([mlx_tokens])
    mlx_logits = mlx_model(mlx_inputs)
    mx.eval(mlx_logits)

    mlx_logits_np = np.array(mlx_logits.astype(mx.float32))

    # Token comparison
    print(f"\nTokens (HF):  {hf_tokens}")
    print(f"Tokens (MLX): {mlx_tokens}")
    if hf_tokens != mlx_tokens:
        print("WARNING: Token mismatch!")

    # === NUMERICAL COMPARISON ===
    print(f"\n{'='*60}")
    print("NUMERICAL COMPARISON")
    print(f"{'='*60}")

    print(f"\nShape - HF: {hf_logits_np.shape}, MLX: {mlx_logits_np.shape}")

    # Basic statistics
    print(f"\nHF logits  - min: {hf_logits_np.min():.4f}, max: {hf_logits_np.max():.4f}, mean: {hf_logits_np.mean():.4f}, std: {hf_logits_np.std():.4f}")
    print(f"MLX logits - min: {mlx_logits_np.min():.4f}, max: {mlx_logits_np.max():.4f}, mean: {mlx_logits_np.mean():.4f}, std: {mlx_logits_np.std():.4f}")

    # Difference analysis
    diff = np.abs(hf_logits_np - mlx_logits_np)
    rel_diff = diff / (np.abs(hf_logits_np) + 1e-8)

    print(f"\nAbsolute diff - min: {diff.min():.6f}, max: {diff.max():.6f}, mean: {diff.mean():.6f}")
    print(f"Relative diff - min: {rel_diff.min():.6f}, max: {rel_diff.max():.6f}, mean: {rel_diff.mean():.6f}")

    # Tolerance checks
    tolerances = [1e-3, 1e-2, 1e-1, 1.0]
    print("\nTolerance checks (% of values within threshold):")
    for tol in tolerances:
        within = (diff < tol).mean() * 100
        print(f"  < {tol}: {within:.2f}%")

    # === TOP PREDICTIONS ===
    print(f"\n{'='*60}")
    print("TOP 10 PREDICTIONS (last token)")
    print(f"{'='*60}")

    hf_last = hf_logits_np[0, -1, :]
    mlx_last = mlx_logits_np[0, -1, :]

    # Stable softmax in numpy (avoids the torch dep when --reference-from
    # is set and we never imported torch).
    def softmax(x):
        e = np.exp(x - x.max())
        return e / e.sum()

    hf_probs = softmax(hf_last)
    mlx_probs = softmax(mlx_last)

    # Get sorted top-10 indices
    hf_top_idx = np.argsort(hf_probs)[-10:][::-1]
    mlx_top_idx = np.argsort(mlx_probs)[-10:][::-1]

    print(f"\n{'Rank':<6} {'HF Token':<10} {'HF Text':<20} {'HF Prob':<10} {'MLX Token':<10} {'MLX Text':<20} {'MLX Prob':<10}")
    print("-" * 96)

    for i in range(10):
        hf_idx = hf_top_idx[i]
        hf_prob = hf_probs[hf_idx]
        hf_text = repr(hf_tokenizer.decode([hf_idx]))

        mlx_idx = mlx_top_idx[i]
        mlx_prob = mlx_probs[mlx_idx]
        mlx_text = repr(mlx_tokenizer.decode([mlx_idx]))

        print(f"{i+1:<6} {hf_idx:<10} {hf_text:<20} {hf_prob:<10.6f} {mlx_idx:<10} {mlx_text:<20} {mlx_prob:<10.6f}")

    # === OVERLAP ANALYSIS ===
    print(f"\n{'='*60}")
    print("OVERLAP ANALYSIS")
    print(f"{'='*60}")

    # Top-1 match
    top1_match = hf_top_idx[0] == mlx_top_idx[0]
    print(f"\nTop-1 match: {top1_match}")
    print(f"  HF:  {hf_top_idx[0]} ({repr(hf_tokenizer.decode([hf_top_idx[0]]))})")
    print(f"  MLX: {mlx_top_idx[0]} ({repr(mlx_tokenizer.decode([mlx_top_idx[0]]))})")

    # Top-5 overlap
    hf_top5 = set(hf_top_idx[:5])
    mlx_top5 = set(mlx_top_idx[:5])
    top5_overlap = len(hf_top5 & mlx_top5)
    print(f"\nTop-5 overlap: {top5_overlap}/5")
    print(f"  HF:  {list(hf_top_idx[:5])}")
    print(f"  MLX: {list(mlx_top_idx[:5])}")

    # Top-10 overlap
    hf_top10 = set(hf_top_idx)
    mlx_top10 = set(mlx_top_idx)
    top10_overlap = len(hf_top10 & mlx_top10)
    print(f"\nTop-10 overlap: {top10_overlap}/10")

    # === SUMMARY ===
    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")

    if top1_match and top5_overlap >= 4:
        print("SUCCESS: Predictions match well")
    elif top1_match:
        print("PARTIAL: Top-1 matches but some divergence in top-5")
    else:
        print("FAILURE: Top-1 differs - investigate layer-by-layer")

    return {
        'top1_match': top1_match,
        'top5_overlap': top5_overlap,
        'top10_overlap': top10_overlap,
        'max_diff': diff.max(),
        'mean_diff': diff.mean(),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Side-by-side transformers vs MLX prediction comparison."
    )
    parser.add_argument("model_path")
    parser.add_argument("prompt", nargs="?", default="The")
    parser.add_argument(
        "--trust-remote-code",
        action="store_true",
        help="Pass trust_remote_code=True when loading the HF tokenizer and "
             "(in live mode) the HF model.",
    )
    parser.add_argument(
        "--reference-from",
        default=None,
        help="Path to a precomputed reference safetensors (produced by "
             "compute_reference.py). When set, the HF forward pass is "
             "skipped — tokens and logits are loaded from the file.",
    )
    args = parser.parse_args()

    results = compare_predictions(
        args.model_path,
        args.prompt,
        trust_remote_code=args.trust_remote_code,
        reference_from=args.reference_from,
    )
