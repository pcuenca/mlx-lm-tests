# Reproducing these results

**PR:** https://github.com/pcuenca/mlx-lm/pull/5 (branch `olmo-hybrid-v2`)
**Commit:** `b0706fc8f6125a85372d1096345604a88b20d300`
**Model type:** `olmo_hybrid`

The exact scripts that produced these results are archived in `scripts/`.
The manifest used is `manifest.yaml`.

## Quick reproduction

```bash
python scripts/run_harness.py manifest.yaml
```

The harness resolves the branch to its current head sha. To reproduce
against this exact commit, check out `b0706fc8f6125a85372d1096345604a88b20d300` of `pcuenca/mlx-lm` manually
and rerun the per-test commands below.

## Per-test commands

Each `<variant>/<test>.json` file includes the exact command that was run,
its exit code, stdout, and stderr. To rerun a single test, copy the
command from there.
