# Governance Rubric

Use this rubric after running the inventory script. Judge each skill on behavior, not sentiment.

## Core Tests

### 1. Trigger Distinctness

- Pass: a user would know when to invoke this skill instead of a neighboring one.
- Fail: the description is vague, generic, or interchangeable with another skill.

### 2. Behavioral Leverage

- Pass: the skill adds workflow, judgment, or resources that plain prompting would likely miss.
- Fail: the skill mostly repeats general advice the base model can already produce.

### 3. Deterministic Leverage

- Pass: the skill owns scripts, templates, schemas, or references that reduce repeated work or fragile execution.
- Fail: the skill has no reusable assets and no non-obvious procedure.

### 4. Scope Economy

- Pass: the skill has one dominant reason to exist and a bounded surface area.
- Fail: it behaves like a category page, a market shelf, or a kitchen-sink wrapper.

### 5. Validation Integrity

- Pass: success can be checked with files, output shape, or a concrete end state.
- Fail: the skill only produces aspirational guidance with no reliable completion check.

## Action Matrix

- `keep`: distinct trigger, real leverage, bounded scope, and clean validation
- `tighten`: the core capability matters, but naming, description, or metadata weakens invocation
- `merge`: two skills answer the same entry intent or share the same assets with only surface-level differences
- `split`: one skill hides multiple independently invokable workflows with different resources or validation
- `replace`: the skill is a thin wrapper around direct prompting and does not earn its token cost
- `remove`: nothing unique survives after the analysis or the stronger neighbor absorbs it

## Fast Scoring

Ask these five yes-or-no questions:

1. Would a user reliably know when to call this skill?
2. Does it outperform plain prompting in a repeatable way?
3. Does it own a script, reference, asset, or failure-prone workflow?
4. Is its scope narrower than a broad category label?
5. Can success be validated concretely?

Interpret the total:

- `5`: keep, then tighten only if metadata is weak
- `4`: keep or tighten
- `3`: tighten or merge, depending on overlap
- `2`: merge or replace
- `0-1`: replace or remove

## Delete Bias

When in doubt, delete the weaker duplicate rather than preserve both. A smaller library with sharper triggers is more useful than a large library with fuzzy boundaries.

## When External Research Is Worth It

Use external research only when the decision depends on current official reality:

- a skill format, policy, or platform rule may have changed
- a built-in model or tool capability may have made the skill obsolete
- an integration-specific workflow needs confirmation from primary docs

Do not browse just to justify a local cleanup decision. The local files are the primary evidence.
