# Architecture Map

## Archetype purpose

Use this archetype to depict a system as a structured composition of planes, modules, interfaces, and closed loops.

---

## Primary example reference

`../examples/unified-architecture.png`

---

## When to use this archetype

- when the content is mainly about **what components exist** and **how they interact**;
- when the reader needs to understand the overall system boundary;
- when offline learning, runtime execution, and memory or evaluation layers must be shown together.

---

## Canonical figure claim

"This system is a coherent architecture, not a loose collection of components."

---

## Information structure

- high-level input or goal;
- major regions or planes;
- primary execution path;
- evidence / verification loop;
- memory / experience output;
- offline improvement or update path;
- optional modules clearly marked as optional.

---

## Mandatory elements

- clearly named regions or planes;
- a visible main runtime path;
- at least one closed feedback loop if the system is iterative;
- distinction between runtime, learning, and offline activity;
- boundary or indication of safety if relevant.

---

## Optional elements

- implementation examples as subordinate notes;
- secondary verifiers or critics;
- optional inset explaining one key distinction;
- example status tags such as core / optional / research.

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

1. dumping every subsystem of the codebase into the figure;
2. treating papers or model names as the architecture itself;
3. failing to distinguish runtime vs offline flows;
4. hiding the closed loop.

## Related files

- `../DESIGN.md`
- `../SKILL.md`

---

## Minimal production checklist

- [ ] Is this truly the correct archetype for the claim?
- [ ] Are the main structural elements present?
- [ ] Are semantic classes visually consistent with `../DESIGN.md`?
- [ ] Does the figure remain legible at document scale?
