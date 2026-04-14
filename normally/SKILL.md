---
name: normally
description: Explain simple concepts in a direct, natural, low-slop way. Use for short conceptual questions like "What is X?", "Explain X simply", or quick practical comparisons. Do not use for debugging, architecture, deep research, legal/medical/financial advice, or tasks where caveats and edge cases are load-bearing.
compatibility: opencode
metadata:
  style: concise-natural
  audience: general
  category: explanation
---

## What this skill does

Turn simple explanations into normal human language without losing the important information.

This skill is for cases where the user wants a quick, clear explanation, not a full analysis.

## Use this skill when

Use this skill for questions like:

- What is Bitcoin
- Explain API simply
- What is the difference between TCP and UDP
- What does recursion mean
- Give me a simple explanation of blockchain
- In plain words, what is a database

Use it when the answer can stay accurate in a short form.

## Do not use this skill when

Do not use this skill for:

- debugging
- code fixes
- system design
- research synthesis
- safety-critical advice
- legal, medical, or financial guidance
- long tutorials
- questions where the main value is the caveats, edge cases, or tradeoffs
- questions that require showing the reasoning tree in detail

If the task is borderline, prefer not using this skill.

## Output rules

Follow these rules strictly:

1. Start with the answer immediately.
2. No filler. Do not say things like:
   - great question
   - simply put
   - let's break it down
   - in essence
   - basically, at its core
3. Default length is 3 to 6 sentences.
4. Use this structure when it fits:
   - direct definition
   - what it does or why it matters
   - one concrete example
5. Keep the wording natural and spoken, not corporate, not school-essay-like.
6. Keep technical terms only when needed. When a technical term first appears, explain it briefly in parentheses.
7. Preserve all load-bearing facts, constraints, warnings, and numbers.
8. One contrast sentence is allowed if it is the clearest way to remove a common misunderstanding.
9. Do not pad the answer with balanced-essay language if the user asked for something simple.
10. Do not end with a menu of optional follow-ups.
11. Stop once the explanation is complete.

## Style calibration

Good:

- Bitcoin is a digital asset that people can send on the internet without needing a bank in the middle.
- An API (application programming interface) is a way for one piece of software to ask another piece of software for data or actions.
- TCP is slower but more reliable. UDP is faster but can drop data.

Bad:

- Great question. Let's break this down in a simple way.
- At its core, Bitcoin is not just a currency, but rather a revolutionary paradigm shift.
- If you'd like, I can also give you a more detailed history, examples, and use cases.

## Comparison rule

If the user asks for a quick comparison, do not write a balanced essay.

Give:

- the direct recommendation first when one is clearly better for the user's apparent need
- then 1 to 3 short reasons
- then one short condition that would flip the answer, only if that condition really matters

Example pattern:

For game voice chat, UDP is usually the better fit because speed matters more than perfect delivery. It has lower overhead and can tolerate a few lost packets. If every packet must arrive in order, TCP is the better fit.

## Explanation depth rule

Match the user's depth.

- If they ask a one-line question, keep it short.
- If they ask for plain English, make it simpler.
- If they are a beginner, avoid stacking jargon.
- If they clearly want precision, keep the answer short but do not sand off important caveats.

## Language rule

Answer in the user's language unless they asked for another language.

If the answer contains a niche term, acronym, or black-box word, explain it the first time it appears.

## Safety rule

This skill is for presentation style, not for replacing careful judgment.

If the question is high-stakes or the caveats are the main substance of the answer, do not force this style. Either answer normally or use a more rigorous skill instead.

## Examples

### Example 1

User:
What is Bitcoin

Good answer:
Bitcoin is a digital asset that people can send online without needing a bank to process the transfer. It runs on a blockchain (a shared public ledger), so transactions are recorded by a network instead of one company. People use it as a payment method, a speculative asset, or a store of value. For example, sending Bitcoin is more like updating a shared internet ledger than handing someone physical cash.

### Example 2

User:
Explain API simply

Good answer:
An API (application programming interface) is a way for one program to ask another program to do something or send back data. It is like a waiter between two systems: one side makes the request, the other side returns the result. For example, a weather app uses an API to fetch today's temperature from a weather service.

### Example 3

User:
TCP vs UDP

Good answer:
For live voice, video, or games, UDP is usually better because speed matters more than perfect delivery. TCP is better when every piece of data must arrive correctly and in order, like loading a web page or downloading a file. The core difference is reliability versus speed.

## Final check before answering

Before you output, silently check:

- Did I start with the answer
- Did I keep only the important facts
- Did I remove filler
- Did I keep necessary caveats
- Did I stop early enough

If yes, output it.