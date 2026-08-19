---
name: cdb-design-review
description: Review visual designs with the CDB Functionality, Efficiency, and Emotion model. Use when the user asks for CDB standard review, poster critique, slide critique, design feedback, or whether a visual design actually works.
---

# CDB Design Review

Use this skill to review posters, slides, UI screens, visual drafts, and information graphics through CDB’s design lens.

## Core Model

CDB review is not taste review. Judge the work through:

- Functionality: does it serve the message, task, user, and output context?
- Efficiency: does it reduce reading, recognition, and operation cost?
- Emotion: does the feeling support the message without competing with it?

If the user did not provide task, audience, or output context, infer a reasonable default from the artifact and mark it as an assumption.

## Review Workflow

1. State the design task in one sentence.
2. Identify the target audience and the first message they need to understand.
3. Score Functionality, Efficiency, and Emotion from 0 to 4.
4. List priority issues in order of user impact.
5. For each issue, say what to observe, why it matters, how to fix it, and how to verify the fix.
6. Name what should stay unchanged so the next revision does not destroy working parts.

## Output Format

Use this structure:

```markdown
## Verdict
[One direct sentence.]

## F.E.E. Score
| Dimension | Score | Reason |
|---|---:|---|
| Functionality | 0-4 | ... |
| Efficiency | 0-4 | ... |
| Emotion | 0-4 | ... |

## Priority Fixes
- [P0-P3] Problem: ...
  Reason: ...
  Fix: ...
  Verify: ...

## Keep
- ...

## Revision Checklist
- ...
```

## Checks

- Do not say only that a design is beautiful or ugly.
- Do not give generic UI advice without tying it to message, audience, reading order, or output context.
- For slides, check attention path and text load.
- For posters, check first glance, second glance, print or screen output, image quality, color contrast, type hierarchy, and layout.
- For icon or shape work, check semantic clarity and visual consistency.

## Working with the CDB suite

- Review sits at the end of the build chain: `cdb-storyboarding-slides` sets one task per slide, `cdb-layout` / `cdb-typography` / `cdb-color` carry the visual system, this skill accepts or rejects the result.

## Sources

Read `references/cdb-source-map.md` for source PDFs and pages.
