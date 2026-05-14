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
    python compare_layers.py <model_path> [prompt] --trust-remote-code
    python compare_layers.py <model_path> --reference-from ref.safetensors

When --reference-from is set, the transformers forward pass is skipped and
hidden states + logits come from the precomputed safetensors (produced by
compute_reference.py). Used when the HF reference can only run on CUDA.
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

def _make_capture(wrapped, sink):
    """Create a capture wrapper that passes ``isinstance`` checks.

    Hybrid models (e.g. OLMo Hybrid) dispatch different masks to
    different layer types via ``isinstance``.  A plain wrapper class
    would break those checks.  We solve this by dynamically creating a
    subclass of the wrapped object's class that overrides ``__call__``
    to record the output, and ``__getattr__`` for forwarding.
    """
    base = type(wrapped)

    class _Capture(base):
        def __init_subclass__(cls, **kw):
            pass

        def __init__(self):
            # Skip base __init__; we proxy everything to `wrapped`.
            pass

        def __call__(self, *args, **kwargs):
            out = wrapped(*args, **kwargs)
            hidden = out[0] if isinstance(out, tuple) else out
            sink.append(hidden)
            return out

        def __getattr__(self, name):
            return getattr(wrapped, name)

    return _Capture()


# ---------------------------------------------------------------------------
# Transformers
# ---------------------------------------------------------------------------

def load_reference_states(path):
    """Load reference states from a precomputed safetensors.

    Returns the same shape compare() expects from a live transformers run:
      [post_layer_0, ..., post_layer_{N-2}, post_norm, logits]
    plus the input_ids and metadata for cross-checking.
    """
    from safetensors import safe_open
    with safe_open(path, framework="numpy") as f:
        keys = set(f.keys())
        metadata = f.metadata() or {}
        # post_layer_0 .. post_layer_K
        layer_keys = sorted(
            (k for k in keys if k.startswith("post_layer_")),
            key=lambda k: int(k.rsplit("_", 1)[-1]),
        )
        states = [f.get_tensor(k) for k in layer_keys]
        states.append(f.get_tensor("post_norm"))
        states.append(f.get_tensor("logits"))
        input_ids = f.get_tensor("input_ids").tolist()
    return input_ids, states, metadata


def collect_transformers_states(model_path, input_ids, dtype, trust_remote_code=False):
    """Return layer outputs as numpy arrays.

    `outputs.hidden_states` layout (for the common "append-before-layer"
    convention used by Llama, BailingMoeV2_5, etc.):
      - [0]               = embedding (input to layer 0)
      - [i] for 1<=i<=N-1 = input to layer i (= output of layer i-1)
      - [N]               = post-final-norm
      - [N+1..]           = optional model-specific extras (e.g. MTP layer
                            outputs in BailingMoeV2_5)

    We return [layer_0_out, ..., layer_{N-2}_out, post-final-norm, logits]
    by slicing hidden_states[1:N+1] explicitly so we skip anything appended
    after the post-final-norm.
    """
    import torch
    from transformers import AutoModelForCausalLM

    torch_dtype = getattr(torch, dtype)
    print(f"Loading transformers model (dtype={dtype})...", flush=True)
    model = AutoModelForCausalLM.from_pretrained(
        model_path,
        torch_dtype=torch_dtype,
        device_map="cpu",
        trust_remote_code=trust_remote_code,
    )

    inputs = torch.tensor([input_ids], dtype=torch.long)
    with torch.no_grad():
        outputs = model(inputs, output_hidden_states=True)

    num_hidden_layers = model.config.num_hidden_layers
    states = [
        h[0].float().numpy()
        for h in outputs.hidden_states[1 : num_hidden_layers + 1]
    ]

    states.append(outputs.logits[0].float().numpy())

    del model, outputs
    gc.collect()
    return states


# ---------------------------------------------------------------------------
# MLX
# ---------------------------------------------------------------------------

def collect_mlx_states(model_path, input_ids, trust_remote_code=False):
    """Return (states, dtype_str).

    states = [post-layer-0, ..., post-layer-(N-2), post-final-norm, logits].
    The last layer output is replaced with the post-final-norm state to
    match transformers' ``output_hidden_states`` convention.
    """
    import mlx.core as mx
    from mlx_lm import load

    print("Loading MLX model...", flush=True)
    tokenizer_config = {"trust_remote_code": True} if trust_remote_code else None
    model, _ = load(model_path, tokenizer_config=tokenizer_config)
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
            layers[i] = _make_capture(original_layers[i], captured)

        inputs = mx.array([input_ids], dtype=mx.int32)
        out = model(inputs)
        mx.eval(out)
        for h in captured:
            mx.eval(h)

        # Transformers' output_hidden_states replaces the last layer
        # output with the post-final-norm state.  Do the same here.
        if hasattr(inner, "norm") and captured:
            normed = inner.norm(captured[-1])
            mx.eval(normed)
            captured[-1] = normed

        # Append logits [batch, seq, vocab] — h[0] below strips the batch dim
        mx.eval(out)
        captured.append(out)
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

        # Label: layer outputs, post-norm, logits
        if i < num_layers:
            lbl = f"layer {i}"
        elif i == num_layers:
            lbl = "post-norm"
        else:
            lbl = "logits"

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
    parser.add_argument("--trust-remote-code", action="store_true",
                        help="Pass trust_remote_code=True when loading the HF "
                             "model and tokenizer.")
    parser.add_argument("--reference-from", default=None,
                        help="Path to a precomputed reference safetensors "
                             "(produced by compute_reference.py). When set, "
                             "skips the live transformers forward pass.")
    args = parser.parse_args()

    print(f"Model: {args.model_path}")
    print(f"Prompt: {args.prompt!r}")
    print(f"trust_remote_code: {args.trust_remote_code}")
    if args.reference_from:
        print(f"reference_from: {args.reference_from}")

    if args.reference_from:
        ref_input_ids, t_states, ref_meta = load_reference_states(
            args.reference_from
        )
        ref_prompt = ref_meta.get("prompt") if ref_meta else None
        if ref_prompt is not None and ref_prompt != args.prompt:
            print("WARNING: Reference prompt does not match the prompt passed "
                  "to this script. Comparison results will be meaningless.")
        input_ids = ref_input_ids
        print(f"Token count: {len(input_ids)} (from reference)")
        if ref_meta:
            print(f"Reference metadata: {ref_meta}")
        mlx_states, mlx_dtype = collect_mlx_states(args.model_path, input_ids, trust_remote_code=args.trust_remote_code)
        t_dtype = ref_meta.get("compute_dtype", "unknown") if ref_meta else "unknown"
    else:
        from transformers import AutoTokenizer
        tokenizer = AutoTokenizer.from_pretrained(
            args.model_path, trust_remote_code=args.trust_remote_code
        )
        input_ids = tokenizer.encode(args.prompt)
        print(f"Token count: {len(input_ids)}")

        # Run MLX first to detect runtime dtype, then match in transformers.
        mlx_states, mlx_dtype = collect_mlx_states(args.model_path, input_ids, trust_remote_code=args.trust_remote_code)
        t_dtype = args.t_dtype or mlx_dtype
        t_states = collect_transformers_states(
            args.model_path, input_ids, t_dtype,
            trust_remote_code=args.trust_remote_code,
        )

    # Both sides: [layer outputs..., post-norm, logits].
    # Number of decoder layers = total - 2 (post-norm + logits).
    num_layers = len(mlx_states) - 2 if len(mlx_states) == len(t_states) else len(mlx_states)

    print(f"\nCollected {len(t_states)} transformers states, {len(mlx_states)} MLX states "
          f"(transformers dtype={t_dtype}, MLX dtype={mlx_dtype})")
    compare(t_states, mlx_states, num_layers)


if __name__ == "__main__":
    main()
