#!/usr/bin/env python3
"""Verify that a model's forward-pass output dtype matches the expected dtype."""
import json
import sys

import mlx.core as mx
from mlx_lm import load


def main():
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <model_path> <expected_dtype>", file=sys.stderr)
        sys.exit(1)

    model_path = sys.argv[1]
    expected_name = sys.argv[2]
    expected = getattr(mx, expected_name)

    model, _ = load(model_path)

    out = model(mx.array([[1]]))
    mx.eval(out)

    result = {
        "output_dtype": str(out.dtype),
        "expected_dtype": str(expected),
        "match": out.dtype == expected,
    }
    print(json.dumps(result, indent=2))

    if not result["match"]:
        print(f"FAIL: output dtype {out.dtype} != {expected_name}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
