---
name: paogen-wendi
description: 用“刨根问底”方式辅导学习：从一个概念、题目或 topic 倒推前置知识，找出最小必要基础，再自下而上推理整合。Use this when the user wants to deeply learn, review, or diagnose a subject by unpacking prerequisites, rebuilding understanding, practicing retrieval, or transferring the same method beyond math.
compatibility:
  - markdown
  - opencode
metadata:
  display_name: 刨根问底
  category: learning
  default_language: zh-CN
---

# 刨根问底

## Purpose

Help the learner understand something by moving in two directions:

1. **Top-down 拆解**: start from the target concept, problem, or topic and trace the prerequisite ideas it depends on.
2. **Bottom-up 重建**: start from the lowest missing foundation and rebuild the reasoning chain back to the target.

This skill is for durable learning, not quick answer delivery. It works for math, science, humanities, technical topics, exams, and general self-study.

## Read order

1. Read this file first.
2. If you need the learning-science rationale, read [references/research-foundation.md](references/research-foundation.md).
3. If you need trigger/evaluation examples, read [examples/test-prompts.md](examples/test-prompts.md).

## Use this skill when

Use this skill when the user wants to:

- learn a new concept from the roots up
- review a topic by going back to more basic knowledge
- understand why a formula, theorem, framework, event, or mechanism works
- diagnose why they cannot solve a problem
- turn a solved problem into a reusable understanding path
- build a study plan that recursively repairs missing prerequisites
- transfer the same learning method from math to another subject
- ask things like “从底层讲起”, “刨根问底”, “我基础不稳”, “一步一步推回来”, “为什么这里可以这样”, “这个东西到底依赖什么”

## Do not use this skill when

Do not use this skill for:

- a short factual answer where the user clearly wants speed
- pure homework completion where the user only wants the final answer
- broad research reports where source gathering is the main task
- motivational coaching without a concrete learning target
- medical, legal, financial, or safety-critical instruction

If the user asks for a quick answer first, answer briefly, then offer the shortest root-path only if it is needed for understanding.

## Core model

Use a four-part learning loop:

1. **Target**: define the exact thing to understand or solve.
2. **Prerequisite ladder**: identify the few concepts that are necessary, not every related concept.
3. **Root repair**: teach the lowest missing layer with examples, retrieval prompts, and self-explanation.
4. **Reconstruction**: reason upward until the learner can explain, apply, and transfer the target idea.

The goal is not to be exhaustive. The goal is to find the smallest foundation that makes the target make sense.

## Default workflow

1. **Set the target**: name the concept, problem, or topic; infer current level if visible; define what the learner should be able to do afterward. Ask only if ambiguity changes the whole route.
2. **Probe prior knowledge**: use the user's work or 3 to 5 short checks: define a term, explain a dependency, solve a tiny subproblem, classify an example, or predict a change. Classify the likely breakpoint as conceptual, representational, procedural, dependency, or misconception; output only the most likely 1 to 3 breakpoints.
3. **Build the ladder**: map `intuition -> vocabulary/symbols -> prerequisite rules/mechanisms -> target -> transfer`. Expand at most 3 to 5 key prerequisite nodes at a time, and mark layers as `solid`, `shaky`, `missing`, or `not checked`.
4. **Repair the root**: teach the lowest necessary missing layer. For each key prerequisite node, explain what it is, why it matters, how it connects to the layer above, and one minimal example or counterexample.
5. **Reconstruct upward / 回升**: do not stop after teaching the root. Push the chain back up layer by layer: from the repaired node to the next layer, then to the original target, stating what each layer gives us, why the next step follows, and where the original confusion disappears.
6. **Practice for durability**: end with near transfer, far transfer, an interleaved question, a teach-back prompt, and one spaced-review prompt.

Only descend deeper when the current layer cannot support the next inference.
Do not treat rereading as proof of learning. The learner must retrieve, explain, or apply.

## Stop descending

Stop going deeper when at least two of these are true:

- the learner can explain the current node without prompting
- the learner can use the current node to reason back to the layer above
- new errors come from fluency or practice volume, not a deeper missing concept
- continuing downward has lower value than rebuilding upward

## Output patterns

Use one of these compact structures:

- Concept learning: `目标` -> `先测基础` -> `前置知识梯` -> `从根部补起` -> `推理回来` -> `练习与复盘`
- Problem diagnosis: `题目目标` -> `卡点定位` -> `缺的前置层` -> `最低必要补课` -> `解题链条` -> `同类题检查`
- Study plan: `最终目标` -> `当前基础假设` -> `知识树` -> `学习顺序` -> `每天的检索练习` -> `迁移检查`

If the task looks like graded homework, prioritize diagnosis, hints, and learner explanation before giving a full final answer. If making a study plan, prefer a narrow first loop over a huge syllabus.

## Behavior rules

- Start from the learner's current understanding, not from a textbook table of contents.
- Make every prerequisite earn its place by explaining why the target depends on it.
- Prefer active generation over long lectures: ask the learner to explain, predict the next step, give an example, distinguish a nearby concept, or explain why a wrong path is wrong.
- Make difficulty desirable: challenging enough to require effort, not so hard that the learner cannot progress.
- Treat mistakes as diagnostic evidence and identify which layer caused them.
- Preserve the user's language line. Use Chinese by default when the user writes in Chinese.

## Quality bar

Good output locates the broken layer, explains the minimum necessary foundation, rebuilds the reasoning chain, and checks transfer.

Bad output gives a polished answer without prerequisite diagnosis, lists a giant curriculum, uses jargon before intuition, or claims understanding without retrieval and transfer.
