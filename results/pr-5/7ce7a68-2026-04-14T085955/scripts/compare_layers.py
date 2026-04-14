#!/usr/bin/env python3
"""
Layer-by-layer comparison between transformers and MLX.

Single forward pass per framework:
  - Transformers: uses `output_hidden_states=True`.
  - MLX: temporarily wraps each entry in `model.model.layers` to capture
    the output, then restores the originals.

Compares per-layer outputs (post-layer-0 through post-layer-(N-1)) and the
post-final-norm state. Skips the embedding to avoid model-specific
pre-layer scaling that differs across architectures.

Works on any mlx-lm model where `model.[language_model.]model.layers` is
a list and `model.[language_model.]model.norm` is the final norm.

Usage:
    python compare_layers.py <model_path> [prompt]
    python compare_layers.py <model_path> [prompt] --t-dtype float32
"""

import gc
import sys

import numpy as np


# ---------------------------------------------------------------------------
# Find the inner module that holds layers + norm
# ---------------------------------------------------------------------------

def _inner(model):
    """Walk down nested submodule attrs to find the module with both
    `layers` and `norm`.
    """
    current = model
    visited = set()
    for _ in range(5):
        if id(current) in visited:
            break
        visited.add(id(current))
        if hasattr(current, "layers") and hasattr(current, "norm"):
            return current
        for attr in ("language_model", "text_model", "model"):
            if hasattr(current, attr):
                current = getattr(current, attr)
                break
        else:
            break
    return current


# ---------------------------------------------------------------------------
# Wrapping helper
# ---------------------------------------------------------------------------

class _Capture:
    """Callable wrapper that records the (first) output of `wrapped`.

    Attribute access is forwarded to the wrapped object so that callers
    that read layer flags (e.g. `layer.use_sliding`) keep working.
    """
    def __init__(self, wrapped, sink):
        object.__setattr__(self, "wrapped", wrapped)
        object.__setattr__(self, "sink", sink)

    def __call__(self, *args, **kwargs):
        out = self.wrapped(*args, **kwargs)
        hidden = out[0] if isinstance(out, tuple) else out
        self.sink.append(hidden)
        return out

    def __getattr__(self, name):
        return getattr(self.wrapped, name)


# ---------------------------------------------------------------------------
# Transformers
# ---------------------------------------------------------------------------

def collect_transformers_states(model_path, input_ids, dtype):
    """Return layer outputs as numpy arrays.

    `outputs.hidden_states` layout:
      - [0] = pre-layer-0 (embedding + pre-processing)
      - [i] = pre-layer-i = post-layer-(i-1)   for 1 <= i <= N-1
      - [N] = post-final-norm

    We return [post-layer-0, ..., post-layer-(N-2), post-final-norm],
    i.e., hidden_states[1:].  Length = N.
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

    # Skip [0] (embedding), take [1:] (layer outputs + post-norm)
    states = [h[0].float().numpy() for h in outputs.hidden_states[1:]]

    del model, outputs
    gc.collect()
    return states


# ---------------------------------------------------------------------------
# MLX
# ---------------------------------------------------------------------------

def collect_mlx_states(model_path, input_ids):
    """Return (states, dtype_str).

    states = [post-layer-0, ..., post-layer-(N-1), post-final-norm].
    Length = N + 1 if final norm exists, N otherwise.
    """
    import mlx.core as mx
    from mlx_lm import load

    print("Loading MLX model...", flush=True)
    model, _ = load(model_path)
    inner = _inner(model)

    if not hasattr(inner, "layers"):
        raise RuntimeError(
            "MLX model does not follow the expected mlx-lm structure "
            "(`model.[language_model.]model.layers`)."
        )

    captured = []
    layers = inner.layers
    original_layers = list(layers)

    try:
        for i in range(len(layers)):
            layers[i] = _Capture(original_layers[i], captured)

        inputs = mx.array([input_ids], dtype=mx.int32)
        out = model(inputs)
        mx.eval(out)
        for h in captured:
            mx.eval(h)

        # Align with transformers: hidden_states[-1] is post-final-norm,
        # not the raw output of the last layer. Replace to match.
        if hasattr(inner, "norm") and captured:
            normed = inner.norm(captured[-1])
            mx.eval(normed)
            captured[-1] = normed
    finally:
        for i in range(len(layers)):
            layers[i] = original_layers[i]

    states = [np.array(h[0].astype(mx.float32)) for h in captured]
    runtime_dtype = str(out.dtype).rsplit(".", 1)[-1]
    return states, runtime_dtype


# ---------------------------------------------------------------------------
# Comparison
# ---------------------------------------------------------------------------

def compare(t_states, mlx_states, num_layers):
    n = min(len(t_states), len(mlx_states))
    if len(t_states) != len(mlx_states):
        print(f"\nWARNING: state count mismatch — T={len(t_states)}, "
              f"MLX={len(mlx_states)}. Comparing first {n}.")

    print()
    header = (f"{'pos':<10} {'max diff':>10} {'mean diff':>10} "
              f"{'max |T|':>10} {'max |MLX|':>10} {'rel diff':>10}  status")
    print(header)
    print("-" * len(header))

    first_div = None
    for i in range(n):
        t, mlx_ = t_states[i], mlx_states[i]

        # Label: layer outputs, then post-norm
        if i < num_layers:
            lbl = f"layer {i}"
        else:
            lbl = "final*"

        if t.shape != mlx_.shape:
            print(f"{lbl:<10} SHAPE MISMATCH  T={t.shape}  MLX={mlx_.shape}")
            continue

        diff = np.abs(t - mlx_)
        max_d, mean_d = diff.max(), diff.mean()
        max_t = np.abs(t).max()
        max_mlx = np.abs(mlx_).max()
        rel = max_d / max_t if max_t > 0 else float("inf")

        if rel < 0.01:
            status = "ok"
        elif rel < 0.10:
            status = "warn"
        else:
            status = "DIVERGED"
            if first_div is None:
                first_div = i

        print(f"{lbl:<10} {max_d:>10.4f} {mean_d:>10.4f} "
              f"{max_t:>10.2f} {max_mlx:>10.2f} {rel:>9.2%}  {status}")

    print()
    if first_div is not None:
        lbl = f"layer {first_div}" if first_div < num_layers else "final*"
        print(f"First significant divergence at {lbl} "
              f"(>10% of signal magnitude).")
    else:
        print("All layers within tolerance (<10% of signal magnitude).")


# ---------------------------------------------------------------------------

def main():
    import argparse
    parser = argparse.ArgumentParser(
        description="Layer-by-layer comparison between transformers and MLX.")
    parser.add_argument("model_path")
    parser.add_argument("prompt", nargs="?", default="The")
    parser.add_argument("--t-dtype", default=None,
                        help="dtype for the transformers model "
                             "(default: match MLX runtime dtype)")
    args = parser.parse_args()

    print(f"Model: {args.model_path}")
    print(f"Prompt: {args.prompt!r}")

    from transformers import AutoTokenizer
    tokenizer = AutoTokenizer.from_pretrained(args.model_path)
    input_ids = tokenizer.encode(args.prompt)
    print(f"Token count: {len(input_ids)}")

    # Run MLX first to detect runtime dtype, then match in transformers.
    mlx_states, mlx_dtype = collect_mlx_states(args.model_path, input_ids)
    t_dtype = args.t_dtype or mlx_dtype
    t_states = collect_transformers_states(args.model_path, input_ids, t_dtype)

    # Number of decoder layers = total states minus the post-norm entry.
    # If MLX didn't find a final norm, all states are layer outputs.
    num_layers = len(mlx_states) - 1 if len(mlx_states) == len(t_states) else len(mlx_states)

    print(f"\nCollected {len(t_states)} transformers states, {len(mlx_states)} MLX states "
          f"(transformers dtype={t_dtype}, MLX dtype={mlx_dtype})")
    compare(t_states, mlx_states, num_layers)


if __name__ == "__main__":
    main()
