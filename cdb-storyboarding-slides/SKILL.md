---
name: cdb-storyboarding-slides
description: Plan or review slides, storyboards, presentation flow, Magic Move, morph transitions, and audience attention. Use when the user asks for slide design, deck structure, storyboard, presentation critique, or how to prevent the audience from losing focus.
---

# CDB Storyboarding Slides

Use this skill to create or review presentation sequences where the audience must follow a visual and spoken path.

## Core Position

A slide is not a document page. A slide is a timed information unit. Storyboarding decides what the audience sees first, what changes, and why the change matters.

## Workflow

1. Define audience and presentation goal.
2. Split the material into timed beats, not paragraphs.
3. For each slide, assign one main message.
4. Define attention path: first look, second look, supporting detail.
5. Decide whether a transition is needed:
   - reveal: show information step by step
   - compare: make difference visible
   - transform: show state change
   - move: show spatial relation
6. Remove large paragraphs unless the task explicitly requires reading.
7. Check that speech, visual change, and audience reading do not compete.
8. For teaching, worked-example, or symbolic-reasoning slides, read `references/teaching-slide-reasoning.md` and decide the learning mode, reasoning trace, and pagination before styling.

## Output Format

```markdown
## Storyboard
| Slide | Main message | First look | Visual structure | Transition purpose | Speaker note |
|---:|---|---|---|---|---|

## Attention Risks
- ...

## Text Reduction
- Keep:
- Cut:
- Convert to visual:
```

## Checks

- Do not add Magic Move only for decoration.
- Do not place long paragraphs on slides.
- If a slide has multiple focal points, split it or reveal it.
- If the audience may lose focus, reduce simultaneous reading, listening, and animation demands.
- Render structural notation as structural notation. Do not use raw LaTeX source or slash text when a fraction, matrix, radical, or hierarchy carries meaning.
- A worked example should expose source state, target, operation, result, and conclusion. Highlighting must track the same object across those states.
- If two or more independent reasoning chains need full explanations, split them into separate slides unless comparison itself is the learning objective.
- Do not label a slide retrieval if the answer or complete solution is already visible. Choose guided example, retrieval check, or comparison deliberately.
- A retrieval check must preserve productive struggle: do not pre-solve the decisive step the learner is meant to execute.

## Working with the CDB suite

- Storyboarding output feeds `cdb-layout`, `cdb-typography`, and `cdb-color` for the visual system.
- Close the loop with `cdb-design-review` to score Functionality, Efficiency, Emotion and verify the fixes.

## Sources

- Read `references/cdb-source-map.md` for source PDFs and pages.
- Read `references/teaching-slide-reasoning.md` for teaching-mode selection, reasoning visibility, math notation, density triggers, and pagination QA.
