#!/usr/bin/env python3
"""Verify that a model's forward-pass output dtype matches the expected dtype."""
import argparse
import json

import mlx.core as mx
from mlx_lm import load


def main():
    parser = argparse.ArgumentParser(
        description="Verify a model's forward-pass output dtype.")
    parser.add_argument("model_path")
    parser.add_argument("expected_dtype")
    parser.add_argument("--trust-remote-code", action="store_true",
                        help="Pass trust_remote_code=True to mlx_lm.load's "
                             "tokenizer config. Required for custom-code "
                             "models — mlx_lm.utils.load (unlike sharded_load) "
                             "doesn't default this on.")
    args = parser.parse_args()

    tokenizer_config = {"trust_remote_code": True} if args.trust_remote_code else None

    expected = getattr(mx, args.expected_dtype)

    model, _ = load(args.model_path, tokenizer_config=tokenizer_config)

    out = model(mx.array([[1]]))
    mx.eval(out)

    result = {
        "output_dtype": str(out.dtype),
        "expected_dtype": str(expected),
        "match": out.dtype == expected,
    }
    print(json.dumps(result, indent=2))

    if not result["match"]:
        import sys
        print(f"FAIL: output dtype {out.dtype} != {args.expected_dtype}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
