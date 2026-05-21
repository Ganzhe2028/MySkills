---
name: defense-presentation-narrative-reviewer
description: Review defense presentations, slide outlines, or draft decks for narrative structure, evidence chain, growth logic, and visual allocation. Use when the user asks to diagnose or improve Exploration Defense / growth defense presentations, especially around story, nuclei, evidence, feedback, slide arc, or draft slides.
compatibility: opencode
---

# Defense Presentation Narrative Reviewer

Use this skill when the user provides defense slides, a slide outline, speaker notes, or a presentation draft and wants feedback on whether the story works.

The job is review and diagnosis. By default, do not edit the original slides or rewrite the whole deck unless the user explicitly asks.

## Core Standard

The presentation is not a product showcase. It is a scored defense of learning.

Judge every slide by whether it helps prove:

- what the learner originally assumed;
- what broke that assumption;
- what evidence shows the break;
- what changed in behavior;
- what the learner can now do that they could not do before.

## Source Priority

For `track-defense` work, use this source order when checking claims:

1. Official workflow, rubric, and artifact files in `RawMaterials/Rubrics/`
2. Raw evidence, memo files, Feishu documents, artifact screenshots, and feedback originals
3. Filled material banks and summarized material
4. `GUIDANCE.md`, `MEMORY.md`, and dated memory files
5. Curated reference articles and storytelling guidance cards

Do not let a polished slide claim outrank weaker raw evidence.

## Workflow

### 1. Identify Presentation Type

Classify the input as one of:

- Exploration Defense / growth defense
- Project presentation
- Portfolio or track-fit presentation
- Other

If it is not a defense or growth presentation, still give useful feedback, but label the mismatch and avoid forcing the full growth-defense structure.

### 2. Extract Candidate Nuclei

Find 4 to 6 likely nuclei: the events or decisions that change the causal chain.

For each candidate, record:

- slide number or section;
- what changed;
- what evidence supports it;
- whether removing it would break the story.

If the deck has more than 6 nuclei, recommend consolidation. If it has fewer than 4, identify missing turning points.

### 3. Check The Narrative Arc

Verify whether the deck has:

- old script: what the learner originally believed;
- breach: what broke that belief;
- low point or friction: where the old method stopped working;
- exploration: what changed in action;
- new equilibrium: what is now possible;
- reflective voice: present self looking back at past self.

Mark any missing piece as a structural issue, not a style issue.

### 4. Run The Slide-Level Checklist

For each slide or section, check:

- function: nucleus, catalyzer, index, informant, transition, or conclusion;
- evidence: raw quote, screenshot, artifact, data point, memo, or unsupported claim;
- pace: scene for turning points, summary for routine work, ellipsis for noise;
- reflection: action plus consciousness, not action alone;
- visual role: whether the layout matches the slide's narrative function.

### 5. Diagnose Emotion And Credibility

Check whether the deck avoids a flat success story.

Look for:

- V-shaped or N-shaped arc rather than straight upward progress;
- visible failure, inefficiency, or misjudgment;
- fact-feeling mismatch;
- movement from "I must change" to "I choose to change";
- specific reflections instead of abstract self-praise.

### 6. Recommend Concrete Fixes

Give edits that can be acted on slide by slide.

Prefer:

- "Move this feedback quote before the V2 screenshot"
- "Demote this process screenshot into a small catalyzer card"
- "Split this slide because the nucleus and reflection are fighting"
- "Add the original feedback sentence here"

Avoid vague feedback like:

- "Make it stronger"
- "Improve storytelling"
- "Add more emotion"

## Output Format

Default output:

```markdown
# Narrative Presentation Review

## 总判断

...

## 核心问题

| 优先级 | 问题 | 为什么影响答辩 |
| --- | --- | --- |

## Nuclei Map

| Slide/Section | Candidate nucleus | Evidence | Keep / merge / demote |
| --- | --- | --- | --- |

## 逐页反馈

| Slide/Section | Function | Issue | Specific fix |
| --- | --- | --- | --- |

## 优先修改清单

1. ...
2. ...
3. ...

## 可保留亮点

- ...
```

Keep the review direct. Do not praise filler. If a slide is busy but not meaningful, say so.

## Visual Rules

Use these visual judgments:

- Nucleus: standalone page, high contrast, large title, no side branches.
- Catalyzer: small cards, lower contrast, never the main dramatic page.
- Index: gray, draft-like, human texture, supports the person without stealing focus.
- Informant: time, version, sample size, or location in a corner label.
- Decision fork: abandoned path as dark dashed line, chosen path as bright solid line.
- Low point: black background, high-contrast text, no decorative charts.
- New equilibrium: quiet space, large proof, enough breathing room.

## Test Prompts

### Prompt 1: Draft Slides Review

`这是我的 Exploration Defense draft slides，帮我从叙事、证据链、视觉分配上审查。`

Good output:

- triggers the skill;
- identifies presentation type as Exploration Defense;
- extracts nuclei;
- returns total judgment, core issues, nuclei map, slide-level feedback, priority fixes, and retainable strengths.

Failure:

- rewrites the deck without being asked;
- only comments on visual polish;
- ignores old script, breach, evidence, and new equilibrium.

### Prompt 2: Slide Outline Review

`我还没有做 Keynote，只有 12 页大纲。帮我看这个 defense presentation 结构是否成立。`

Good output:

- triggers the skill;
- treats sections as slide candidates;
- focuses on missing nuclei, weak breach, unsupported claims, and pacing;
- does not demand visual assets that cannot exist yet.

Failure:

- says there is not enough to review;
- gives generic presentation advice.

### Prompt 3: Boundary Case

`这是一个产品发布会 deck，帮我看故事性。`

Good output:

- may use lighter narrative feedback;
- explicitly says it is not a growth defense deck;
- avoids forcing Artifact Reflection, Moonshot, or Exploration Defense scoring logic.

Failure:

- incorrectly applies the full defense rubric;
- criticizes the deck for lacking personal growth when that is not the task.
