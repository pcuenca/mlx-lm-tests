#!/usr/bin/env python3
"""
Layer-by-layer comparison between transformers and MLX.
Helps find where divergence starts between implementations.

Usage: python compare_layers.py <model_path> [prompt]
"""

import sys
import gc
import numpy as np


def compare_embeddings(model_path: str, input_ids: list):
    """Compare embedding layers."""
    import torch
    from transformers import AutoModelForCausalLM
    import mlx.core as mx
    from mlx_lm import load

    print("\n" + "=" * 60)
    print("EMBEDDING COMPARISON")
    print("=" * 60)

    # Transformers
    print("\nLoading transformers model...")
    tf_model = AutoModelForCausalLM.from_pretrained(
        model_path, torch_dtype=torch.float32, device_map="cpu"
    )

    tf_input = torch.tensor([input_ids], dtype=torch.long)
    with torch.no_grad():
        if hasattr(tf_model.model, 'embed_tokens'):
            tf_embed = tf_model.model.embed_tokens(tf_input)
        elif hasattr(tf_model.model, 'wte'):
            tf_embed = tf_model.model.wte(tf_input)
        else:
            print("Could not find embedding layer in transformers model")
            return None, None

    tf_embed_np = tf_embed.numpy()
    print(f"TF embedding: shape={tf_embed_np.shape}")
    print(f"  min={tf_embed_np.min():.6f}, max={tf_embed_np.max():.6f}, mean={tf_embed_np.mean():.6f}, std={tf_embed_np.std():.6f}")

    del tf_model
    gc.collect()

    # MLX
    print("\nLoading MLX model...")
    mlx_model, _ = load(model_path)

    mlx_input = mx.array([input_ids], dtype=mx.int32)
    if hasattr(mlx_model.model, 'embed_tokens'):
        mlx_embed = mlx_model.model.embed_tokens(mlx_input)
    elif hasattr(mlx_model.model, 'wte'):
        mlx_embed = mlx_model.model.wte(mlx_input)
    else:
        print("Could not find embedding layer in MLX model")
        return None, None

    mx.eval(mlx_embed)
    mlx_embed_np = np.array(mlx_embed.astype(mx.float32))
    print(f"MLX embedding: shape={mlx_embed_np.shape}")
    print(f"  min={mlx_embed_np.min():.6f}, max={mlx_embed_np.max():.6f}, mean={mlx_embed_np.mean():.6f}, std={mlx_embed_np.std():.6f}")

    # Compare
    diff = np.abs(tf_embed_np - mlx_embed_np)
    print(f"\nEmbedding diff: max={diff.max():.2e}, mean={diff.mean():.2e}")

    if diff.max() < 1e-5:
        print("PASS: Embeddings match exactly")
    elif diff.max() < 1e-3:
        print("PASS: Embeddings match within tolerance")
    else:
        print("WARN: Embedding difference detected")

    return tf_embed_np, mlx_embed_np, mlx_model


def compare_layer_outputs(model_path: str, input_ids: list, max_layers: int = 3):
    """Compare outputs after each layer."""
    import torch
    from transformers import AutoModelForCausalLM
    import mlx.core as mx
    from mlx_lm import load
    from mlx_lm.models.base import create_attention_mask

    print("\n" + "=" * 60)
    print(f"LAYER-BY-LAYER COMPARISON (first {max_layers} layers)")
    print("=" * 60)

    # Load MLX model first (we'll reuse it)
    print("\nLoading MLX model...")
    mlx_model, _ = load(model_path)

    results = []

    for layer_idx in range(max_layers):
        print(f"\n--- Layer {layer_idx} ---")

        # Transformers
        tf_model = AutoModelForCausalLM.from_pretrained(
            model_path, torch_dtype=torch.float32, device_map="cpu"
        )

        tf_input = torch.tensor([input_ids], dtype=torch.long)
        with torch.no_grad():
            # Get embedding
            if hasattr(tf_model.model, 'embed_tokens'):
                hidden = tf_model.model.embed_tokens(tf_input)
            else:
                hidden = tf_model.model.wte(tf_input)

            # Check for embedding multiplier
            if hasattr(tf_model.config, 'embedding_multiplier'):
                hidden = hidden * tf_model.config.embedding_multiplier

            # Run through layers
            # Try to get position embeddings if model uses them
            position_ids = torch.arange(hidden.shape[1]).unsqueeze(0)
            try:
                if hasattr(tf_model.model, 'rotary_emb'):
                    position_embeddings = tf_model.model.rotary_emb(hidden, position_ids)
                else:
                    position_embeddings = None
            except:
                position_embeddings = None

            for i in range(layer_idx + 1):
                layer = tf_model.model.layers[i]
                try:
                    if position_embeddings is not None:
                        hidden = layer(hidden, position_embeddings=position_embeddings)
                    else:
                        hidden = layer(hidden)
                except TypeError:
                    # Some models return tuples
                    out = layer(hidden)
                    hidden = out[0] if isinstance(out, tuple) else out

        tf_hidden_np = hidden.numpy() if isinstance(hidden, torch.Tensor) else hidden[0].numpy()
        print(f"TF layer {layer_idx}: min={tf_hidden_np.min():.4f}, max={tf_hidden_np.max():.4f}, mean={tf_hidden_np.mean():.4f}")

        del tf_model
        gc.collect()

        # MLX
        mlx_input = mx.array([input_ids], dtype=mx.int32)
        if hasattr(mlx_model.model, 'embed_tokens'):
            mlx_hidden = mlx_model.model.embed_tokens(mlx_input)
        else:
            mlx_hidden = mlx_model.model.wte(mlx_input)

        # Check for embedding multiplier
        if hasattr(mlx_model.model, 'embedding_multiplier'):
            mlx_hidden = mlx_hidden * mlx_model.model.embedding_multiplier

        mask = create_attention_mask(mlx_hidden, None)

        for i in range(layer_idx + 1):
            mlx_hidden = mlx_model.model.layers[i](mlx_hidden, mask=mask, cache=None)

        mx.eval(mlx_hidden)
        mlx_hidden_np = np.array(mlx_hidden.astype(mx.float32))
        print(f"MLX layer {layer_idx}: min={mlx_hidden_np.min():.4f}, max={mlx_hidden_np.max():.4f}, mean={mlx_hidden_np.mean():.4f}")

        # Compare
        diff = np.abs(tf_hidden_np - mlx_hidden_np)
        print(f"Diff: max={diff.max():.2e}, mean={diff.mean():.2e}")

        results.append({
            'layer': layer_idx,
            'max_diff': diff.max(),
            'mean_diff': diff.mean(),
        })

        # Early exit if divergence is significant
        if diff.max() > 10:
            print(f"\nSIGNIFICANT DIVERGENCE at layer {layer_idx} - stopping")
            break

    return results


def compare_final_layernorm(model_path: str, input_ids: list):
    """Compare output after final layernorm (before lm_head)."""
    import torch
    from transformers import AutoModelForCausalLM
    import mlx.core as mx
    from mlx_lm import load

    print("\n" + "=" * 60)
    print("FINAL LAYERNORM COMPARISON")
    print("=" * 60)

    # Transformers
    print("\nLoading transformers model...")
    tf_model = AutoModelForCausalLM.from_pretrained(
        model_path, torch_dtype=torch.float32, device_map="cpu"
    )

    tf_input = torch.tensor([input_ids], dtype=torch.long)
    with torch.no_grad():
        outputs = tf_model.model(tf_input)
        hidden = outputs[0] if isinstance(outputs, tuple) else outputs.last_hidden_state

    tf_hidden_np = hidden.numpy()
    print(f"TF final hidden: min={tf_hidden_np.min():.4f}, max={tf_hidden_np.max():.4f}, mean={tf_hidden_np.mean():.4f}")

    del tf_model
    gc.collect()

    # MLX - run full model but get hidden states
    print("\nLoading MLX model...")
    mlx_model, _ = load(model_path)

    mlx_input = mx.array([input_ids], dtype=mx.int32)
    # Call the inner model (without lm_head)
    mlx_hidden = mlx_model.model(mlx_input)
    mx.eval(mlx_hidden)
    mlx_hidden_np = np.array(mlx_hidden.astype(mx.float32))
    print(f"MLX final hidden: min={mlx_hidden_np.min():.4f}, max={mlx_hidden_np.max():.4f}, mean={mlx_hidden_np.mean():.4f}")

    # Compare
    diff = np.abs(tf_hidden_np - mlx_hidden_np)
    print(f"\nFinal hidden diff: max={diff.max():.2e}, mean={diff.mean():.2e}")

    return diff.max(), diff.mean()


def main():
    if len(sys.argv) < 2:
        print("Usage: python compare_layers.py <model_path> [prompt]")
        sys.exit(1)

    model_path = sys.argv[1]
    prompt = sys.argv[2] if len(sys.argv) > 2 else "The"

    print("=" * 60)
    print("LAYER-BY-LAYER COMPARISON")
    print("=" * 60)
    print(f"Model: {model_path}")
    print(f"Prompt: '{prompt}'")

    # Tokenize
    from transformers import AutoTokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    input_ids = tokenizer.encode(prompt)
    print(f"Tokens: {input_ids}")

    # Run comparisons
    compare_embeddings(model_path, input_ids)
    layer_results = compare_layer_outputs(model_path, input_ids, max_layers=3)

    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)

    print("\nLayer-by-layer max differences:")
    for r in layer_results:
        status = "OK" if r['max_diff'] < 1.0 else "WARN" if r['max_diff'] < 10 else "FAIL"
        print(f"  Layer {r['layer']}: max={r['max_diff']:.2e} [{status}]")

    # Find first problematic layer
    for r in layer_results:
        if r['max_diff'] > 1.0:
            print(f"\nFirst significant divergence at layer {r['layer']}")
            print("Investigate this layer's components (layernorm, attention, MLP)")
            break
    else:
        print("\nAll tested layers within tolerance")


if __name__ == "__main__":
    main()
