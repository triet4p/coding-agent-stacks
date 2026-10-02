# DESIGN.md

## Scientific Systems Diagram Language

Canonical visual specification for research-style diagrams.

---

## 1. Purpose

This document defines the **visual grammar** for a family of scientific diagrams used in systems, robotics, ML, and agentic-architecture writing.

Its job is to answer:

- What visual treatment corresponds to what semantic role?
- How should typography, layout, flow, and optionality be represented?
- How do multiple figures remain visually consistent across one document?

This document deliberately focuses on **design semantics** rather than content generation logic. Content selection, abstraction, and figure-type choice belong to `SKILL.md`.

---

## 2. Design philosophy

### 2.1 Meaning before decoration

No visual attribute should be used only because it looks attractive. Borders, fills, arrow types, line weight, and panel grouping must encode structure.

### 2.2 Low-ornament academic clarity

The target visual identity is closer to a strong ML systems paper or architecture figure than to a business infographic or product brochure.

Avoid:

- glossy gradients,
- photorealistic robot renders,
- excessive iconography,
- oversaturated palettes,
- playful or comic styling,
- visually dense dashboards.

Prefer:

- clear regions,
- consistent shape language,
- compact text,
- muted colors,
- orthogonal flow,
- restrained hierarchy.

### 2.3 Stable cross-figure semantics

A reader should learn the grammar once and then recognize it throughout the full document.

If `Runtime Core` is pale blue with solid outline in Figure 1, it should remain so in Figures 2–8 unless there is a compelling reason to override it.

---

## 3. Semantic visual encoding

### 3.1 Core semantic classes

| Semantic class | Meaning | Recommended visual encoding |
|---|---|---|
| Runtime Core | On-path runtime operational component | Pale blue fill, solid dark navy outline |
| Learning Core | Memory, retrieval, calibration, persistent adaptation | Pale green fill, double outline |
| Accelerator / Optional | High-value but non-essential module | White or very light fill, dashed outline |
| Research Option / Frontier | Experimental or maturity-limited capability | White or light fill, dotted outline |
| Safety / Constraint | Boundary, interlock, forbidden region, hard limit | Very light red/pink fill, red outline |
| Offline Improvement Region | Post-hoc or offline training/evaluation area | Pale beige / sand / warm off-white region |
| Analysis Inset | Supplemental conceptual panel | Pale green or pale neutral panel with its own border |
| Decision | Branching logical condition | Diamond |
| Evidence / data artifact | Verification evidence, structured experience | Neutral or lightly tinted box distinct from control nodes |

### 3.2 Shape semantics

| Shape | Default meaning |
|---|---|
| Rounded rectangle | Component, module, stateful stage |
| Double-outline rounded rectangle | Learning-core / memory-core component |
| Dashed rounded rectangle | Optional / accelerator component |
| Dotted rounded rectangle | Research / frontier component |
| Diamond | Decision, branching condition |
| Large rounded panel / region | Grouping or plane |
| Inset panel | Secondary analytic explanation |

### 3.3 Arrow semantics

| Arrow style | Meaning |
|---|---|
| Solid black arrow | Main control / action / causally primary flow |
| Solid gray arrow | Information / evidence / state-flow |
| Dashed gray or navy arrow | Offline update / learning / feedback-to-future |
| Boundary enclosure / band | Safety, authority, or protected region |

These meanings must be preserved across all figures.

---

## 4. Color language

### 4.1 Palette behavior

Use a **muted paper palette**. Colors should differentiate semantic categories without dominating the figure.

Recommended families:

- **Runtime**: light blue / powder blue.
- **Learning**: light green / sage mint.
- **Offline improvement**: warm beige / pale sand.
- **Safety**: pale red / rose tint.
- **Research frontier**: largely neutral, distinguished more by border treatment than fill.

### 4.2 Color usage rules

1. Fill colors should be light enough to keep text readable.
2. Border color should carry more semantic weight than fill saturation.
3. Do not use strong colors merely to make the figure "pop".
4. Different shades inside one semantic family are acceptable only for grouping, not to redefine meaning.
5. If color printing is unavailable, semantics should still remain legible from border and line style.

---

## 5. Typography

### 5.1 Typographic hierarchy

Use a consistent hierarchy:

1. **Figure title** — large, prominent, serif-like or research-paper style, bold.
2. **Figure thesis / subtitle** — smaller, subdued, often italic, one sentence.
3. **Section / region headers** — bold serif or slab-like treatment.
4. **Node labels** — short, readable, bold-ish but not visually heavy.
5. **Node explanation / secondary line** — smaller italic or lighter text.
6. **Annotations** — small, unobtrusive, often italic.
7. **Legend** — compact and neutral.

### 5.2 Text behavior in nodes

- Prefer short noun phrases.
- Limit most nodes to 1–3 lines.
- Use line breaks strategically.
- Avoid paragraph-length explanations inside nodes.
- Put nuance in subtitles, side notes, or small branch annotations.

### 5.3 Compression style

Instead of writing:

> A capability router estimates whether the specialist can support the present state and chooses the best available option.

prefer:

```text
Supported specialist
and in-distribution?
```

with branch annotation:

```text
known + supported
→ specialist
```

---

## 6. Layout grammar

### 6.1 Default canvas

Recommended default canvas:

```yaml
canvas:
  aspect_ratio: 4:3
  background: warm white
  safe_margin: 4–6%
```

This is the default reference. Wider canvases may be used for horizontally structured figures; taller canvases for stacks or ladders.

### 6.2 Region organization

Most figures should respect one of a few clean structural layouts:

- **left → right process flow**,
- **top → bottom hierarchy**,
- **three-column transformation**,
- **central convergence with side inset**,
- **2D conceptual map**,
- **matrix/table**, or
- **staircase / ladder**.

Avoid mixed layout logic inside one figure.

### 6.3 Spacing

Use generous spacing. The figure should not feel crowded.

Recommended composition constraints:

```yaml
spacing:
  major_region_gap: moderate-to-generous
  node_gap: moderate
  text_padding: generous
  edge_clearance: explicit
```

### 6.4 Edge routing

Prefer orthogonal or gently curved routing that reduces ambiguity.

Rules:

1. Avoid crossing edges whenever possible.
2. Merge flows before the destination when several nodes feed one stage.
3. Use elbows rather than diagonal chaos if it improves clarity.
4. Keep arrow direction visually obvious.

---

## 7. Figure hierarchy and macro-structure

A typical figure should read in this order:

```text
Figure Title
    ↓
One-line thesis / subtitle
    ↓
Primary visual structure
    ↓
Secondary annotations / inset panel
    ↓
Legend
```

### 7.1 One figure, one claim

A good title usually states the claim class, not merely the topic.

Good:

- `Specialist-first Routing under Uncertainty`
- `Failure Taxonomy → Recovery → Learning Decision Graph`
- `Improvement Escalation Ladder`

Weaker:

- `Routing Figure`
- `Architecture Diagram`
- `Our System`

---

## 8. Legends

Every complex figure should include a legend if multiple border/arrow semantics are present.

The legend should:

- decode border treatments,
- decode arrow types,
- optionally decode inset panels,
- remain compact,
- not dominate the page.

Legends should not introduce semantics unused in the figure.

---

## 9. Optionality and maturity

One of the most important tasks of this design language is to visually separate:

- what is **core**,
- what is **learning core**,
- what is **optional but useful**,
- what is **research frontier**.

This distinction should appear visually through border treatment and sometimes panel grouping.

Use this consistently because it prevents the architecture from collapsing into a list of named papers or modules.

---

## 10. Architectural role vs implementation instance

A figure should primarily depict **functional slots**, not brand or paper names.

Preferred pattern:

```text
Generalist Capability / VLA
DexFLEX-like Action Realization
TOPReward-like Semantic Critic
VLK-style Synthetic Factory
```

Avoid making the figure's ontology equal to a bibliography.

Rule:

> The diagram should remain valid if every named implementation is replaced.

---

## 11. Density management

### 11.1 Practical density limits

As a default:

- primary nodes should usually remain within a moderate count,
- most nodes should not exceed three text lines,
- only one inset panel should be used unless absolutely necessary,
- figures should not exceed four visual hierarchy levels unless the structure is highly disciplined.

### 11.2 Readability test

A figure should survive the following reductions:

1. embedded in a paper column or half page,
2. viewed as a slide from moderate distance,
3. skimmed in under ten seconds for the main claim.

---

## 12. Anti-patterns

Do **not** do the following unless the subject explicitly requires it:

1. Decorative 3D robot renders.
2. Multiple unrelated figure grammars in one document.
3. Using color only for beauty and not meaning.
4. Huge text blocks inside nodes.
5. Paper names replacing component roles.
6. Overly complex arrow spaghetti.
7. Ambiguous dashed vs dotted usage.
8. Legends that contradict the figure.
9. Bright neon colors.
10. Invented quantitative claims.

---

## 13. Example references

These grounded examples illustrate the design language in practice:

- Unified architecture: `./examples/unified-architecture.png`
- Authority stack: `./examples/authority_timescale_stack.png`
- Routing graph: `./examples/specialist-first-routing.png`
- Failure graph: `./examples/failure-recovery-learning.png`
- Experience flywheel: `./examples/data-economy.png`
- Strategic map: `./examples/research-option-map.png`
- Escalation ladder: `./examples/improvement-ladder.png`
- Evaluation matrix: `./examples/evaluation-matrix.png`

---

## 14. Compliance checklist

Before considering a figure compliant with this design language, verify:

- [ ] Does every border treatment carry stable semantics?
- [ ] Is the title claim-oriented and not generic?
- [ ] Is there a clear primary reading path?
- [ ] Is the figure readable at paper scale?
- [ ] Is optionality visually distinct from core runtime flow?
- [ ] Are implementation examples subordinate to roles?
- [ ] Are text blocks compressed appropriately?
- [ ] Are arrow semantics clear and consistent?
- [ ] Are unnecessary crossings avoided?
- [ ] Is the legend sufficient but not bloated?

If any of the above is false, the figure is not yet complete.
