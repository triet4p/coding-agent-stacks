# Failure-Recovery Graph

## Archetype purpose

Use this archetype to show that failures should be classified, responded to differently in the short term, and selectively fed into learning in the long term.

---

## Primary example reference

`../examples/failure-recovery-learning.png`

---

## When to use this archetype

- when failures come in multiple kinds;
- when immediate recovery and longer-term adaptation are distinct;
- when the system converts runtime failure into structured experience.

---

## Canonical figure claim

"Not all failures deserve the same response; classify now, recover safely, and learn selectively."

---

## Information structure

- failure-detection entry point;
- failure taxonomy column;
- corresponding recovery column;
- structured experience node;
- decision for whether an event is recurrent or valuable;
- learning or retrieval outcomes;
- offline improvement pipeline if justified.

---

## Mandatory elements

- at least one explicit failure taxonomy;
- differentiated recoveries;
- structured experience artifact;
- distinction between immediate recovery and longer-term learning.

---

## Optional elements

- feedback arrow showing improved future robustness;
- learning-core boxes such as retrieval and calibration;
- offline retraining / new capability pipeline.

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

1. treating all failures as "retry";
2. collapsing recovery and learning into one stage;
3. omitting the value-selection decision.

## Related files

- `../DESIGN.md`
- `../SKILL.md`

---

## Minimal production checklist

- [ ] Is this truly the correct archetype for the claim?
- [ ] Are the main structural elements present?
- [ ] Are semantic classes visually consistent with `../DESIGN.md`?
- [ ] Does the figure remain legible at document scale?
