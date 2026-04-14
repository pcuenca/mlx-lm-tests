# mlx-lm-tests

This is a test harness for transformers-to-mlx model conversions. It is designed to be run on conversions performed by the transformers-to-mlx Skill, but it is not agentic - tests run deterministically instead of driven by an LLM.

Why?

- To ensure the conversion Skill did not hallucinate results or was too complacent with them.
- For reproducibility. Anyone can download this repo and run the tests.
- For documentation and transparency. All results are saved at various levels: [summary reports](https://github.com/pcuenca/mlx-lm-tests/blob/main/results/pr-5/2026-04-14T122120-7ce7a68/summary.md#layers--ran), [per-model details](https://github.com/pcuenca/mlx-lm-tests/blob/main/results/pr-5/2026-04-14T122120-7ce7a68/summary.md#allenaiolmo-hybrid-instruct-sft-7b), [raw inputs/outputs](https://github.com/pcuenca/mlx-lm-tests/tree/main/results/pr-5/2026-04-14T122120-7ce7a68/allenai--Olmo-Hybrid-Instruct-SFT-7B) saved as JSON files. The [tests](https://github.com/pcuenca/mlx-lm-tests/tree/main/results/pr-5/2026-04-14T122120-7ce7a68/scripts) are also copied to results folders so we know what we ran even if we make changes to the harness in the future.

## Typical Workflow

You use the transformers-to-mlx conversion Skill and open a PR. As a side-effect, a PR to this repo will be opened as well, consisting of a small yaml manifest file with some metadata about the conversion. [Here's an example](https://github.com/pcuenca/mlx-lm-tests/blob/main/manifests/pr-5.yaml). It lists the models to test, the repo where the conversion PR was opened, how much memory we expect to use during inference for each model variant.

The mantainers of this repo (currently [`@pcuenca`](https://github.com/pcuenca)) can merge the manifest and run the tests on our infra. We have a couple of Big Macs (M3 Ultra with 512 GB of RAM) so we can handle big checkpoints. Alternatively, you con clone this repo locally and run the tests yourself by issuing a command like:

```bash
python harness/run_harness.py manifests/pr-5.yaml
```

The test harness will use `uv` to create and use a virtual Python environment to run the tests. A new environment is created per commit hash (more about this below). Virtual environments are saved to the `work` directory; you can safely delete them when you are done.

Test results are saved to `results`, and are uniqued by: conversion PR, date, commit hash. If you run the tests yourself, feel free to open a PR to this repo with all the results.

## How to iterate during review

You open a PR with the conversion skill. Then we run the harness and share the results. During review of your MLX modeling code, you are asked to refactor a few things. You do, and push new commits to the MLX repo. At this point you can re-run the harness to test again and see if anything broke.

It's also possible to refer to a specific revision when you launch the tests. This is useful to compare against previous versions while looking for regressions. Do it like this:

```bash
python harness/run_harness.py manifests/pr-5.yaml --sha d6a3190
```

## Why not add this as part of the CI?

This is not a CI gate. Some tests are pretty straightforward (are dtypes correct?), but most are qualitative. Is it normal that a pre-trained model tends to repeat itself when asked to generate a long sequence? Is a relative logits difference of 4% against the transformers codebase "normal"?

Tests are designed to provide additional signal to the reviewer and the contributor, and we use the typical generations we run when converting models. Assessing whether results are good or bad is a judgement call based on experience with previous models that follow similar architectures.

## Contributions

This is experimental an in-progress. Feel free to open suggestions or PRs!

