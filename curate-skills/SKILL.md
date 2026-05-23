---
name: curate-skills
description: Audit and reorganize a skills directory so each changed skill conforms to the current Agent Skills specification and best practices for trigger quality, coherent scope, progressive disclosure, and validation. Use when an agent needs to inventory a skill library, decide which skills to keep, merge, split, replace, rename, or remove, and then edit the remaining skills so they are standards-compliant, leaner, and easier to invoke.
compatibility: Designed for Agent Skills-compatible agents with filesystem access and Python 3. Uses bundled review scripts and can also use the official `skills-ref validate` command when it is installed.
---

# Curate Skills

## Overview

Treat a skill library as an operating system, not a market shelf. Keep only skills that create real leverage through non-obvious workflow, deterministic tooling, reusable references, or domain-specific knowledge, and make every changed skill conform to the current Agent Skills standard before finishing.

## Workflow

1. Audit the target directory with `python scripts/skill_audit.py <skills-dir> --format markdown`.
2. Read [references/agent-skills-standard.md](references/agent-skills-standard.md) before touching any skill.
3. Read [references/governance-rubric.md](references/governance-rubric.md) before deciding any structural change.
4. Read [references/change-patterns.md](references/change-patterns.md) when the right action is unclear.
5. Pick the smallest set of edits that improves trigger clarity, reduces overlap, and preserves the best reusable assets.
6. Apply the edits directly in the writable repo or copied skills tree.
7. Run the separate review gate from [references/review-gate.md](references/review-gate.md). Do not finish on the basis of the audit alone.

## Hard Rules

- Keep a skill only if it changes behavior beyond what plain prompting already does well.
- Give each skill one dominant reason to trigger. If two skills answer the same user intent, merge or replace one.
- Split only when the sub-parts can trigger independently and have different resources, validation paths, or failure modes.
- Move deterministic operations into scripts. Keep `SKILL.md` focused on workflow, decision rules, and resource navigation.
- Keep `SKILL.md` lean. Move bulky details into `references/`.
- Bring every changed skill back to the current Agent Skills spec: valid frontmatter, correct directory/name match, relative file references, and portable instructions.
- Use `compatibility` only when the skill truly depends on a product, package set, operating system, network requirement, or other environment constraint.
- Keep client-specific UI metadata outside `SKILL.md`. Files such as `agents/openai.yaml` are allowed, but they do not replace spec compliance.
- Never stop after a promising diff. A changed skill is incomplete until the strict review gate reports zero blocking findings.
- Update existing docs when names, paths, or user-visible behavior change. Do not create new docs just to describe the cleanup.
- Do not edit protected system skill roots in place. Work inside a writable repo or a copied skills tree.

## Standards Contract

For every changed skill, enforce all of the following:

- `SKILL.md` exists and begins with valid YAML frontmatter.
- Frontmatter keys stay within the current spec: `name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools`.
- `name` is 1-64 characters, lowercase hyphen-case, and matches the parent directory name exactly. When folder and frontmatter name differ, **prefer the folder name** (shorter, more discoverable) and change the frontmatter to match — not the other way around.
- `description` explains both what the skill does and when to use it. If the description contains a colon followed by a space (`: `), the value must be quoted in YAML (`description: "..."`) or the YAML parser will break.
- `compatibility` is present only when the environment assumptions matter and is kept concise. Must be a plain string (`compatibility: opencode, hermes`), never a YAML list.
- File references inside `SKILL.md` use relative paths from the skill root and stay one level deep.
- `SKILL.md` stays focused enough to support progressive disclosure instead of turning into a handbook.

## Audit Output

The audit script emits:

- discovered skills and health checks
- line counts and bundled-resource signals
- overlap candidates based on names, descriptions, and headings
- action hints such as `keep`, `tighten`, `merge-candidate`, `split-candidate`, and `replace-candidate`

Treat those hints as evidence, not verdicts. Use the rubric to make the final decision.

## Decision Order

1. Remove or replace skills that do not materially outperform direct model usage.
2. Merge skills with the same entry intent or highly overlapping bundled resources.
3. Split overgrown skills only when the split creates cleaner triggers and cleaner standards compliance.
4. Tighten descriptions, names, file references, and compatibility declarations so invocation becomes more reliable.
5. Normalize structure only as needed: `scripts/`, `references/`, `assets/`, optional client metadata, and spec-compliant `SKILL.md`.

## Editing Patterns

### Merge

- Choose the better trigger surface as the survivor.
- Move unique scripts, references, and assets into the survivor before deleting anything.
- Rewrite the survivor's description around the combined intent.
- Update existing docs or links that still point at the retired skill.

### Split

- Create separate skills only when users would realistically invoke them separately.
- Give each child a narrower description and a different default prompt.
- Move variant-specific detail out of the shared `SKILL.md` and into its own references or scripts.

### Replace Or Remove

- Replace thin wrapper skills with direct model ability when they only restate obvious advice.
- Keep one short skill only if there is still a non-obvious workflow, tool contract, or reusable artifact worth preserving.

### Tighten

- Rewrite vague descriptions first. Bad triggering is often the real problem. A good description follows the golden rule: ask the reader's problem as a question, then say how this skill solves it — in plain language a beginner would understand. "你的 skill 文件夹越堆越乱？这个 skill 帮你整理" beats "系统性重构 Skill 库结构" every time.
- Remove non-standard frontmatter fields from `SKILL.md` and move client-specific metadata elsewhere.
- For bulk frontmatter cleanup across many skills, write a Python script that iterates all `SKILL.md` files: strip non-spec keys (`version`, `author`, `dependencies`, `title`, etc.), flatten nested `metadata` to string-to-string, and write back. Hand-editing 100+ files is error-prone.
- Add or remove `compatibility` based on real environment coupling, not habit.
- Remove decorative sections that do not change behavior.
- Regenerate or update `agents/openai.yaml` if it no longer matches the rewritten skill.

## Outside Research

Use local evidence first: actual skill files, metadata, scripts, references, and current repo structure.

Browse only when the decision depends on moving external reality, such as:

- a current official skill format or platform rule
- whether a built-in capability has replaced a third-party skill
- tool-specific guidance that may have changed recently

When browsing, prefer official sources and use them only to resolve the specific external question.

## Separate Review Gate

Run a separate final pass with:

- `python scripts/strict_review.py <skills-dir-or-skill> --strict-warnings --format markdown`

The review gate is mandatory and independent from the editing pass. It must check:

- spec compliance
- portability and file references
- progressive disclosure limits
- trigger clarity and compatibility usage
- stale artifacts such as TODOs or OS junk files

Note: the `absolute-path` check in `strict_review.py` is overbroad — it flags slash commands (`/model`), relative markdown links (`/references/foo.md`), URL fragments, and model names as false positives. Real issues are limited to workstation paths like `/Users/...`, `/tmp/...`, `/opt/...`. Manually verify each absolute-path failure before acting on it.

If the official `skills-ref` validator is installed, run it as an additional check. Treat any failure from either validator as blocking.

Only proceed to final reporting when the strict review gate has no blocking findings.

## Validation Loop

1. Make the changes.
2. Run the strict review gate.
3. Fix every failure and every warning that is realistically fixable.
4. Run the strict review gate again.
5. Re-run `python scripts/skill_audit.py <skills-dir> --format markdown` for a final inventory view.

## Report Back

Return:

- what changed
- why each keep, merge, split, replace, or rename decision was made
- what the strict review gate checked and whether it passed cleanly
- any skills left for manual review and the exact missing signal
