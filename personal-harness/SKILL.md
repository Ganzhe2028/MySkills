---
name: personal-harness
description: "Route personal agent work across writing, research, config audit, debugging, skill use, lightweight coding, and harness selection. Use when a task needs a small top-level routing check before choosing the concrete skill or repo workflow."
---

# Personal Harness

Use this as the top-level router for personal agent work. Keep the result small, inspectable, and tied to the user's actual task.

## Route by task

- **Writing or analysis**: use the relevant writing skill first (`khazix-writer`, `natural-chinese-writing`, `hv-analysis`, `paper-term-explainer`, or `research-pipeline` when durable research files are needed).
- **Local agent or software configuration**: use `agent-config-audit` for the state snapshot, then `systematic-debugging` if something is broken.
- **Repeated retries or stuck runs**: use `agent-loop-guard` before more execution.
- **Skill creation or cleanup**: use `skill-creator` or `curate-skills`; keep runtime instructions concise.
- **Lightweight coding**: read the repo's own instructions first. If there is no harness and the user asks for one, use `repo-harness-minimal`.

## Five checks

For non-trivial work, identify the minimum version of these five harness parts:

1. Instructions: which file or skill tells the agent what to do.
2. State: where progress or current status persists.
3. Verification: what command, test, or review proves the result.
4. Scope: the one thing being finished now.
5. Lifecycle: how the next session can resume cleanly.

## Rules

- Prefer a skill or script over repeating long instructions in chat.
- Do not change model defaults, tokens, permissions, MCP servers, or gateway state unless the user explicitly requested that change.
- Do not add repo harness files to non-code writing folders.
- For code repos, update existing docs when behavior or usage changes.
- Report the outcome, reason, and verification evidence; do not end with optional follow-up prompts.
