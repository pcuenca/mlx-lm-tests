#!/usr/bin/env python3
"""
Test harness for MLX model conversion PRs.

Checks out a PR, sets up the environment, and runs the standard test
battery against each variant specified in the manifest.

Usage:
    python run_harness.py manifest.yaml
    python run_harness.py manifest.yaml --results-dir ./results
    python run_harness.py manifest.yaml --publish
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML required: pip install pyyaml")


HARNESS_DIR = Path(__file__).resolve().parent
TEST_HARNESS_ROOT = HARNESS_DIR.parent

ARCHIVED_SCRIPTS = [
    "run_harness.py",
    "check_dtype.py",
    "compare_predictions.py",
    "compare_layers.py",
    "manifest-schema.yaml",
]

DEFAULT_RESULTS_REPO = "pcuenca/mlx-lm-tests"

BASE_GENERATE_PROMPT = (
    "The discovery of gravitational waves in 2015 confirmed a major prediction"
    " of Einstein's general theory of relativity. The implications of this"
    " discovery for our understanding of the universe are profound, as they"
    " open up entirely new ways to observe cosmic events that were previously"
    " invisible to us. In particular,"
)
INSTRUCT_GENERATE_PROMPT = (
    "Explain how a transformer neural network processes a sentence, step by step."
)
BASE_LONG_PROMPT = (
    "Write a detailed tutorial on building a web server from scratch in Python,"
    " covering sockets, HTTP parsing, routing, and error handling."
)
INSTRUCT_LONG_PROMPT = (
    "Write an HTML and JavaScript page implementing the game of space invaders."
)
NUMERICAL_PROMPT = (
    "The quick brown fox jumps over the lazy dog. This sentence contains every"
    " letter of the English alphabet at least once and has been used as a typing"
    " exercise for over a century. In the world of computing, pangrams like this"
    " one serve a practical purpose beyond mere amusement. They help test fonts,"
    " keyboards, and text rendering systems by exercising the full range of"
    " characters that a system must support. Similar sentences"
)


def log(msg):
    print(f"[harness] {msg}", flush=True)


def run_cmd(args, cwd=None, env=None, timeout=None):
    merged = {**os.environ, **(env or {})}
    try:
        return subprocess.run(
            args, cwd=cwd, env=merged, capture_output=True, text=True, timeout=timeout,
        )
    except subprocess.TimeoutExpired:
        return subprocess.CompletedProcess(args, 124, "", "TIMEOUT")


def archive_scripts(results_dir, manifest_path):
    """Copy the harness scripts and manifest into the results folder for reproducibility."""
    scripts_dest = results_dir / "scripts"
    scripts_dest.mkdir(parents=True, exist_ok=True)
    for name in ARCHIVED_SCRIPTS:
        src = HARNESS_DIR / name
        if src.exists():
            shutil.copy2(src, scripts_dest / name)
    shutil.copy2(manifest_path, results_dir / "manifest.yaml")


def write_reproduce_md(results_dir, manifest, sha):
    """Write a brief README explaining how to reproduce the tests."""
    pr = manifest["pr"]
    content = f"""# Reproducing these results

**PR:** https://github.com/{pr['repo']}/pull/{pr['number']} (branch `{pr['branch']}`)
**Commit:** `{sha}`
**Model type:** `{manifest['model_type']}`

The exact scripts that produced these results are archived in `scripts/`.
The manifest used is `manifest.yaml`.

## Quick reproduction

```bash
python scripts/run_harness.py manifest.yaml
```

The harness resolves the branch to its current head sha. To reproduce
against this exact commit, check out `{sha}` of `{pr['repo']}` manually
and rerun the per-test commands below.

## Per-test commands

Each `<variant>/<test>.json` file includes the exact command that was run,
its exit code, stdout, and stderr. To rerun a single test, copy the
command from there.
"""
    (results_dir / "reproduce.md").write_text(content)


def save_result(output_dir, name, r):
    result = {
        "command": r.args if isinstance(r.args, str) else " ".join(r.args),
        "exit_code": r.returncode,
        "stdout": r.stdout,
        "stderr": r.stderr,
    }
    with open(output_dir / f"{name}.json", "w") as f:
        json.dump(result, f, indent=2)
    return result


# ---------------------------------------------------------------------------
# Setup
# ---------------------------------------------------------------------------

def resolve_branch_sha(repo, branch):
    """Resolve a branch to its current head sha via ls-remote (no clone)."""
    repo_url = f"https://github.com/{repo}.git"
    r = run_cmd(["git", "ls-remote", repo_url, f"refs/heads/{branch}"])
    if r.returncode != 0 or not r.stdout.strip():
        sys.exit(f"Failed to resolve {repo}@{branch}:\n{r.stderr}")
    sha = r.stdout.split()[0]
    return sha


def clone_pr(manifest, work_dir, sha):
    """Clone the PR branch into work_dir/mlx-lm and check out `sha`.

    Shallow-clones the branch HEAD; if `sha` is older, fetches it explicitly.
    Skip if already present.
    """
    pr = manifest["pr"]
    repo_url = f"https://github.com/{pr['repo']}.git"
    dest = work_dir / "mlx-lm"

    if dest.exists():
        log(f"Reusing existing clone at {dest}")
        return dest

    log(f"Cloning {pr['repo']} @ {pr['branch']}...")
    r = run_cmd(["git", "clone", "--branch", pr["branch"], "--depth", "1",
                  repo_url, str(dest)])
    if r.returncode != 0:
        sys.exit(f"Clone failed:\n{r.stderr}")

    # If branch HEAD doesn't match the requested sha, fetch and check out that sha.
    head = run_cmd(["git", "rev-parse", "HEAD"], cwd=dest).stdout.strip()
    if head != sha:
        log(f"Fetching commit {sha[:7]} (branch HEAD is {head[:7]})...")
        r = run_cmd(["git", "fetch", "--depth", "1", "origin", sha], cwd=dest)
        if r.returncode != 0:
            sys.exit(f"Failed to fetch sha {sha}:\n{r.stderr}")
        r = run_cmd(["git", "checkout", sha], cwd=dest)
        if r.returncode != 0:
            sys.exit(f"Failed to checkout {sha}:\n{r.stderr}")

    return dest


def create_venv(work_dir, mlx_lm_dir):
    """Create the venv and install deps. Skip if venv already exists."""
    venv_dir = work_dir / ".venv"
    python = str(venv_dir / "bin" / "python")

    if venv_dir.exists():
        log(f"Reusing existing venv at {venv_dir}")
        return python

    def pip(*pkgs):
        r = run_cmd(["uv", "pip", "install", "--python", python, *pkgs])
        if r.returncode != 0:
            sys.exit(f"Install failed:\n{r.stderr}")

    log("Creating virtual environment...")
    r = run_cmd(["uv", "venv", str(venv_dir)])
    if r.returncode != 0:
        sys.exit(f"venv creation failed:\n{r.stderr}")

    log("Installing mlx-lm (editable)...")
    pip("-e", str(mlx_lm_dir))

    log("Installing transformers, accelerate, torch...")
    pip("transformers", "accelerate", "torch")

    return python


def download_model(repo_id, python):
    log(f"Downloading {repo_id}...")
    r = run_cmd(
        [python, "-c",
         f"from huggingface_hub import snapshot_download; snapshot_download('{repo_id}')"],
        timeout=1800,
    )
    if r.returncode != 0:
        log(f"Download warning: {r.stderr[:200]}")


# ---------------------------------------------------------------------------
# Test battery
# ---------------------------------------------------------------------------

PASS_FAIL_TESTS = {"dtype", "quant_dtype"}


def run_test(name, args, output_dir, timeout=300):
    log(f"  {name}...")
    r = run_cmd(args, timeout=timeout)
    save_result(output_dir, name, r)
    if name in PASS_FAIL_TESTS:
        status = "PASS" if r.returncode == 0 else "FAIL"
    else:
        status = "done" if r.returncode == 0 else "errored"
    log(f"  {name}: {status}")
    return r.returncode == 0


def run_battery(variant, python, output_dir, work_dir, quantize):
    vtype = variant["type"]
    model = variant["repo_id"]

    gen_prompt = BASE_GENERATE_PROMPT if vtype == "base" else INSTRUCT_GENERATE_PROMPT
    long_prompt = BASE_LONG_PROMPT if vtype == "base" else INSTRUCT_LONG_PROMPT

    # mlx-lm CLI entry points live next to the venv's python
    venv_bin = Path(python).parent
    mlx_generate = str(venv_bin / "mlx_lm.generate")
    mlx_convert = str(venv_bin / "mlx_lm.convert")

    # Test 1: dtype (run first — fast and decisive)
    run_test("dtype", [
        python, str(HARNESS_DIR / "check_dtype.py"),
        model, variant["expected_dtype"],
    ], output_dir, timeout=300)

    # Test 2: generation
    run_test("generate", [
        mlx_generate,
        "--model", model, "--prompt", gen_prompt, "--max-tokens", "200",
    ], output_dir, timeout=300)

    # Test 3: numerical comparison
    run_test("predictions", [
        python, str(HARNESS_DIR / "compare_predictions.py"),
        model, NUMERICAL_PROMPT,
    ], output_dir, timeout=900)

    # Test 5: long sequence
    run_test("long_sequence", [
        mlx_generate,
        "--model", model, "--prompt", long_prompt, "--max-tokens", "4096",
    ], output_dir, timeout=1800)

    if not quantize:
        return

    # Phase 5: quantize
    quant_dir = str(work_dir / "quantized" / variant["repo_id"].replace("/", "--"))
    ok = run_test("quantize", [
        mlx_convert,
        "--hf-path", model, "-q", "--q-bits", "4", "--mlx-path", quant_dir,
    ], output_dir, timeout=900)

    if not ok:
        return

    run_test("quant_dtype", [
        python, str(HARNESS_DIR / "check_dtype.py"),
        quant_dir, variant["expected_dtype"],
    ], output_dir, timeout=300)

    run_test("quant_generate", [
        mlx_generate,
        "--model", quant_dir, "--prompt", gen_prompt, "--max-tokens", "200",
    ], output_dir, timeout=300)


# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------

PREDICTIONS_PATTERNS = {
    "max_diff": re.compile(r"Absolute diff -.*?max:\s*([\d.eE+-]+)"),
    "mean_diff": re.compile(r"Absolute diff -.*?mean:\s*([\d.eE+-]+)"),
    "within_1e-3": re.compile(r"<\s*0\.001:\s*([\d.]+)%"),
    "within_1e-2": re.compile(r"<\s*0\.01:\s*([\d.]+)%"),
    "within_1e-1": re.compile(r"<\s*0\.1:\s*([\d.]+)%"),
    "top1": re.compile(r"Top-1 match:\s*(True|False)"),
    "top5": re.compile(r"Top-5 overlap:\s*(\d+/\d+)"),
    "top10": re.compile(r"Top-10 overlap:\s*(\d+/\d+)"),
}


def parse_predictions(stdout):
    """Extract key metrics from compare_predictions stdout. Missing keys -> '-'."""
    out = {}
    for key, pattern in PREDICTIONS_PATTERNS.items():
        m = pattern.search(stdout)
        out[key] = m.group(1) if m else "-"
    return out


def predictions_table(manifest, results_dir, suffix=""):
    """Return a markdown table with prediction metrics for all variants.

    `suffix` is "" for the unquantized case, "_quant" for the quantized one.
    Returns None if no predictions results were found.
    """
    test_name = f"predictions{suffix}"
    rows = []
    for variant in manifest["variants"]:
        slug = variant["repo_id"].replace("/", "--")
        result_path = results_dir / slug / f"{test_name}.json"
        if not result_path.exists():
            continue
        with open(result_path) as f:
            result = json.load(f)
        if result["exit_code"] != 0:
            rows.append((variant["repo_id"], None, "errored"))
            continue
        rows.append((variant["repo_id"], parse_predictions(result["stdout"]), None))

    if not rows:
        return None

    lines = [
        "| Variant | Max diff | Mean diff | <0.01 | <0.1 | Top-1 | Top-5 | Top-10 |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for repo_id, m, error in rows:
        if error:
            lines.append(f"| `{repo_id}` | — | — | — | — | — | — | _{error}_ |")
        else:
            lines.append(
                f"| `{repo_id}` | {m['max_diff']} | {m['mean_diff']} | "
                f"{m['within_1e-2']}% | {m['within_1e-1']}% | "
                f"{m['top1']} | {m['top5']} | {m['top10']} |"
            )
    return "\n".join(lines)


def write_summary(manifest, results_dir, sha):
    pr = manifest["pr"]
    pr_url = f"https://github.com/{pr['repo']}/pull/{pr['number']}"
    commit_url = f"https://github.com/{pr['repo']}/commit/{sha}"

    lines = [
        f"# Test Results: PR #{pr['number']}",
        "",
        f"- **PR:** [{pr['repo']}#{pr['number']}]({pr_url})",
        f"- **Branch:** `{pr['branch']}`",
        f"- **Commit:** [`{sha}`]({commit_url})",
        f"- **Model type:** `{manifest['model_type']}`",
        f"- **Timestamp:** {datetime.now(timezone.utc).isoformat(timespec='seconds')}",
        "",
    ]

    # Numerical comparison summary table(s)
    pred_table = predictions_table(manifest, results_dir)
    if pred_table:
        lines += ["## Numerical comparison (transformers vs MLX)", "", pred_table, ""]

    quant_pred_table = predictions_table(manifest, results_dir, suffix="_quant")
    if quant_pred_table:
        lines += ["## Numerical comparison after quantization", "", quant_pred_table, ""]

    # Per-variant detail
    for variant in manifest["variants"]:
        slug = variant["repo_id"].replace("/", "--")
        variant_dir = results_dir / slug
        lines.append(f"## {variant['repo_id']}")
        lines.append("")

        if not variant_dir.exists():
            lines.append("No results found.\n")
            continue

        for result_file in sorted(variant_dir.glob("*.json")):
            with open(result_file) as f:
                result = json.load(f)
            name = result_file.stem
            if name in PASS_FAIL_TESTS:
                label = "PASS" if result["exit_code"] == 0 else "FAIL"
            else:
                label = "errored" if result["exit_code"] != 0 else "ran"
            lines.append(f"### {name} — {label}")
            lines.append("")
            lines.append("<details><summary>stdout</summary>")
            lines.append("")
            lines.append("````text")
            lines.append(result["stdout"].strip())
            lines.append("````")
            lines.append("</details>")
            if result["exit_code"] != 0 and result["stderr"].strip():
                lines.append("")
                lines.append("<details><summary>stderr</summary>")
                lines.append("")
                lines.append("````text")
                lines.append(result["stderr"].strip())
                lines.append("````")
                lines.append("</details>")
            lines.append("")

    if manifest.get("notes"):
        lines.append("## Notes")
        lines.append("")
        lines.append(manifest["notes"])
        lines.append("")

    summary = "\n".join(lines)
    summary_path = results_dir / "summary.md"
    summary_path.write_text(summary)
    log(f"Summary written to {summary_path}")
    return summary


def push_results(results_dir, results_repo, pr_num, model_type):
    """Push results to the results repo. Returns the URL to the results folder."""
    results_dir = Path(results_dir)
    timestamp = results_dir.name
    remote_path = f"results/pr-{pr_num}/{timestamp}"
    repo_url = f"https://github.com/{results_repo}.git"

    # Clone the results repo into a temp dir, copy results, push
    with tempfile.TemporaryDirectory(prefix="mlx-results-push-") as tmp:
        tmp = Path(tmp)
        repo_dir = tmp / "repo"

        log(f"Cloning {results_repo}...")
        r = run_cmd(["git", "clone", "--depth", "1", repo_url, str(repo_dir)])
        if r.returncode != 0:
            log(f"Failed to clone results repo:\n{r.stderr}")
            return None

        dest = repo_dir / remote_path
        shutil.copytree(results_dir, dest)

        run_cmd(["git", "add", "."], cwd=repo_dir)
        run_cmd(["git", "commit", "-m",
                 f"Results for PR #{pr_num} ({model_type})"], cwd=repo_dir)
        r = run_cmd(["git", "push"], cwd=repo_dir)
        if r.returncode != 0:
            log(f"Failed to push results:\n{r.stderr}")
            return None

    results_url = f"https://github.com/{results_repo}/tree/main/{remote_path}"
    log(f"Results pushed: {results_url}")
    return results_url


def post_link(manifest, results_url):
    """Post a short comment on the mlx PR linking to the full results."""
    pr_num = manifest["pr"]["number"]
    repo = manifest["pr"]["repo"]
    model_type = manifest["model_type"]

    variants = ", ".join(v["repo_id"] for v in manifest["variants"])
    body = (
        f"**Test harness results** for `{model_type}` "
        f"({variants}):\n\n"
        f"{results_url}"
    )

    log(f"Posting link to {repo}#{pr_num}...")
    r = run_cmd(["gh", "pr", "comment", str(pr_num),
                  "--repo", repo, "--body", body])
    if r.returncode != 0:
        log(f"Failed to post comment: {r.stderr[:200]}")
    else:
        log("Link posted.")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Run MLX model conversion tests for a PR")
    parser.add_argument("manifest", help="Path to the test manifest YAML")
    parser.add_argument("--results-dir", default=None,
                        help="Directory for results (default: <test-harness>/results/pr-<N>/<timestamp>)")
    parser.add_argument("--work-dir", default=None,
                        help="Working directory for clone/venv (default: <test-harness>/work/pr-<N>)")
    parser.add_argument("--publish", action="store_true",
                        help="Push results to the results repo and post a link on the PR")
    parser.add_argument("--results-repo", default=DEFAULT_RESULTS_REPO,
                        help=f"GitHub repo for results (default: {DEFAULT_RESULTS_REPO})")
    parser.add_argument("--sha", default=None,
                        help="Run against a specific commit instead of branch HEAD "
                             "(for testing or running against an older commit).")
    args = parser.parse_args()

    with open(args.manifest) as f:
        manifest = yaml.safe_load(f)

    pr_num = manifest["pr"]["number"]

    # Resolve the branch to a sha so work and results are tied to a specific commit.
    if args.sha:
        sha = args.sha
        log(f"Using provided sha {sha} (branch HEAD not resolved)")
    else:
        sha = resolve_branch_sha(manifest["pr"]["repo"], manifest["pr"]["branch"])
        log(f"Resolved {manifest['pr']['branch']} -> {sha}")
    short_sha = sha[:7]

    # Working directory: one per (pr, sha) so re-pushes don't reuse stale code
    if args.work_dir:
        work_dir = Path(args.work_dir)
    else:
        work_dir = TEST_HARNESS_ROOT / "work" / f"pr-{pr_num}" / short_sha
    work_dir.mkdir(parents=True, exist_ok=True)

    # Results directory: includes sha so each commit's runs are distinguishable
    if args.results_dir:
        results_dir = Path(args.results_dir)
    else:
        timestamp = datetime.now().strftime("%Y-%m-%dT%H%M%S")
        results_dir = TEST_HARNESS_ROOT / "results" / f"pr-{pr_num}" / f"{short_sha}-{timestamp}"
    results_dir.mkdir(parents=True, exist_ok=True)

    # Archive scripts + manifest + write reproduction notes
    archive_scripts(results_dir, args.manifest)
    write_reproduce_md(results_dir, manifest, sha)

    log(f"PR #{pr_num} — {manifest['model_type']} @ {short_sha}")
    log(f"Results: {results_dir}")
    log(f"Work dir: {work_dir}")

    try:
        mlx_lm_dir = clone_pr(manifest, work_dir, sha)
        python = create_venv(work_dir, mlx_lm_dir)
        quantize = manifest.get("quantize", True)

        for variant in manifest["variants"]:
            slug = variant["repo_id"].replace("/", "--")
            output_dir = results_dir / slug
            output_dir.mkdir(parents=True, exist_ok=True)

            log(f"=== {variant['repo_id']} ({variant['type']}) ===")
            download_model(variant["repo_id"], python)
            run_battery(variant, python, output_dir, work_dir, quantize)

        write_summary(manifest, results_dir, sha)

        if args.publish:
            results_url = push_results(
                results_dir, args.results_repo, pr_num, manifest["model_type"])
            if results_url:
                post_link(manifest, results_url)

    finally:
        log(f"Work dir preserved at: {work_dir}")

    log("Done.")


if __name__ == "__main__":
    main()
