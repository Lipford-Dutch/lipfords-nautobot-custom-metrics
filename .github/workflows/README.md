# CI/CD workflows — intentionally disabled

**Status:** All GitHub Actions CI workflows in this repository have been
**removed on purpose** to stop consuming GitHub Actions runner minutes and
automated PR-review spend.

## What was removed

| File | What it did |
| --- | --- |
| `ci.yml` | Lint (ruff) + a Python 3.11–3.14 unit-test matrix (Nautobot 3.x with Postgres/Redis services), plus tag-gated PyPI / GitHub release publishing. |
| `upstream_testing.yml` | Scheduled upstream-compatibility testing against newer Nautobot releases. |

These files still exist in git history; nothing is lost. See **Restoring CI**
below.

## Why

CI runs and the automated code reviewer were triggering on every push, pull
request, and bot-generated dependency PR, accumulating cost with no
corresponding benefit for the current workflow. Disabling them stops that
spend at the source.

## Manual steps that must be done outside this repository

Deleting these files stops the GitHub Actions workflows, but a few cost
sources are configured **outside** the repo's workflow files and cannot be
turned off from a commit:

1. **Automated code review (ChatGPT Codex / "Code Copilot").**
   This is a GitHub App integration, not a workflow. Disable it in the Codex
   cloud settings — <https://chatgpt.com/codex/cloud/settings/general> — by
   turning off automatic PR reviews for this repository. It otherwise runs on
   every PR open / "mark ready" / `@codex review` comment.

2. **CodeQL "default setup" code scanning.**
   The `Analyze (python)` / `Analyze (actions)` jobs are GitHub Advanced
   Security CodeQL runs configured in **Settings → Code security → Code
   scanning → CodeQL analysis** as a *managed default setup* — they are
   **not** defined by any workflow file in this repo, so deleting the
   workflows above does not stop them. They run on every push/PR. To stop
   them, switch CodeQL default setup to *Disabled* in that settings page.

3. **In-progress Actions runs.**
   Automation here lacks permission to cancel runs (the API returns
   `403 Resource not accessible by integration`). Cancel any still-running
   jobs manually from the repo's **Actions** tab if needed.

4. **Dependabot (optional).**
   `.github/dependabot.yml` schedules dependency-update jobs that consume
   runner minutes and open PRs (which in turn can trigger the code reviewer).
   To pause it, comment out / remove the schedules in that file, or disable
   Dependabot in the repo's **Settings → Code security**. Note this also
   pauses automated *security* dependency updates.

## Restoring CI

To bring the workflows back, restore the files from history, e.g.:

```bash
# restore both workflow files from the commit prior to their removal
git checkout <this-commit>^ -- .github/workflows/ci.yml .github/workflows/upstream_testing.yml
```

or `git revert` the commit that removed them.
