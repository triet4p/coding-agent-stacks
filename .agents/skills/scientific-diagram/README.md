# Scientific Systems Diagram Language

A reusable design system for **scientific / systems / ML / robotics diagrams**.

This package contains two complementary layers:

- **`DESIGN.md`** — the canonical visual grammar.
- **`SKILL.md`** — the reasoning procedure that decides *what figure to make*, *how to compress content*, *which archetype to choose*, and *how to apply the visual grammar consistently*.

It also includes a library of figure archetypes and a set of grounded example references.

---

## Directory structure

```text
scientific-diagram/
├── README.md
├── DESIGN.md
├── SKILL.md
├── archetypes/
│   ├── architecture-map.md
│   ├── authority-stack.md
│   ├── routing-graph.md
│   ├── failure-recovery-graph.md
│   ├── flywheel.md
│   ├── strategic-map.md
│   ├── escalation-ladder.md
│   ├── evaluation-matrix.md
│   └── frontier-curve.md
└── examples/
    ├── README.md
    ├── unified-architecture.png
    ├── authority_timescale_stack.png
    ├── specialist-first-routing.png
    ├── failure-recovery-learning.png
    ├── data-economy.png
    ├── research-option-map.png
    ├── improvement-ladder.png
    └── evaluation-matrix.png
```

---

## Core idea

This visual language is intended for diagrams that behave like **paper figures**, not decorative marketing illustrations.

The central principles are:

1. **Meaning before decoration.** Every shape, border, and arrow style should mean something.
2. **One figure = one principal claim.** A figure can support a section, but it should not attempt to summarize an entire document.
3. **Stable semantics across figures.** A dashed box must mean the same thing everywhere.
4. **Architectural roles over implementation instances.** Prefer `Action Realization` over `DexFLEX`, `Semantic Critic` over `TOPReward`, etc.
5. **Readable at paper scale.** The figure must still work when embedded in a PDF or slide deck.

---

## Recommended reading order

1. Read **`DESIGN.md`** for the visual grammar.
2. Read **`SKILL.md`** for the generation and reasoning procedure.
3. Use the relevant file under **`archetypes/`** for the specific figure type.
4. Consult **`examples/README.md`** and the example images for reference grounding.

---

## Quick map from problem type to archetype

| If the content is mainly about... | Use this archetype |
|---|---|
| System composition, planes, interfaces | `archetypes/architecture-map.md` |
| Authority hierarchy, responsibility, timescale | `archetypes/authority-stack.md` |
| Conditional selection, routing, escalation | `archetypes/routing-graph.md` |
| Failure modes and their responses | `archetypes/failure-recovery-graph.md` |
| Closed-loop improvement over experience | `archetypes/flywheel.md` |
| Positioning components in a conceptual space | `archetypes/strategic-map.md` |
| Ordered improvement by cost/risk | `archetypes/escalation-ladder.md` |
| Evaluation logic, ablation structure, metric families | `archetypes/evaluation-matrix.md` |
| Coverage vs reliability trade-off | `archetypes/frontier-curve.md` |

---

## Example references

The package is grounded by the following example images:

- `./examples/unified-architecture.png`
- `./examples/authority_timescale_stack.png`
- `./examples/specialist-first-routing.png`
- `./examples/failure-recovery-learning.png`
- `./examples/data-economy.png`
- `./examples/research-option-map.png`
- `./examples/improvement-ladder.png`
- `./examples/evaluation-matrix.png`

These example filenames are stable and intended for relative references from the documentation.
