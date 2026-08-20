# Trigger and behavior cases

Use these cases for qualitative trigger review. They are based on real workflow failures rather than synthetic wording.

| Prompt | Trigger? | Good behavior | Failure |
| --- | --- | --- | --- |
| “done，我把 marks 放在页面里了，你看看。” | Yes | Read the page and marks, diagnose visible evidence, create the next worksheet when clear | Give generic praise or ask whether to make a page |
| “今天拖了一个小时，做不下去了。” | Yes | Inspect the attempted task, distinguish format exposure from a valid test, reduce the next task | Treat the attempt as a score or prescribe another full mock |
| “so what's next?” after a completed worksheet | Yes | Resolve the current track and create a new sibling page | Return only advice and require another user message to create it |
| “把反馈做成今天能直接练的 Notion 学案。” | Yes | Create a validated 15–25 minute editable page | Produce an essay-like lesson plan or ambiguous input areas |
| “这个提示我看不懂，不像人说的话。” | Yes | Classify the comment as worksheet friction, rewrite the instruction as a concrete action, and run the Chinese wording review again | Diagnose a knowledge gap, defend the original wording, or merely add more explanation |
| “我几乎都卡在符号”，但三个区间的符号全对、最终区间写错 | Yes | Preserve the self-report as experience evidence, then localize the bottleneck at the sign-to-interval conversion and practise only that step | Reteach the entire sign table or accept the self-label as the diagnosis |
| Final answer is correct, the written reason is wrong, or the learner corrected it before answer reveal | Yes | Record first response, reason, self-correction, and final answer separately; treat self-correction as emerging control and retain a short checkpoint | Mark the skill mastered from the final answer alone or ignore the repair process |
| “到底先对照答案还是先发给你？我订正后你会分不清。” | Yes | State the order explicitly: first response → send → compare → separate correction; preserve the original text | Leave the timing implicit or tell the learner to overwrite the first response |
| “Matching Information 是什么题型？” with no ongoing task | Borderline / usually no | Answer the concept directly unless continuing context clearly requires a practice page | Create an unwanted Notion page |
| “帮我写一封英文邮件给老师。” | No | Route to ordinary writing behavior | Trigger the learning loop or create a worksheet |

## Output review criteria

- Diagnosis quotes or points to learner evidence.
- Diagnosis distinguishes first response, reason, self-correction, and final answer when present.
- The next task targets the earliest broken conversion rather than repeating earlier correct steps.
- At most two bottlenecks are trained.
- The next page is created automatically when the next step is clear.
- Existing learner pages remain untouched.
- Every field uses exactly `【　　】`.
- The page contains material, timing, explicit operations, stop rules, completion record, and collapsed answers.
- Retrieval tests a method or transferable relationship, not memorized answer letters.
- Chinese worksheets explicitly load natural-chinese-writing for the final wording review.
- Every instruction passes the “look at what / do what / write what” test when read aloud.
- Completion and reflection fields have a concrete diagnostic use; blank generic reflections do not override the answer trace.
- Answer-checking pages state when to submit and where later corrections belong.
