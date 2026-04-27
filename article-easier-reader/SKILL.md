---
name: article-easier-reader
description: Convert an English article, essay, PDF, or pasted text into a Markdown easier-reading study version. Use when the user asks for a simplified article, easier reading version, vocabulary simplification table, one-sentence core meaning, or a Chinese explanation of an abstract or jumpy essay's hidden thought line.
compatibility: opencode
---

# Article Easier Reader

## Purpose

Turn an English article or essay into one Markdown study document that helps a student read the piece without flattening its meaning.

The default output has four parts:
- an easier English version
- a simple vocabulary replacement table
- one sentence explaining the core meaning
- a Chinese explanation of the author's hidden thought line

This skill is especially useful for reflective, literary, or abstract nonfiction where the author moves between concrete examples, memories, ideas, science, religion, emotion, or metaphor.

## Use This Skill When

Use this skill when the user provides an article, essay, PDF, screenshot OCR, Markdown file, or pasted text and asks for one or more of:
- an easier reading version
- simplified English while keeping the original order
- vocabulary simplification
- a study version in Markdown
- a one-sentence core meaning
- a Chinese explanation of why the article feels jumpy, abstract, indirect, or hard to follow
- the author's thought line, hidden logic, or transition path

Do not use this skill for:
- literal translation
- formal literary criticism
- full academic analysis
- grammar correction only
- summarizing a paper's research methods or results

## Input Handling

Start from the source text itself.

If the input is a PDF or document:
- extract the full readable text before writing
- remove page numbers, repeated headers, footers, and line-break artifacts
- preserve the title, author, named people, key examples, and the original sequence of ideas

If the article is long:
- condense paragraph by paragraph instead of copying every sentence
- keep all major turns in the author's thinking
- do not invent connective logic that is not present in the source

If the source appears copyrighted or published:
- rewrite in fresh wording
- keep direct quotations short and only when necessary
- do not reproduce long passages verbatim

## Output Format

Always output Markdown in this structure:

```markdown
# {Article Title} — Easier Reading Version

> Based on {author/source if known}.  
> This version keeps the main ideas and order, but uses simpler words and shorter sentences.

---

## Easier Version

{Simplified article}

---

## Simple Vocabulary Replacements

| Original / harder word | Easier meaning |
| ---------------------- | -------------- |
| ... | ... |

---

## One-sentence Core Meaning

{One sentence}

---

## Extraction

{Chinese thought-line explanation}
```

Keep the section titles exactly as shown unless the user asks for another format.

## Easier Version Rules

Write the easier version in English.

Target a smart middle-school or early high-school reader:
- use shorter sentences
- replace difficult words with common words
- keep the tone natural, not childish
- keep the author's main ideas, order, examples, and emotional movement
- explain implied transitions when needed, but do not over-explain
- preserve important names, places, texts, and concepts
- avoid worksheet language such as "the author is trying to show" inside the rewritten article

The easier version should read like a real simplified essay, not a bullet summary.

For abstract essays:
- keep the concrete objects that carry the argument
- make each turn easier to follow
- show why the author moves from one idea to the next
- do not erase strangeness or ambiguity if it matters to the piece

## Vocabulary Table Rules

Choose words or phrases from the original article that would block understanding or carry important style.

Default length: 12 to 25 rows.

For each row:
- put the harder source word or phrase in the left column
- give a short, context-specific easier meaning in the right column
- prefer plain English definitions
- include a phrase when the phrase matters more than a single word
- do not include random common words just to fill the table

Good vocabulary definitions are short enough to scan while reading.

## One-Sentence Core Meaning Rules

Write one English sentence.

It should:
- name the author when known
- include the article's concrete surface topic
- include the deeper emotional or conceptual turn
- avoid vague thesis language

Pattern:

```text
{Author} says {surface topic} may seem {simple/common problem}, but {deeper point}.
```

## Chinese Extraction Rules

The Chinese section should follow this intent:

> 帮我解释这篇文章为什么读起来有点跳跃和抽象。不要写正式分析，也不要急着总结主题。请像朋友解释给朋友一样，帮我还原作者的思路暗线：他从什么想到什么，为什么会突然转到另一个东西，最突兀的跳转有什么作用。把抽象概念翻译成具体好懂的话，最后给我一条读这篇文章时可以抓住的线。中文回答，口语化，初中生能懂，但理解深度接近高中阅读讨论。

Write this section in Chinese.

Tone:
- conversational
- clear
- not formal
- not lecture-like
- not literary-critic style
- easy enough for a middle-school student, but with real reading depth

Default shape:
1. Start with what the article is roughly doing, in plain Chinese.
2. Walk through the author's thought path in order.
3. Explain why each major jump happens.
4. Name the most abrupt jump and explain what it does.
5. Translate abstract ideas into concrete everyday language.
6. End with one line the reader can hold onto while reading.

Useful Chinese openings:
- `这篇文章大概是在讲：`
- `它读起来跳，是因为作者不是按“观点-论据-结论”在写，而是在顺着一个念头往下想。`
- `最突兀的一跳是这里：`
- `读这篇文章时可以抓住这条线：`

Avoid:
- `本文通过...揭示了...`
- `综上所述`
- `作者旨在表达`
- long thesis-first analysis
- heavy terms without concrete explanation

## Quality Check

Before finishing, check that:
- the output is one Markdown document
- the four required sections appear in order
- the easier English version keeps the source's main order
- the vocabulary table uses words from the source
- the core meaning is exactly one sentence
- the Chinese section explains the thought line, not just the theme
- the most abrupt transition is identified when the essay has one
- the final Chinese line gives the reader a usable reading thread
- no long source passage is copied verbatim

## Decision Rule

Optimize for:
- easier reading without dumbing down
- faithful order over clever restructuring
- concrete explanation over abstract analysis
- student usefulness over polished literary commentary
