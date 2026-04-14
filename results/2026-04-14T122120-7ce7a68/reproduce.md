# Reproducing these results

**PR:** https://github.com/pcuenca/mlx-lm/pull/5 (branch `olmo-hybrid-v2`)
**Commit:** `7ce7a68789b7b0e5dbfb0b8d27f3f3d4b991d4a1`
**Model type:** `olmo_hybrid`

The exact scripts that produced these results are archived in `scripts/`.
The manifest used is `manifest.yaml`.

## Quick reproduction

```bash
python scripts/run_harness.py manifest.yaml
```

The harness resolves the branch to its current head sha. To reproduce
against this exact commit, check out `7ce7a68789b7b0e5dbfb0b8d27f3f3d4b991d4a1` of `pcuenca/mlx-lm` manually
and rerun the per-test commands below.

## Per-test commands

Each `<variant>/<test>.json` file includes the exact command that was run,
its exit code, stdout, and stderr. To rerun a single test, copy the
command from there.
