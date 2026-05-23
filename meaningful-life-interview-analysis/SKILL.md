---
name: meaningful-life-interview-analysis
description: Analyze qualitative interview transcripts for meaningful-life projects. Use when the user asks to code interviews, find cross-interview patterns, apply Baumeister PVEW or Marcia identity status, fill pattern/evidence tables, or compare groups around AI, learning, self-worth, purpose, values, efficacy, or identity exploration.
compatibility: opencode
---

# Meaningful Life Interview Analysis

Use this skill for school or research-style interview analysis where the job is to move from raw transcript evidence to defensible patterns.

Treat this as academic qualitative analysis, not ordinary summarization. When the user frames the work as research, PA, school assessment, teacher-supervised work, or high-stakes academic writing, every cross-interview claim must survive an explicit evidence audit before it appears in the final table.

The default framework is:

- Baumeister: Purpose, Value / Values, Efficacy, Self-Worth
- Marcia: Crisis / Exploration, Commitment, Moratorium, Achievement, Foreclosure, Diffusion

Read `references/coding-guide.md` before coding if the task mentions PVEW, Marcia, identity status, meaning, learning meaning, AI anxiety, self-worth, or evidence tables.

## Use This Skill When

Use this skill when the user asks for any of these:

- analyze interview transcripts or notes
- code interviewee answers
- find repeated patterns across interviewees
- fill a pattern recognition + evidence table
- fill a compare and contrast table
- apply PVEW, Baumeister, Marcia, identity status, crisis, commitment, moratorium, or achievement
- turn interview evidence into presentation findings
- analyze how people make meaning in relation to AI, learning, work, ability, self-worth, values, or future identity

## Do Not Use This Skill When

Do not use this skill for:

- simple rewriting or polishing
- generic summary of one short text
- designing interview questions only
- making a PPT from already-finished findings without needing evidence analysis
- coding that does not involve interviews, reflective evidence, or meaning/identity questions

If the user explicitly says not to begin analysis yet, stop after reading the task, mapping the requirements, and confirming what the future analysis should produce.

## Core Rules

0. Run the academic rigor gate before writing final claims.
   No final pattern may be written until the exact claim has a support audit over all distinct interviewees: Present / Weak-partial / Absent. The support count must come from that audit, not from how many examples are convenient to cite.

1. Start from interviewee evidence, not theory labels.
   The theory explains the evidence after the evidence is understood.

2. Use only the interviewee's own words as evidence.
   Do not treat interviewer prompts, interviewer summaries, leading questions, or AI-generated task notes as evidence.

3. Preserve speaker context.
   If one interviewee has multiple transcript files, treat those files as one person unless the source clearly says otherwise.

4. Do not force every quote into a code.
   Code only material that helps explain meaning, value, ability, self-worth, identity, AI role, or learning.

5. One quote may support multiple codes.
   However, final tables should use the code that best supports the pattern being argued.

6. A pattern must cross people.
   A finding usually needs evidence from at least two interviewees. If only one person supports it, call it an individual insight, not a pattern.

7. Write patterns as full claims.
   Do not write labels like "creativity" or "AI dependency." Do not use vague quantity words such as "several," "many," "some," "most," "all," "both," "the group," "很多," "一些," "多数," "大部分," "都," or "全部" as prevalence claims unless they are paired with an exact count. Write claims with the specific number and denominator, such as: "4 of 6 interviewees believe creativity remains valuable because AI output feels useful but less personally meaningful." In group comparison tables, write "2 of 2 members in this group..." instead of "they all..." or "both..."

8. Count before claiming.
   Every final pattern must state exactly how many interviewees substantively support the exact claim, using "N of total interviewees" or an equivalent clear count. Count distinct interviewees, not evidence bullets. Do not mechanically turn the number of cited examples into the support count. If a table only shows a subset of evidence, still verify all counted interviewees first and either name them compactly or write that the row shows selected evidence.

8a. Replace vague prevalence language everywhere in final outputs.
    This applies beyond the pattern column. Evidence summaries, compare/contrast tables, conclusions, and presentation-ready bullets should use exact counts when making claims about how many interviewees or group members share a view. Pronouns like "they" are acceptable only for normal grammar after the exact counted group has already been named in the same sentence, not as a substitute for the count.

8b. Separate count, displayed evidence, and selected evidence.
    If the claim says "6 of 6 interviewees," the agent must have verified all 6. The evidence cell should either name all 6 compactly or include a support audit nearby. Never make the count equal to the number of examples shown unless that is also the verified support count.

8c. Do not use absence by omission.
    If a pattern excludes one or more interviewees, state whether each excluded case is Weak / partial or Absent. Do not leave the reader to infer that omitted interviewees did not mention the theme.

9. Keep claims proportional to evidence.
   If evidence is mixed, uncertain, or weak, say so. Do not inflate a clean story for the table.

10. Build compare/contrast groups from evidence.
   Use group traits that appear in the material, such as AI-heavy vs AI-cautious, internal self-worth vs external recognition, or settled commitment vs ongoing exploration. Do not invent demographic traits.

11. Keep the final answer usable for school presentation.
    Prefer clear, compact findings with direct evidence over dense theory prose.

## Workflow

### 1. Understand the Task and Sources

Identify:

- the required output table or document
- the interview files
- the task rubric or guidance
- whether the user wants analysis, table completion, presentation findings, or only task understanding

If a table template is provided, preserve its structure unless the user asks for a different format.

### 2. Read Once for Meaning

Read the full transcript set once before final coding.

For each interviewee, build a short working profile:

- central attitude toward AI / learning / work / meaning
- main source of purpose or value
- main source of efficacy
- main source of self-worth
- identity status signals
- memorable evidence anchors

This profile is a working aid, not automatically the final output.

### 3. Extract Evidence

Extract only useful interviewee statements.

For each evidence item, keep:

- interviewee name
- short quote or close paraphrase
- context if needed
- possible codes
- why it matters

Prefer exact wording when it carries meaning. Use paraphrase when the transcript is long, repetitive, or hard to quote cleanly.

### 4. Code the Evidence

Use the coding guide to assign codes.

Common code families:

- PVEW: Purpose, Value, Efficacy, Self-Worth
- Marcia: Crisis / Exploration, Commitment, Moratorium, Achievement, Foreclosure, Diffusion
- AI role: AI as tool, partner, teacher, executor, threat
- Learning meaning: thinking, creativity, expression, real experience
- Risks: dependency, loss of basic skills, hallucination, flattery, loss of real-world connection
- Human value: agency, connection, emotional understanding, creativity, judgment

Do not over-code filler, interviewer explanations, or repeated agreement.

### 5. Find Cross-Interview Patterns

Cluster evidence by repeated code and repeated meaning.

A good pattern usually has:

- evidence from two or more interviewees
- an exact support count, such as "3 of 6 interviewees"
- a clear claim
- a useful contrast or tension
- enough detail to support presentation narration

Before finalizing a count, make a quick support audit:

- Present: the interviewee directly supports this exact pattern; count them
- Weak / partial: the interviewee is related but does not support the full claim; do not count them unless the claim is narrowed or broadened honestly
- Absent: no usable interviewee evidence; do not count them

Record the audit in the working notes or final output whenever the user is challenging rigor, the table will be assessed academically, or any count is less than the total number of interviewees.

Weak pattern:

- "People think AI is useful."

Better pattern:

- "4 of 6 interviewees treat AI as a useful executor, but they still reserve judgment, responsibility, or emotional meaning for humans."

### 6. Fill Pattern + Evidence Table

Default columns:

| Patterns recognized, please write complete sentences | Evidence, make sure you use empirical evidence from your interview notes |
| --- | --- |

For each row:

- write one complete pattern claim with the exact number of supporting interviewees
- include at least two evidence points when possible
- name the interviewee for each evidence point
- keep evidence concrete enough that the reader can see where the claim came from
- make the number in the pattern match the verified support audit, not just the number of examples shown
- if the evidence cell cannot include every supporting interviewee, explicitly say the evidence is selected and avoid implying unverified support
- replace group-level wording such as "many interviewees," "some students," "they all," "both," or "大部分人" with exact counts
- when a pattern excludes someone, include the excluded count and reason in an audit note, e.g. "1 of 6 not counted / weak: George has agency evidence but not direct self-worth evidence"

### 7. Fill Compare and Contrast Table

Default columns:

| Group | Group traits | Questions / claim you want to compare | Similarities among groups | Differences for each group | Conclusion after comparison |
| --- | --- | --- | --- | --- | --- |

Choose groups based on the strongest split in the evidence. Typical grouping options:

- AI-heavy users vs AI-cautious users
- people with internal self-worth vs people relying more on external recognition
- people in identity achievement vs people in moratorium
- people who see learning as skill utility vs people who see learning as human formation

Use one comparison question across all groups. Examples:

- How do different groups decide what is still worth learning in the AI era?
- How do different groups confirm their self-worth when external outcomes are uncertain?
- How do different groups define what humans should not outsource to AI?

### 8. Final Quality Check

Before delivery, verify:

- every pattern is a complete sentence with a specific support count
- every pattern has evidence from interviewees
- every pattern's count matches a distinct-interviewee support audit
- weak or absent cases are excluded from the count or explicitly marked
- all prevalence claims in compare/contrast and summaries use exact counts, not vague words
- evidence is not taken from interviewer prompts
- theory labels match the actual quote
- compare/contrast groups are based on real evidence
- claims are not stronger than the support
- the output is ready to paste into the user's table

For academic work, add this semantic check:

- the count was not copied from the number of evidence bullets
- every counted interviewee has at least one directly relevant statement
- every uncounted interviewee is labeled Weak / partial or Absent
- broad pattern wording has not been stretched to count weak evidence
- narrow pattern wording has not accidentally excluded valid evidence
- final wording distinguishes "evidence shown" from "support count"
- no prevalence phrase remains without a number and denominator

## Known Failure Modes

- Mechanical count replacement: changing "many interviewees" into "4 of 6" because the row currently cites 4 people. This is wrong unless the all-interviewee support audit also says exactly 4 are Present.
- Evidence-display bias: citing only the strongest examples and then treating omitted interviewees as absent. If evidence is selected, say it is selected or add a support audit.
- Over-broad theory language: words like "self-worth," "identity," or "creativity" can become too elastic. Define the exact claim first, then count only direct support.
- Silent weak cases: when an interviewee is related to the topic but not the full claim, mark Weak / partial instead of counting them.
- Syntactic-only verification: skill validators and grep checks are not enough. Academic work needs semantic verification of claim, count, evidence, and exclusions.

## Output Style

Match the user's language. For Chinese school work, write natural Chinese and keep theory terms in English where useful.

Use concise table-ready wording. Avoid abstract filler such as:

- "This shows the complexity of modern society."
- "The interviewees all have different thoughts."
- "AI has both advantages and disadvantages."

Prefer evidence-backed statements:

- "2 of 6 interviewees draw a clear contrast between AI efficiency and human judgment: George treats AI mainly as a tool for efficiency, while Jacqueline is more concerned that relying on it may weaken personal judgment."

## Skill Test Prompts

Use these prompts to check trigger accuracy:

1. `读这些访谈 txt，按 PVEW 和 Marcia 找出 pattern，填 tables to be finish.md。`
   Expected: trigger this skill; code evidence and fill both tables.

2. `帮我从这几份采访里找出 AI 时代学习意义的共同模式。`
   Expected: trigger this skill; produce cross-interview patterns with evidence.

3. `只润色一下这段中文，让它更自然。`
   Expected: do not trigger this skill.

4. `根据这些采访做 PPT storyboard。`
   Expected: trigger only if pattern/evidence analysis is still needed; otherwise use a presentation or writing workflow.
