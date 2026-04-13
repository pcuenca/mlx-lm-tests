#!/usr/bin/env python3
"""
Layer-by-layer comparison between transformers and MLX.

Single forward pass per framework:
  - Transformers: uses `output_hidden_states=True`.
  - MLX: temporarily wraps each entry in `model.model.layers` (and the
    embedding) to capture the output, then restores the originals.

Works on any mlx-lm model that follows the standard structure
(`model.model.layers` is a list, `model.model.embed_tokens` is the embedding).

Usage: python compare_layers.py <model_path> [prompt]
"""

import gc
import sys

import numpy as np


def _inner(model):
    """Return the inner submodule that holds `layers` and `embed_tokens`."""
    return model.model if hasattr(model, "model") else model


# ---------------------------------------------------------------------------
# Transformers
# ---------------------------------------------------------------------------

def collect_transformers_states(model_path, input_ids, dtype):
    """Return a list of numpy arrays, one per `hidden_states` entry.

    `outputs.hidden_states` has length `num_layers + 1`:
      - [0] is the input to the first decoder layer (post-embedding,
        post any pre-layer transforms applied by the model).
      - [i+1] is the output of layer i.
    """
    import torch
    from transformers import AutoModelForCausalLM

    torch_dtype = getattr(torch, dtype)
    print(f"Loading transformers model (dtype={dtype})...", flush=True)
    model = AutoModelForCausalLM.from_pretrained(
        model_path, torch_dtype=torch_dtype, device_map="cpu"
    )

    inputs = torch.tensor([input_ids], dtype=torch.long)
    with torch.no_grad():
        outputs = model(inputs, output_hidden_states=True)

    # Cast to float32 for comparison (avoids np.array() failures on bf16)
    states = [h[0].float().numpy() for h in outputs.hidden_states]

    del model, outputs
    gc.collect()
    return states


# ---------------------------------------------------------------------------
# MLX
# ---------------------------------------------------------------------------

class _Capture:
    """Callable wrapper that records the (first) output of `wrapped`.

    Not an `nn.Module` — we want it to be invisible to parameter tracking
    and just intercept the call. Since mlx-lm stores layers in a plain
    Python list, swapping in a non-Module callable works fine for inference.
    """
    def __init__(self, wrapped, sink):
        self.wrapped = wrapped
        self.sink = sink

    def __call__(self, *args, **kwargs):
        out = self.wrapped(*args, **kwargs)
        hidden = out[0] if isinstance(out, tuple) else out
        self.sink.append(hidden)
        return out


def collect_mlx_states(model_path, input_ids):
    """Return (states, dtype_str) — states is a list of numpy arrays."""
    import mlx.core as mx
    from mlx_lm import load

    print("Loading MLX model...", flush=True)
    model, _ = load(model_path)
    inner = _inner(model)

    if not hasattr(inner, "layers") or not hasattr(inner, "embed_tokens"):
        raise RuntimeError(
            "MLX model does not follow the expected mlx-lm structure "
            "(`model.model.layers` and `model.model.embed_tokens`)."
        )

    captured = []
    layers = inner.layers
    original_layers = list(layers)
    original_embed = inner.embed_tokens

    try:
        inner.embed_tokens = _Capture(original_embed, captured)
        for i in range(len(layers)):
            layers[i] = _Capture(original_layers[i], captured)

        inputs = mx.array([input_ids], dtype=mx.int32)
        out = model(inputs)
        mx.eval(out)
        for h in captured:
            mx.eval(h)
    finally:
        inner.embed_tokens = original_embed
        for i in range(len(layers)):
            layers[i] = original_layers[i]

    states = [np.array(h[0].astype(mx.float32)) for h in captured]
    # Sniff MLX runtime dtype from the model's forward output
    runtime_dtype = str(out.dtype).rsplit(".", 1)[-1]
    return states, runtime_dtype


# ---------------------------------------------------------------------------
# Comparison
# ---------------------------------------------------------------------------

def label(i, n_states):
    if i == 0:
        return "embed"
    return f"layer {i - 1}"


def compare(tf_states, mlx_states):
    n = min(len(tf_states), len(mlx_states))
    if len(tf_states) != len(mlx_states):
        print(f"\nWARNING: state count mismatch — TF={len(tf_states)}, "
              f"MLX={len(mlx_states)}. Comparing first {n}.")

    print()
    header = f"{'pos':<8} {'shape':<22} {'max diff':>11} {'mean diff':>11} {'TF mean':>11} {'MLX mean':>11}  status"
    print(header)
    print("-" * len(header))

    first_div = None
    for i in range(n):
        tf, mlx_ = tf_states[i], mlx_states[i]
        if tf.shape != mlx_.shape:
            print(f"{label(i, n):<8} SHAPE MISMATCH  TF={tf.shape}  MLX={mlx_.shape}")
            continue

        diff = np.abs(tf - mlx_)
        max_d, mean_d = diff.max(), diff.mean()

        if max_d < 1e-2:
            status = "ok"
        elif max_d < 1.0:
            status = "warn"
        else:
            status = "DIVERGED"
            if first_div is None:
                first_div = i

        print(f"{label(i, n):<8} {str(tf.shape):<22} "
              f"{max_d:>11.4e} {mean_d:>11.4e} "
              f"{tf.mean():>11.4f} {mlx_.mean():>11.4f}  {status}")

    print()
    if first_div is not None:
        print(f"First significant divergence at {label(first_div, n)}.")
    else:
        print("All compared states within tolerance.")


# ---------------------------------------------------------------------------

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("model_path")
    parser.add_argument("prompt", nargs="?", default="The")
    parser.add_argument("--tf-dtype", default=None,
                        help="dtype for the transformers model "
                             "(default: match MLX runtime dtype, typically bfloat16). "
                             "Use 'float32' for a higher-precision reference.")
    args = parser.parse_args()

    print(f"Model: {args.model_path}")
    print(f"Prompt: {args.prompt!r}")

    from transformers import AutoTokenizer
    tokenizer = AutoTokenizer.from_pretrained(args.model_path)
    input_ids = tokenizer.encode(args.prompt)
    print(f"Token count: {len(input_ids)}")

    # Run MLX first so we know its runtime dtype, then load TF with the same.
    mlx_states, mlx_dtype = collect_mlx_states(args.model_path, input_ids)
    tf_dtype = args.tf_dtype or mlx_dtype
    tf_states = collect_transformers_states(args.model_path, input_ids, tf_dtype)

    print(f"\nCollected {len(tf_states)} TF states, {len(mlx_states)} MLX states "
          f"(TF dtype={tf_dtype}, MLX dtype={mlx_dtype})")
    compare(tf_states, mlx_states)


if __name__ == "__main__":
    main()
