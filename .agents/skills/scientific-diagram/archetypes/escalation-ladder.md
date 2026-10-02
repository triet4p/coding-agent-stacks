# Escalation Ladder

## Archetype purpose

Use this archetype to show ordered interventions from cheapest / safest to most expensive / ambitious.

---

## Primary example reference

`../examples/improvement-ladder.png`

---

## When to use this archetype

- when the system should prefer low-cost fixes before high-cost retraining or research;
- when cost, time, risk, or required resources increase monotonically;
- when the key message is strategy under constraint.

---

## Canonical figure claim

"Expensive improvement is an escalation path, not the default first response."

---

## Information structure

- a monotonic ordered structure;
- a notion of increasing cost / risk / sophistication;
- each rung or step corresponding to an intervention;
- optional resource annotations.

---

## Mandatory elements

- clear direction of escalation;
- ordered steps;
- one or more side annotations indicating what increases upward or rightward.

---

## Optional elements

- cost icons or labels;
- human/GPU/robot-hour annotations;
- guardrail notes about promotion gates.

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

1. unordered lists disguised as ladders;
2. mixing incomparable step types without explanation;
3. unclear escalation direction.

## Related files

- `../DESIGN.md`
- `../SKILL.md`

---

## Minimal production checklist

- [ ] Is this truly the correct archetype for the claim?
- [ ] Are the main structural elements present?
- [ ] Are semantic classes visually consistent with `../DESIGN.md`?
- [ ] Does the figure remain legible at document scale?
