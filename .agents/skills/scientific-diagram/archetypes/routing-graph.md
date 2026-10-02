# Routing Graph

## Archetype purpose

Use this archetype to show conditional selection, gating, abstention, escalation, and fallback logic.

---

## Primary example reference

`../examples/specialist-first-routing.png`

---

## When to use this archetype

- when the system branches based on uncertainty or support;
- when different tools, skills, or sub-agents are selected conditionally;
- when the argument depends on separating semantic uncertainty from metric or physical uncertainty.

---

## Canonical figure claim

"Use the most reliable supported capability first, then abstain, repair, or escalate."

---

## Information structure

- one input state or decision context;
- one or more decision diamonds;
- branch annotations;
- resulting capability choices;
- convergence into execution;
- possible retry or belief-update loop.

---

## Mandatory elements

- a clear input state;
- at least one decision layer;
- explicit branch outcomes;
- convergence or terminal actions;
- optional abstain / safe fallback path when relevant.

---

## Optional elements

- uncertainty-axis inset;
- belief-update loop;
- calibration or confidence threshold annotation.

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

1. confusing routing with taxonomy;
2. burying branch logic in long text;
3. too many levels of branching without compression;
4. not making abstention or fallback explicit when needed.

## Related files

- `../DESIGN.md`
- `../SKILL.md`

---

## Minimal production checklist

- [ ] Is this truly the correct archetype for the claim?
- [ ] Are the main structural elements present?
- [ ] Are semantic classes visually consistent with `../DESIGN.md`?
- [ ] Does the figure remain legible at document scale?
