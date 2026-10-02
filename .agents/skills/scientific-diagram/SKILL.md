---
name: scientific-diagram
description: Create publication-quality scientific systems diagrams by identifying the figure's principal claim, selecting the appropriate diagram archetype, compressing source material into visual structure, applying a stable semantic visual grammar, and performing consistency and readability QA. Use for research-paper figures, systems architecture diagrams, robotics/ML diagrams, routing graphs, failure-recovery graphs, authority stacks, flywheels, strategic maps, escalation ladders, evaluation matrices, and conceptual frontier plots. Prefer functional architectural roles over paper/model names, preserve stable meanings for shapes, borders, colors, and arrow styles, and never invent quantitative results.
---

## Scientific Diagram Generation Skill

This document defines the **reasoning procedure** that turns source material into a coherent scientific figure using the grammar specified in `DESIGN.md`.

---

## 1. Purpose

The skill exists to answer **what to draw**, not only **how to style it**.

It performs five jobs:

1. infer the central claim of the figure,
2. choose the correct archetype,
3. compress source text into visual units,
4. map those units into layout and flow,
5. apply the visual grammar in `DESIGN.md` and run QA.

This is what prevents the system from producing pretty but conceptually weak diagrams.

---

## 2. Inputs

A scientific diagram request may provide any subset of:

- source prose,
- section headings,
- formulas or propositions,
- lists or tables,
- architectural descriptions,
- failure taxonomies,
- evaluation plans,
- example figures,
- role/status taxonomy,
- named implementation references.

The skill must infer missing structure where possible.

---

## 3. Outputs

The skill should produce:

1. **selected archetype**,
2. **figure claim / thesis**,
3. **node list and grouping**,
4. **flow semantics**,
5. **compressed text labels**,
6. **visual layout plan**,
7. **legend requirements**,
8. **QA result**.

---

## 4. Core workflow

### Step 1 — Identify the figure's principal claim

A figure is not a bag of facts. It should express one main statement.

Examples:

- "The system is a closed loop across three planes."  
- "Authority narrows toward hardware while timescale accelerates."  
- "Specialists should be chosen first; generalists are fallback under coverage failure."  
- "Failures should branch into immediate recovery and selective learning."  

If the source text contains many ideas, choose the one most visually central and push the rest to annotations or separate figures.

### Step 2 — Classify the problem type

Use the following mapping:

| Content type | Preferred archetype |
|---|---|
| Components + interfaces + planes | Architecture Map |
| Hierarchy + authority + timescale | Authority Stack |
| Conditional branching or gating | Routing Graph |
| Error classes + responses + longer-term handling | Failure-Recovery Graph |
| Closed-loop improvement process | Flywheel |
| Positioning components in conceptual space | Strategic Map |
| Ordered escalation by cost/risk/resources | Escalation Ladder |
| Ablations, metric families, experiment design | Evaluation Matrix |
| Coverage vs reliability trade-off | Frontier Curve |

### Step 3 — Extract semantic units

Turn the source text into a structured set of units:

- **actors / components**,
- **states / artifacts**,
- **decisions**,
- **flows**,
- **recovery paths**,
- **offline update paths**,
- **constraints / safety boundaries**,
- **optional accelerators**,
- **research-only extensions**.

### Step 4 — Compress language

Convert long prose into concise node text.

#### Compression rules

1. Prefer noun phrases to sentences.
2. Preserve the core distinction, not every explanatory clause.
3. Move nuance into subtitle, annotation, or legend.
4. Split long ideas into a primary label plus a secondary italic line.

#### Example

Long source:

> The capability router determines whether a specialist is applicable under the current uncertainty and otherwise escalates to either a generalist or a correction module.

Compressed representation:

```text
Supported specialist
and in-distribution?
```

branch notes:

```text
known + supported
→ specialist

semantic OOD
→ generalist

metric residual
→ geometry
```

### Step 5 — Assign semantic classes

Every extracted unit must be tagged as one of the semantic classes in `DESIGN.md`:

- Runtime Core,
- Learning Core,
- Optional / Accelerator,
- Research Option,
- Safety / Constraint,
- Evidence / Experience,
- Decision.

This step ensures that visual styling encodes meaning rather than ad hoc appearance.

### Step 6 — Compose the layout

Choose a single primary reading logic:

- left-to-right process,
- top-to-bottom stack,
- three-column transform,
- 2D map,
- ladder,
- matrix,
- curve.

Do not mix multiple layout logics unless the figure explicitly requires an inset or supporting panel.

### Step 7 — Add legend and optional inset

Include a legend when:

- multiple arrow types are used,
- multiple border semantics are used,
- optionality / maturity distinctions matter,
- an inset panel introduces additional analytic structure.

Add an inset only if it clarifies a concept that would otherwise clutter the main flow.

### Step 8 — QA and revision

Run the QA checklist in Section 10 before finalization.

---

## 5. Figure selection heuristics

### 5.1 Architecture Map

Use when the main question is:

- what are the parts,
- how are they grouped,
- how does information/action move between them,
- what closed loops exist.

### 5.2 Authority Stack

Use when the main distinction is **who gets to decide what**, often combined with **timescale** or **physical authority**.

### 5.3 Routing Graph

Use when the system should branch under conditions such as:

- in-distribution vs OOD,
- semantic uncertainty vs metric residual,
- specialist supported vs unsupported,
- escalate vs abstain.

### 5.4 Failure-Recovery Graph

Use when the core message is:

- not all failures are the same,
- failures should map to different immediate recoveries,
- some experiences should later feed learning.

### 5.5 Flywheel

Use when the focus is recurrent improvement across deployment, traces, data, and training.

### 5.6 Strategic Map

Use when conceptual positioning matters more than process flow. Suitable for:

- core vs frontier,
- necessity vs maturity,
- performance vs cost,
- reliability vs coverage.

### 5.7 Escalation Ladder

Use when the main claim is ordered intervention by increasing cost, risk, or sophistication.

### 5.8 Evaluation Matrix

Use when the figure defines what experiments should be run, what variables differ, or how multiple metric families align to multiple system layers.

### 5.9 Frontier Curve

Use when a trade-off frontier or selective-prediction intuition is the main message.

---

## 6. Role over paper name rule

Whenever source text contains concrete paper or model names, the skill should attempt to rewrite them as **role labels**.

Examples:

| Source instance | Preferred functional label |
|---|---|
| DexFLEX | Contact-aware Action Realization |
| TOPReward | Semantic Progress Critic |
| VLK | Synthetic Experience Factory |
| StressDream | Counterfactual Stress Testing |
| ENPIRE | Autonomous Improvement / Autoresearch |
| OpenVLA / RT-2 / VLA | Generalist Capability / VLA |

If preserving the original name is useful, place it secondarily as `-like` or `style` reference, not as the ontology-defining box name.

---

## 7. Semantic compression skill

### 7.1 Node-writing rules

A node should usually be one of:

- component name,
- state artifact,
- question / decision,
- recovery action,
- metric family,
- conceptual category.

### 7.2 Preferred grammar by node type

- **Component**: noun phrase (`Capability Router`)
- **Decision**: short question (`Supported specialist and in-distribution?`)
- **Recovery**: action phrase (`pose refine / local search / visual servo`)
- **Evidence**: artifact noun (`Structured Experience`)
- **Inset quadrant label**: category phrase (`Geometry / Servo zone`)

### 7.3 Length control

If a node exceeds three lines, consider one of the following:

1. Split into primary label + italic explanation.
2. Move the explanation to a branch annotation.
3. Split the concept into two nodes if the flow requires it.
4. Remove non-essential adjectives.

---

## 8. Prompt / rendering blueprint

If this skill is implemented for image generation, the internal structure should be described approximately in this order:

1. overall figure type and style,
2. title and subtitle,
3. overall regions or layout,
4. node contents in reading order,
5. arrows and branch semantics,
6. legend,
7. optional inset,
8. restrictions: no clutter, clean white background, paper-like style.

The style instructions should emphasize:

- scientific systems diagram,
- vector / infographic cleanliness,
- muted pastel panels,
- serif-like research-paper title,
- high text legibility,
- clear arrow semantics.

---

## 9. Failure modes of the skill

The skill should explicitly guard against the following failure modes:

1. **Topic dump** — too many concepts stuffed into one figure.
2. **Aesthetic drift** — style becomes business infographic, not scientific figure.
3. **Ontology collapse** — boxes become paper names instead of functional roles.
4. **Over-texting** — node text too long to scan.
5. **Weak claim** — figure shows objects but not a thesis.
6. **Arrow ambiguity** — multiple edge styles with no stable meaning.
7. **Core/optional confusion** — optional modules visually indistinguishable from runtime core.
8. **Unstable semantics across figures** — dashed means two different things in different figures.
9. **Invented numbers** — fake quantitative results added without evidence.

---

## 10. QA checklist

Before finalization, check all of the following:

### Claim and structure

- [ ] Is there a single principal claim?
- [ ] Is the title aligned with that claim?
- [ ] Is the chosen archetype the correct one?
- [ ] Is the primary reading path obvious?

### Semantics and abstraction

- [ ] Are architectural roles expressed as roles rather than paper names?
- [ ] Are optional / research modules visually distinguishable from core runtime logic?
- [ ] Is the difference between control flow, evidence flow, and learning flow explicit?
- [ ] If safety matters, is it represented as a boundary or distinct semantic class?

### Text quality

- [ ] Are nodes concise?
- [ ] Are long explanations moved to subtitle, annotation, or legend?
- [ ] Is text readable when scaled down?

### Layout quality

- [ ] Are crossings minimized?
- [ ] Are merges visually clean?
- [ ] Is spacing generous enough?
- [ ] Is the figure balanced?

### Integrity

- [ ] Are quantitative claims absent unless sourced?
- [ ] Are example names and references correct?
- [ ] Does the figure look like a coherent member of the same figure family?

---

## 11. Example grounding references

Use the following grounded examples as style anchors and archetype references:

- Architecture map: `./examples/unified-architecture.png`
- Authority stack: `./examples/authority_timescale_stack.png`
- Routing graph: `./examples/specialist-first-routing.png`
- Failure graph: `./examples/failure-recovery-learning.png`
- Flywheel: `./examples/data-economy.png`
- Strategic map: `./examples/research-option-map.png`
- Escalation ladder: `./examples/improvement-ladder.png`
- Evaluation matrix: `./examples/evaluation-matrix.png`

---

## 12. Operating maxim

The skill should always follow this maxim:

> **First discover the argument, then choose the archetype, then compress the content, then apply the design language.**

Anything that reverses this order risks producing a stylish diagram with weak scientific content.
