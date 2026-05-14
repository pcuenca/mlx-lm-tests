# Reproducing these results

**PR:** https://github.com/ivanfioravanti/mlx-lm/pull/1227 (branch `add-ling-2.6-flash`)
**Commit:** `4d4758dca32f03b66bf3224e5be030b61e4e9237`
**Model type:** `bailing_hybrid`

The exact scripts that produced these results are archived in `scripts/`.
The manifest used is `manifest.yaml`.

## Quick reproduction

```bash
python scripts/run_harness.py manifest.yaml
```

The harness resolves the branch to its current head sha. To reproduce
against this exact commit, check out `4d4758dca32f03b66bf3224e5be030b61e4e9237` of `ivanfioravanti/mlx-lm` manually
and rerun the per-test commands below.

## Per-test commands

Each `<variant>/<test>.json` file includes the exact command that was run,
its exit code, stdout, and stderr. To rerun a single test, copy the
command from there.
