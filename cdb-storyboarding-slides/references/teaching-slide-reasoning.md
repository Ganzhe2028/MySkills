# Teaching Slides: Reasoning Visibility and Pagination

Use this reference when a deck teaches a procedure, symbolic transformation, classification, worked example, or interactive check.

## Four-layer model

### Layer 0: Semantic representation

The visual representation must preserve the structure of the knowledge.

- Render fractions, radicals, matrices, exponents, and aligned equations with MathML, KaTeX, SVG, or an equivalent structural renderer.
- Do not ship raw LaTeX source or slash fractions when the two-dimensional structure carries meaning.
- Preserve accessible labels or semantic annotations.

### Layer 1: Visible inference

A teaching visual should externalize the reasoning the learner is expected to perform.

Use this trace for procedural examples:

```text
source state -> target object -> operation -> intermediate result -> decision rule -> conclusion
```

- Repeat enough of the source expression to preserve context.
- Highlight one target object at a time.
- Keep the target's visual identity stable across before and after states.
- Show the transformed result, not only a verbal description of the operation.
- Feedback must explain the causal link, not merely say correct or incorrect.

### Layer 2: Cognitive pagination

A slide boundary should follow one audience action, not the amount of available canvas.

Split rather than shrink when any of these are true:

- Two or more independent reasoning chains each need a full source-to-result trace.
- Equations or labels must be reduced below comfortable presentation size to fit.
- The audience must scan several dense columns before understanding any one case.
- Each card needs a source, highlighted target, operation, result, choices, and feedback.

Keep cases together only when comparison is itself the learning objective and each case has already been explained or is simple enough to read without a full derivation.

### Layer 3: Learning-mode integrity

Choose the mode before deciding when the answer appears.

| Mode | What appears first | When the solution appears | Primary purpose |
|---|---|---|---|
| Guided example | Full reasoning trace | Immediately | Imitation and explanation |
| Retrieval check | Prompt and necessary evidence | After the learner responds | Recall and diagnosis |
| Comparison | Multiple already-understood states | Together | Difference detection |

Never show the full answer and still label the slide a retrieval check.

For concept rehearsal, the initial state must leave the decisive mental action to the learner. Show the prompt and necessary evidence, but do not pre-compute the operation that determines the answer. An incorrect choice should receive a directional, non-revealing hint. Reveal the complete trace only after a correct response or an explicit request for the solution.

## Secondary design rules

1. **One highlight, one meaning.** Reuse a color only for the same tracked object or semantic role.
2. **Operation labels are verbs.** Use cancel, substitute, factor, compare, or isolate rather than vague labels such as step.
3. **Results are visual states.** Show the simplified expression, moved object, changed graph, or classified state.
4. **Feedback repeats the reason.** A correct response should reconnect target, operation, result, and conclusion.
5. **Pagination is a system change.** Updating slide count also requires page labels, progress denominator, deep links or hashes, speaker-note indices, print order, and end-of-deck navigation.
6. **Retrieval preserves productive struggle.** Keep the decisive step hidden until the learner acts; do not turn a simple check into answer recognition.

## Decision path

```text
Does notation encode structure?
  yes -> render it structurally

Does the learner need to reproduce a procedure?
  yes -> show or reveal the full reasoning trace

Are there multiple independent full traces on one slide?
  yes -> split one trace per slide
  no  -> keep together only if comparison is the message

Is the answer visible before the learner acts?
  yes -> call it guided, not retrieval
  no  -> reveal the reasoning after the response
```

## Verification

- Inspect the target presentation viewport, not only the source markup.
- Confirm equations are rendered and legible at presentation distance.
- Confirm every highlight has a unique semantic purpose.
- Confirm each slide has one main audience action.
- Confirm interactive feedback explains why.
- Confirm a retrieval slide does not expose the decisive operation or answer before the response.
- After pagination, verify slide count, progress, notes, navigation, deep links, and print order.
