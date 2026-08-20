---
name: adaptive-learning-workbook
description: Continue an ongoing self-study or practice loop by reading the learner's latest work or annotations, diagnosing the smallest actionable bottleneck, and creating the next low-friction, editable Notion worksheet. Use when the user says they finished a study task, shares marks or annotations, asks “what's next”, reports they could not continue, or asks to turn feedback into the next practice page. Especially useful for IELTS and ESL practice, but reusable for other learning tracks. Do not use for one-off explanations or ordinary writing requests with no continuing practice loop.
---

# Adaptive Learning Workbook

Turn real learner behavior into the next small, executable practice task:

`work → evidence → diagnosis → next worksheet → annotation → transfer`

The purpose is not to produce impressive lesson plans. The purpose is to make the next useful action obvious, editable, and easy to start.

## Read order

1. Read [references/learner-contract.md](references/learner-contract.md) every time.
2. Read [references/learning-method.md](references/learning-method.md) before diagnosing work or choosing the next task.
3. Read [references/notion-page-contract.md](references/notion-page-contract.md) before creating or editing a Notion page.
4. For Chinese worksheets, load `natural-chinese-writing` before drafting and use it again during the final wording review. For other languages, load the closest available plain-language or writing skill.
5. For IELTS Reading, also read [references/ielts-reading-adapter.md](references/ielts-reading-adapter.md).
6. Select one matching template from `assets/` and adapt it to the learner's evidence.

## Default workflow

### 1. Collect evidence

Start from the learner's actual work, not a general impression.

- If the user links a Notion page, fetch it.
- If the user mentions marks, annotations, comments, or an attached record, read them.
- If the user says they could not continue, inspect what they completed, where they stopped, and what instructions or material were present.
- Treat the linked or attached work as the current source of truth. Dynamic progress remains in Notion, not inside this skill.
- Separate four layers when they are available: the first response, the stated reason, any self-correction made before answer reveal, and the final answer. Do not let a correct final answer erase an incorrect reason or an earlier repair.
- Treat “I was stuck on X” as evidence of the learner's experience, not automatically as the location of the academic bottleneck. Compare it with the step-by-step work.

Do not infer a stable personal trait from one attempt. Describe visible events such as:

- selected a keyword that did not answer the question;
- located the right sentence but could not integrate its clauses;
- could not tell where to type;
- stopped after the task exceeded the current processing capacity.

### 2. Diagnose the smallest bottleneck

Use the `K/P/S/O/E/F` taxonomy in the learning method reference. Select at most two bottlenecks for the next worksheet.

Locate the earliest broken conversion in the task chain: the last step the learner completed correctly followed by the first step that became wrong or unclear. Preserve or supply the earlier correct work and practise only the next conversion when possible.

Distinguish:

- a language or knowledge problem;
- a task-strategy problem;
- processing overload;
- output difficulty;
- execution error;
- worksheet or instruction friction.

Do not turn every problem into “study more vocabulary” or “do a full mock test”.

### 3. Choose the next task

Choose one page type:

- `diagnostic-page.md`: the learner stopped, misunderstood the format, or the evidence is still unclear;
- `micro-practice-page.md`: one or two mechanisms need isolated practice;
- `transfer-page.md`: the learner succeeded with familiar material and must apply the method to new material.

Keep the task between 15 and 25 minutes by default. The hard limit is 60 minutes.

If the next step is clear, create it without asking the user to approve routine details. Ask only when:

- the learning direction would change;
- the task would exceed 60 minutes;
- a purchase or paid resource is required;
- the available evidence cannot distinguish materially different next steps;
- the operation could alter or remove existing user content.

### 4. Set the scaffold level

Use three levels:

1. **Full scaffold**: explicit steps, one action per line, bounded hints, fixed answer locations.
2. **Reduced scaffold**: goal, sequence, and checks remain; some hints and sentence starters are removed.
3. **Independent practice**: task, time limit, and acceptance criteria only.

Move down one support level after two consecutive successful transfer tasks on the same micro-skill with no instruction friction. Move up one level after abandonment, instruction confusion, or transfer failure. Do not remove support merely because the learner completed one familiar item.

Advancing to the next curriculum topic is not the same as fading support. A learner may move on after a correct new-material transfer with an explicit self-correction, while the next page retains one short checkpoint for the repaired rule.

### 5. Build and validate the worksheet

Follow the Notion page contract exactly.

Before creating the page:

1. Draft the page as Notion-flavored Markdown.
2. Check that every response has one unambiguous input location.
3. Check that no instruction, hint, or supplied sentence already reveals the response being requested.
4. Run a wording review with the language-appropriate writing skill. For Chinese, use `natural-chinese-writing` and read every learner-facing sentence aloud. Replace any sentence that names an abstract operation without saying what the learner should actually do.
5. Run the plain-language test: after reading one instruction, the learner must be able to point to the material, perform one visible action, and know what belongs in the answer field. If any of those three are unclear, classify it as worksheet friction (`F`) and rewrite the instruction before judging the learner's knowledge.
6. Run:

```bash
python3 <this-skill-directory>/scripts/lint_lesson.py PATH_TO_DRAFT.md
```

Fix every error before creating the Notion page.

### 6. Create safely in Notion

- Default to a new sibling page when the learner has written in the current page.
- Resolve the parent from the linked page's ancestor first; otherwise use the learning-track mapping in the learner contract.
- Never replace a completed or partially completed learning page.
- If the user explicitly asks for an edit, fetch the latest page again and make the smallest targeted update.
- Read the connected Notion skill and enhanced Markdown specification before writing.

### 7. Return a compact handoff

After creating the page, return only:

- the evidence-based diagnosis;
- the page link;
- the task's objective and total time.

Do not append a long lecture or ask whether the user wants the next step. The page is the next step.

## Critical quality rules

- A worksheet is an editable work surface, not an essay, report, or decorative dashboard.
- Use `【　　】` for every empty input position: exactly two full-width spaces.
- Never create two apparent places for the same answer.
- Never ask the learner to fill an answer already revealed by the instruction.
- Treat “看不懂这句话”“不像人说的话” and similar comments as direct worksheet-friction (`F`) evidence. Rewrite the wording before adding academic explanation or judging the learner's ability.
- Prefer literal actions over pedagogical labels. “每个区间选一个数，代入各因子，只写正负号” is usable; “符号表是在重复哪一个动作” makes the learner guess what the worksheet writer means.
- A correct final answer with an incorrect reason is not successful transfer. A self-correction made before the answer is revealed is evidence of emerging control, not yet automaticity.
- Completion and reflection fields must change a later diagnosis or decision. Remove generic prompts such as “总结一下” or “说说体感” when the answer trace and annotations already provide the needed evidence.
- State the submission order whenever answers are hidden for later checking: complete and preserve the first response, send or mark it complete, then compare. Corrections belong in a separate field or annotation and must not overwrite the first response.
- Do not use closed-book recall to test arbitrary answer letters. Retrieval should recover a method, relationship, or transferable rule, or apply it to new material.
- Keep worked examples visibly separate from independent practice.
- Put answers only in a collapsed answer section at the end.
- Give direct material links or include the practice material. Do not make the learner search for what to use.
- Include a stop rule so the learner knows when to move on.

## Boundaries

Do not trigger this skill for:

- a one-off concept explanation with no ongoing practice task;
- writing or rewriting an ordinary email, essay, or translation;
- broad study advice when the user has not supplied a learning goal or current evidence;
- high-stakes psychological or medical conclusions about attention or motivation.

If the Notion connector is unavailable, produce the same worksheet content in chat or a local draft, state that the page could not be created, and preserve the page contract for later use.
