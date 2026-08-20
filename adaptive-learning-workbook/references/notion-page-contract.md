# Notion Page Contract

Read the connected Notion skill and its enhanced Markdown specification before creating or updating pages.

## Safe page policy

1. Fetch the linked page and inspect its ancestor.
2. Treat learner answers, marks, comments, and annotations as content to preserve.
3. When the learner has started a page, create the next page as a sibling under the same parent.
4. If the user explicitly asks to edit an existing page, fetch it immediately before the edit and use a targeted update.
5. Do not use whole-page replacement for ordinary corrections.
6. Never move, delete, or hide old learning pages to make the sequence look cleaner.

## Page title

Use:

`YYYY-MM-DD｜[Track] [Page type]：[micro-skill]`

Examples:

- `2026-07-24｜IELTS Reading 微复盘：证据判断`
- `2026-07-25｜IELTS Reading 迁移训练：用途句`

The title belongs in the Notion page property. Do not repeat it as the first content block.

## Required content order

Every practice page contains:

1. `# 今天的目标`
2. a visible `总时限：N 分钟`
3. `# 学习材料` with a direct link or included material
4. `# 操作` with explicit numbered steps
5. the practice sections
6. `# 停止规则`
7. `# 完成记录`
8. a collapsed `<details>` answer section at the end

Diagnostic pages may say `# 本次目标`, but must preserve the same functional sections.

## Input locations

Use this exact pattern:

`**你的答案：** 【　　】`

Rules:

- The brackets contain exactly two Unicode full-width spaces (`U+3000`).
- Put the label and the only input location on the same line.
- One requested response has one location.
- Do not add a bare `【　　】` on its own line.
- Do not add “在这里填写”, “在这里粘贴”, `填写：`, or `粘贴：`.
- Do not place two empty bracket pairs on one line.
- Prefer short labels that state what belongs in the field.
- Free annotations can be made directly on the material; they do not need a second worksheet field.

## Instruction design

- One action per numbered step.
- State where to look, what to produce, and when to stop.
- Supply the exact material or a direct link.
- If a task needs a special method, provide the method before the practice item.
- If an example contains the answer, label it as a worked example and use a different item for practice.
- Do not ask the learner to enter information already supplied by the page.
- Use Chinese instructions and retain useful English task language.
- Prefer ordinary headings, lists, callouts, and toggles. Avoid decorative tables and multi-column layouts.

## Plain-language review

For a Chinese worksheet, load `natural-chinese-writing` during drafting and use it again after the worksheet is otherwise complete. This is a required review step, not optional polish.

Read every learner-facing instruction aloud and check three things:

1. The learner knows exactly what to look at.
2. The learner knows the single visible action to perform.
3. The learner knows what kind of response belongs in the field.

Rewrite any sentence that only names an abstract skill or asks the learner to infer the worksheet writer's intended wording. For example:

- Avoid: `符号表不是猜图，而是重复哪一个动作？`
- Use: `每个区间选一个 test value，代入每个因子，只写正号或负号。请用一句话复述这三步。`

If the learner writes “看不懂”“不像人说的话” or annotates an instruction as unclear, classify that evidence as worksheet friction (`F`). Fix the instruction first. Do not count the unanswered or malformed response as evidence of a knowledge gap until the rewritten instruction has been tried.

## Answer section

Answers belong only at the end:

```text
<details>
<summary>完成后对照</summary>
	- 参考答案或判断标准
</details>
```

Do not reveal `正确答案`, `参考答案`, or `答案是` in the main practice content. If immediate feedback is required, split the work into separate pages instead of placing the answer above the task.

When the learner is expected to send the page for review and then check the answers, state the order on the page:

1. complete the first response without opening the answer section;
2. send the page link or mark the first response complete;
3. compare with the answer;
4. keep the first response unchanged and put corrections in a separate “二次订正” field or annotation.

Do not rely on the learner to infer whether checking happens before or after submission.

## Timing and stop rules

- Default total time: 15–25 minutes.
- Hard limit: 60 minutes.
- Break the total into short sections whose sum does not exceed the visible total.
- Include a stop rule such as:
  - one item exceeds four minutes;
  - the evidence still cannot be found after one bounded scan;
  - the total timer ends.

The learner must know whether to skip, annotate, or stop.

## Completion and reflection fields

Every field in `# 完成记录` must have a concrete diagnostic use. Ask for information that can change the next task, such as actual time, the exact step where the learner stopped, or which check repaired an answer.

- Do not add generic prompts such as “一句话总结”“说说体感” or “提取方法” unless the expected response form and its later use are explicit.
- Prefer evidence already present in answers and annotations over asking the learner to restate the same information.
- A blank reflection field does not erase a complete answer trace. Diagnose from the strongest available evidence.
- When reviewing a page, distinguish the first response, the learner's reason, any self-correction before answer reveal, and the final answer.

## Pre-create checklist

- The diagnosis and next exercise match.
- The page asks for at most two new mechanisms.
- Every field has one obvious purpose.
- Every completion or reflection field can change a later diagnosis or decision.
- No answer is revealed before it is requested.
- The page states the submission-and-correction order when first responses will be externally reviewed.
- Retrieval tests a method or relationship, not arbitrary answer memory.
- The language-appropriate writing skill has been used for a final wording review; for Chinese, this is `natural-chinese-writing`.
- Every instruction passes the “look at what / do what / write what” test when read aloud.
- The page passes `scripts/lint_lesson.py`.
