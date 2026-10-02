# Frontier Curve

## Archetype purpose

Use this archetype to communicate a conceptual trade-off frontier, especially reliability vs coverage or selectivity vs abstention.

---

## Primary example reference

`../examples/specialist-first-routing.png`

---

## When to use this archetype

- when the main message is a trade-off;
- when a theoretical argument should be made visually intuitive;
- when comparing specialist, generalist, and routed systems in conceptual performance space.

---

## Canonical figure claim

"Selective routing can dominate single-policy extremes by improving the coverage–reliability envelope."

---

## Information structure

- axes with clear meaning;
- one or more curves or operating points;
- labeled regions or representative system types;
- optional inset explaining a key distinction such as semantic OOD vs metric residual.

---

## Mandatory elements

- explicit axes;
- at least two contrasted operating points or curves;
- a clear interpretive message, not merely geometry.

---

## Optional elements

- threshold sweeps;
- reject-option annotation;
- small inset showing semantic OOD ≠ metric residual.

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

1. unlabeled conceptual curves;
2. ambiguous axes;
3. implying measured data when only a conceptual frontier is intended.

## Related files

- `../DESIGN.md`
- `../SKILL.md`
- `../examples/specialist-first-routing.png`

---

## Minimal production checklist

- [ ] Is this truly the correct archetype for the claim?
- [ ] Are the main structural elements present?
- [ ] Are semantic classes visually consistent with `../DESIGN.md`?
- [ ] Does the figure remain legible at document scale?
