# Evaluation Matrix

## Archetype purpose

Use this archetype to define experimental structure, ablation logic, metric families, or reliability decomposition.

---

## Primary example reference

`../examples/evaluation-matrix.png`

---

## When to use this archetype

- when the figure explains how reliability is evaluated;
- when several system additions correspond to several metric groups;
- when experimental design is more important than a single numeric result.

---

## Canonical figure claim

"Reliability should be attributed to specific system additions and measured through multiple metric families."

---

## Information structure

- row/column structure;
- ablation progression or component additions;
- metric families;
- visual indication of dependencies or coverage;
- optional notes on expected findings.

---

## Mandatory elements

- a clearly labeled grid or matrix;
- dimensions that actually matter experimentally;
- readable grouping of rows and columns.

---

## Optional elements

- checkmarks, staged accumulation, or color cues;
- callouts for core metrics such as task reliability, routing, verification, transfer, and resource economics.

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

1. inventing quantitative results;
2. using the matrix as a decorative table;
3. unclear mapping between ablations and metrics.

## Related files

- `../DESIGN.md`
- `../SKILL.md`

---

## Minimal production checklist

- [ ] Is this truly the correct archetype for the claim?
- [ ] Are the main structural elements present?
- [ ] Are semantic classes visually consistent with `../DESIGN.md`?
- [ ] Does the figure remain legible at document scale?
