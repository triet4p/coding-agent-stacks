# Authority Stack

## Archetype purpose

Use this archetype to explain hierarchical responsibility, semantic freedom, physical authority, and timescale separation.

---

## Primary example reference

`../examples/authority_timescale_stack.png`

---

## When to use this archetype

- when the main question is **who decides what**;
- when the architecture contains several abstraction layers;
- when control layers and semantic layers should be distinguished;
- when safety boundaries must be shown as cross-cutting constraints.

---

## Canonical figure claim

"Authority should narrow toward hardware, and timescale should generally accelerate toward lower layers."

---

## Information structure

- ordered layers from high-level orchestration to low-level hardware;
- authority interpretation for each layer;
- optional timescale annotations;
- cross-cutting safety band or boundary.

---

## Mandatory elements

- a clearly ordered stack;
- top semantic layer(s);
- bottom hardware / actuation layer;
- indication of what each layer is allowed to decide.

---

## Optional elements

- right-side annotations for timescale;
- safety / constraint column or band;
- side notes on failure or override behavior.

---

## Layout guidance

1. Choose one dominant reading direction.
2. Keep region boundaries explicit when groups matter.
3. Use muted semantic color coding from `../DESIGN.md`.
4. Keep node text compact and scan-friendly.
5. Include a legend if multiple edge or border semantics are used.

---

## Text guidance

- Prefer functional labels.
- Use secondary italic lines only when they add important nuance.
- Keep the title claim-oriented.
- Avoid overloading the figure with prose.

---

## Anti-patterns

1. mixing non-hierarchical flow with the stack;
2. omitting the meaning of authority;
3. using a stack when the content is actually a process or flywheel.

## Related files

- `../DESIGN.md`
- `../SKILL.md`

---

## Minimal production checklist

- [ ] Is this truly the correct archetype for the claim?
- [ ] Are the main structural elements present?
- [ ] Are semantic classes visually consistent with `../DESIGN.md`?
- [ ] Does the figure remain legible at document scale?
