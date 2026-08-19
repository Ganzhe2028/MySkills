---
name: cdb-typography
description: Improve typography using CDB Text principles (text as symbolic shape, font choice, hierarchy, readability, alignment, Chinese-English mixed text, poster or slide text organization). Also covers practical typography fixes — font selection, type scales, weight strategy, readability tuning, and refinement. Use when the user mentions fonts, type, readability, text hierarchy, sizing looks off, or wants more intentional typography.
---

# CDB Typography

Use this skill when text is a design material, not just content. CDB treats text as simplified and symbolic shapes — typography must make information readable, recognizable, and appropriately expressive.

## Core Workflow (CDB)

1. Define reading order: what should be read first, second, and last?
2. Assign type roles: title, subtitle, body, label, annotation
3. Check font fit: language support, reading length, tone, output medium
4. Build hierarchy through size, weight, spacing, color, and alignment
5. For Chinese/English mixed text, check visual weight, line height, baseline feel, punctuation, and number treatment
6. Remove fake hierarchy that relies only on random bolding or oversized text

## Practical Assessment

Analyze what's weak or generic about the current type:

1. **Font choices**: Using invisible defaults? (Inter, Roboto, Arial, system defaults). Does the font match brand personality? Too many families? (More than 2-3 is a mess)
2. **Hierarchy**: Can you tell headings from body from captions at a glance? Are font sizes too close together? (14px, 15px, 16px = muddy). Are weight contrasts strong enough?
3. **Sizing & scale**: Is there a consistent type scale? Body text at least 16px? Appropriate sizing strategy for context? (Fixed `rem` for app UIs; fluid `clamp()` for marketing headings)
4. **Readability**: Line lengths 45-75 characters? Appropriate line-height? Enough contrast?
5. **Consistency**: Same elements styled the same way? Weights used consistently? Letter-spacing intentional?

## Practical Implementation

### Font Selection

- Choose fonts that reflect brand personality
- Pair with genuine contrast (serif + sans, geometric + humanist) — or use a single family in multiple weights
- Ensure web font loading doesn't cause layout shift (`font-display: swap`, metric-matched fallbacks)

### Establish Hierarchy

- **5 sizes cover most needs**: caption, secondary, body, subheading, heading
- **Use a consistent ratio** between levels (1.25, 1.333, or 1.5)
- **Combine dimensions**: Size + weight + color + space for strong hierarchy — don't rely on size alone
- **App UIs**: Use fixed `rem`-based type scale, optionally adjusted at 1-2 breakpoints
- **Marketing / content pages**: Use fluid sizing via `clamp(min, preferred, max)` for headings; keep body text fixed

### Fix Readability

- Set `max-width` on text containers using `ch` units (`max-width: 65ch`)
- Adjust line-height: tighter for headings (1.1-1.2), looser for body (1.5-1.7)
- Increase line-height slightly for light-on-dark text
- Body text at least 16px / 1rem

### Refine Details

- Use `tabular-nums` for data tables and aligned numbers
- Apply proper `letter-spacing`: slightly open for small caps and uppercase, default or tight for large display text
- Use semantic token names (`--text-body`, `--text-heading`), not value names (`--font-16`)
- Set `font-kerning: normal` and consider OpenType features where appropriate

### Weight Strategy

- Define clear roles for each weight and stick to them
- Don't use more than 3-4 weights (Regular, Medium, Semibold, Bold is plenty)
- Load only the weights you actually use

## Output Format (CDB)

```markdown
## Type Diagnosis
- Reading order:
- Main problem:
- Output context:

## Type System
- Title:
- Subtitle:
- Body:
- Label:
- Annotation:

## Fixes
1. ...
```

## Verify

- **Hierarchy**: Can you identify heading vs body vs caption instantly?
- **Readability**: Is body text comfortable to read in long passages?
- **Consistency**: Are same-role elements styled identically?
- **Personality**: Does the typography reflect the brand?
- **Performance**: Are web fonts loading efficiently without layout shift?
- **Accessibility**: Does text meet WCAG contrast ratios? Zoomable to 200%?

**NEVER**:
- Use more than 2-3 font families
- Pick sizes arbitrarily — commit to a scale
- Set body text below 16px
- Use decorative/display fonts for body text
- Disable browser zoom (`user-scalable=no`)
- Use `px` for font sizes — use `rem`
- Default to Inter/Roboto/Open Sans when personality matters
- Pair fonts that are similar but not identical
- Choose fonts only because they look interesting
- Make all text the same size or weight
- Use fake bold or fake italic when it damages glyph quality
- Ignore alignment when text becomes part of layout

## Sources

Read `references/cdb-source-map.md` for source PDFs and pages.
