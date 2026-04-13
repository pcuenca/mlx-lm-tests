# Reproducing these results

**PR:** https://github.com/pcuenca/mlx-lm/pull/5 (branch `olmo-hybrid-v2`)
**Commit:** `d6a3190ce8105be98ec41471d90fe16f7c149b9f`
**Model type:** `olmo_hybrid`

The exact scripts that produced these results are archived in `scripts/`.
The manifest used is `manifest.yaml`.

## Quick reproduction

```bash
python scripts/run_harness.py manifest.yaml
```

The harness resolves the branch to its current head sha. To reproduce
against this exact commit, check out `d6a3190ce8105be98ec41471d90fe16f7c149b9f` of `pcuenca/mlx-lm` manually
and rerun the per-test commands below.

## Per-test commands

Each `<variant>/<test>.json` file includes the exact command that was run,
its exit code, stdout, and stderr. To rerun a single test, copy the
command from there.
