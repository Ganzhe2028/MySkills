---
name: repo-harness-minimal
description: Create a minimal code repo harness: short AGENTS.md, feature_list.json, progress.md, and init.sh for durable agent workflow state.
---

# Repo Harness Minimal

Use only for real code repositories. Do not apply this to plain writing folders or one-off scratch directories.

## Files

Create or adapt the smallest useful set:

- `AGENTS.md`: short router for agent behavior.
- `feature_list.json`: machine-readable scope and evidence.
- `progress.md`: current state and next-session handoff.
- `init.sh`: standard setup and verification entrypoint.

Templates live in `assets/`. Copy them, then replace placeholders with repo-specific commands and feature names.

## Rules

- Keep `AGENTS.md` short. It should point to deeper docs, not become the docs.
- Work one feature at a time.
- A feature is complete only when verification has actually run and evidence is recorded.
- If the repo already has equivalent files, update them instead of duplicating them.
- Do not weaken existing project instructions or tests.
- Update existing docs when user-visible behavior or setup changes.

## Completion

The repo harness is ready when:

- startup instructions are clear
- current work is represented in `feature_list.json`
- `progress.md` states current status and next step
- `init.sh` contains real commands for the repo and can be run by the next agent
