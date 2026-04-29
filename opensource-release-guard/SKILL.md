---
name: opensource-release-guard
description: "Audit a repository before open-sourcing it. Use when a repo needs privacy, security, compliance, Git history, ignore-rule, or publishing-risk review before public GitHub release, then produce a ranked decision report and execute only the approved cleanup path."
---

# OpenSource Release Guard

Use this skill before a repository is made public or pushed to a public GitHub remote. It is a release gate, not a generic code review.

## Read order

1. Read this file first.
2. Use [references/checklists.md](references/checklists.md) for the audit and final re-check checklists.
3. Use [references/command-policy.md](references/command-policy.md) before running Git or filesystem-changing commands.
4. Use [references/output-schema.md](references/output-schema.md) for the report structure.
5. Use [references/history-publish-command-note.md](references/history-publish-command-note.md) only as a warning about risky history-publish commands.

## Use this skill when

- The user wants to open-source a project or publish a repo to GitHub.
- The user wants a repo checked for privacy, compliance, real-data, or release hygiene risks.
- A previous release accident makes the user need a safer release workflow.
- The repo may contain local exports, screenshots, logs, examples copied from real data, secrets, personal paths, messy Git history, or remote divergence.
- The user wants `.gitignore`, example data, release files, or publishing workflow fixed before publication.

## Do not use this skill for

- generic code review
- general security pentesting
- legal certainty about licensing
- a promise that the repo is legally perfect

Make practical judgments from evidence, and mark uncertainty clearly when legal, policy, rights, or history boundaries are unclear.

## Non-negotiable rules

- Separate audit and decision, execution, and final re-check.
- Audit first, modify second.
- Check both current working tree and Git history. Current-tree safety does not prove history safety.
- Treat `.gitignore` as future tracking control, not cleanup.
- Verify ignore behavior instead of assuming patterns do what they appear to do.
- Inspect branch and remote state before recommending pull, rebase, merge, or push.
- Require explicit approval before history rewrite, force push, remote replacement, public publication, destructive deletion, or removal of ambiguous user content.
- Prefer the safest workable release shape: cleanup, split public/private, replace real data with examples, rewrite history, or keep private.

## Required workflow

1. Freeze and snapshot: inspect Git status, remotes, current branch, recent commit graph, tracked/untracked overview, staged files, and top-level publication surface.
2. Audit the working tree: search for privacy, secrets, real data, derived data, local-only docs/scripts, build artifacts, and release hygiene issues.
3. Audit Git history: look for sensitive files, deleted data, renamed paths, historically tracked ignored files, secrets, personal identifiers, and screenshots/media.
4. Classify release readiness: choose exactly one verdict from `READY TO PUBLISH`, `READY AFTER CURRENT-TREE FIXES`, `BLOCKED BY GIT HISTORY`, `RECOMMEND SPLIT PUBLIC/PRIVATE REPO`, or `NOT READY TO OPEN-SOURCE`.
5. Rank release options: put the recommended option first, then state tradeoffs, residual risk, required actions, and publication status.
6. Plan execution: split actions into ordinary working-tree cleanup and actions requiring explicit confirmation.
7. Execute only the approved scope.
8. Re-check before the final verdict.

## Risk categories to inspect

- privacy and identity
- secrets and credentials
- real data and derived data
- Git history exposure
- repo release hygiene
- compliance and redistribution risk
- Git publishing workflow risk

## Output format

Use `audit_report`, `execution_plan`, `execution_update`, or `final_verdict` from [references/output-schema.md](references/output-schema.md). Do not dump raw command output without interpretation. Do not list files without explaining why they matter.

## Heuristics for recommendations

- Recommend cleanup-only when no meaningful Git history exposure exists and risk is limited to current files or release hygiene.
- Recommend history rewrite before publication when sensitive files or real data were committed in the past.
- Recommend split public/private repos when reusable code is mixed with non-public datasets, exports, or operational assets.
- Recommend not publishing yet when uncertainty is high, private assets are central, or the release surface is not understandable.
