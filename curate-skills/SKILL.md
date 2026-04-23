---
name: curate-skills
description: Audit and reorganize a skills directory using first-principles rules for trigger quality, overlap, reusable resources, and validation integrity. Use when Codex needs to analyze a collection of skills, decide which skills to keep, merge, split, replace, rename, or remove, and then directly update the skill repo so the remaining skills are leaner, more distinct, and easier to invoke.
---

# Curate Skills

## Overview

Treat a skill library as an operating system, not a market shelf. Keep only skills that create real leverage through non-obvious workflow, deterministic tooling, reusable references, or domain-specific knowledge.

## Workflow

1. Audit the target directory with `python scripts/skill_audit.py <skills-dir> --format markdown`.
2. Read [references/governance-rubric.md](references/governance-rubric.md) before deciding any structural change.
3. Read [references/change-patterns.md](references/change-patterns.md) when the right action is unclear.
4. Pick the smallest set of edits that improves trigger clarity, reduces overlap, and preserves the best reusable assets.
5. Apply the edits directly in the writable repo or copied skills tree.
6. Re-run the audit. If Anthropic `skill-creator` tooling is available, also run `quick_validate.py` on every changed skill.

## Hard Rules

- Keep a skill only if it changes behavior beyond what plain prompting already does well.
- Give each skill one dominant reason to trigger. If two skills answer the same user intent, merge or replace one.
- Split only when the sub-parts can trigger independently and have different resources, validation paths, or failure modes.
- Move deterministic operations into scripts. Keep `SKILL.md` focused on workflow, decision rules, and resource navigation.
- Keep `SKILL.md` lean. Move bulky details into `references/`.
- Update existing docs when names, paths, or user-visible behavior change. Do not create new docs just to describe the cleanup.
- Do not edit protected system skill roots in place. Work inside a writable repo or a copied skills tree.

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
3. Split overgrown skills only when the split creates cleaner triggers.
4. Tighten descriptions, names, and metadata so invocation becomes more reliable.
5. Normalize structure only as needed: `scripts/`, `references/`, `assets/`, and `agents/openai.yaml`.

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

- Rewrite vague descriptions first. Bad triggering is often the real problem.
- Remove decorative sections that do not change behavior.
- Regenerate or update `agents/openai.yaml` if it no longer matches the rewritten skill.

## Outside Research

Use local evidence first: actual skill files, metadata, scripts, references, and current repo structure.

Browse only when the decision depends on moving external reality, such as:

- a current official skill format or platform rule
- whether a built-in capability has replaced a third-party skill
- tool-specific guidance that may have changed recently

When browsing, prefer official sources and use them only to resolve the specific external question.

## Validation

At minimum:

- Re-run `python scripts/skill_audit.py <skills-dir> --format markdown`
- Confirm every changed skill still has valid frontmatter and a non-empty description
- Confirm every merge, split, or removal decision has a reason tied to trigger clarity, overlap, deterministic tooling, or reusable assets

If Anthropic `skill-creator` tooling is available, also run:

- `python /path/to/quick_validate.py <changed-skill-dir>`

## Report Back

Return:

- what changed
- why each keep, merge, split, replace, or rename decision was made
- what was validated
- any skills left for manual review and the exact missing signal
