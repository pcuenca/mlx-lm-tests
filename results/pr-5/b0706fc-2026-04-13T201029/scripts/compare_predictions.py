#!/usr/bin/env python3
"""
Side-by-side comparison of transformers vs MLX predictions.
Includes numerical analysis, tolerance checks, and top-k overlap.

Usage: python compare_predictions.py <model_path> [prompt]
"""

import sys
import gc
import numpy as np
import torch
import mlx.core as mx
from transformers import AutoTokenizer, AutoModelForCausalLM
from mlx_lm import load


def compare_predictions(model_path: str, prompt: str = "The"):
    print("=== TRANSFORMERS vs MLX COMPARISON ===")
    print(f"Model: {model_path}")
    print(f"Prompt: '{prompt}'")
    print()

    # Load transformers model
    print("Loading transformers model...")
    hf_tokenizer = AutoTokenizer.from_pretrained(model_path)
    hf_model = AutoModelForCausalLM.from_pretrained(model_path, torch_dtype=torch.float32)
    if hf_tokenizer.pad_token is None:
        hf_tokenizer.pad_token = hf_tokenizer.eos_token

    # Tokenize and forward pass - transformers
    hf_tokens = hf_tokenizer.encode(prompt)
    hf_inputs = torch.tensor([hf_tokens])
    with torch.no_grad():
        hf_outputs = hf_model(hf_inputs)
        hf_logits = hf_outputs.logits

    hf_logits_np = hf_logits.numpy()

    # Cleanup transformers
    del hf_model
    gc.collect()

    # Load MLX model
    print("Loading MLX model...")
    mlx_model, mlx_tokenizer = load(model_path)

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

    hf_probs = torch.softmax(torch.tensor(hf_last), dim=-1).numpy()
    mlx_probs = np.exp(mlx_last - mlx_last.max())
    mlx_probs = mlx_probs / mlx_probs.sum()

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
    if len(sys.argv) < 2:
        print("Usage: python compare_predictions.py <model_path> [prompt]")
        sys.exit(1)

    model_path = sys.argv[1]
    prompt = sys.argv[2] if len(sys.argv) > 2 else "The"

    results = compare_predictions(model_path, prompt)
