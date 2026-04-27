# AGENTS.md

This repository is designed for coding-agent work. The goal is to leave the repo restartable and easy to inspect after every task.

## Startup

Before editing:

1. Confirm the working directory with `pwd`.
2. Read `progress.md`.
3. Read `feature_list.json`.
4. Review recent changes with `git status --short` and `git log --oneline -5`.
5. Run `./init.sh`.

If baseline verification fails, fix or report that before starting new feature work.

## Rules

- Work on one feature at a time.
- Keep changes inside the selected feature unless a narrow supporting fix is required.
- Do not mark work complete without verification evidence.
- Do not weaken tests or verification commands to get a pass.
- Update existing docs when behavior or setup changes.

## Done

A feature is done only when:

- target behavior is implemented
- required verification passed
- evidence is recorded in `feature_list.json` or `progress.md`
- the repo can restart through `./init.sh`

