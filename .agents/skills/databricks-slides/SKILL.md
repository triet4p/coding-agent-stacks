---
name: databricks-slides
description: Build editable Databricks-style slide decks that follow the bundled visual references and approved example captures, with declared type/density profiles, topology chosen by the relationship a slide teaches, screenshot-as-evidence rules, layout budgets that prevent template repetition, and QA gates that survive Microsoft PowerPoint. Use for lecture, training, technical, or explainer decks of 20–50 slides.
---

# Databricks Slides

Turn a slide request into an editable deck that visibly follows the bundled Databricks-style system instead of drifting into a generic corporate template. The `assets/example-*.png` files are approved captures from a 15-deck, 453-slide technical training program: match their **structure**, not just their colors.

## Quick start

1. Read `references/layout-spec.md` — tokens, geometry, the four visual families.
2. Read `references/topology-catalog.md` — choose the topology by the relationship the slide teaches.
3. Read `references/repetition-rules.md` — layout and text budget per deck.
4. Read `references/image-evidence.md` before adding any screenshot.
5. Read `references/powerpoint-workflow.md` for a full PPTX, code slides, or batch edits.
6. Read `references/qa-gates.md` before delivery.
7. Open 2–3 `assets/example-*.png` and copy their structure (spacing, callout caps, decision strip).
8. Build editable slides, never a bitmap collage.

## Type and density

Pick **one** profile per deck and declare it at the top of the build script. Never mix profiles inside a deck.

| Profile | Title | Subtitle | Body | Card | Caption | Use when |
|---|---|---|---|---|---|---|
| `training-dense` | 30 pt (auto-shrink to 25) | 17 pt | 18 pt | 16 pt | 13 pt | 20–50 slide technical course; code, tables, screenshots |
| `lecture-sparse` | 32 pt | 20 pt | 24 pt | 20 pt | 16 pt | ≤20 slides; one idea per slide; no tables |

Hard rules for both profiles:

- Displayed copy ≤ ~700 characters per slide (headings, body, callouts; footer excluded).
- Never go below 13 pt for text the learner must read. 10 pt is allowed only for the footer/page number.
- When copy does not fit, delete it or move it to speaker notes. Shrinking below the profile floor is a failure, not a fix.

## Title treatment

Declare one variant for the whole deck:

- `ink-title` (default for decks >20 slides): ink `#0B1F24` bold title with a 0.075 in red rule at the left edge.
- `red-title` (brand-first decks, ≤20 slides): title in brand red, no rule.

Both variants: measure the title with the real font before placing it; shrink 30→25 pt before allowing a wrap; if it wraps to two lines, move the subtitle down to 1.56 in. Never mix variants in one deck.

## Palette

One brand red: `#FF3621`. State colors: info `#2F6BFF`, success `#1A9B62`, caution `#F3B33D`, AI `#7B61FF`, ink `#0B1F24`, border `#D7DDE3`, muted text `#5B6670`. Full tokens and tints: `assets/tokens.json` and `references/layout-spec.md`. Color carries state, never decoration.

## Non-negotiable rules

- Arial for text; Consolas (fallback Cascadia Code, Courier New) for code only.
- Declare one density profile and one title variant per deck; both are documented in the build script header.
- Cover, roadmap/ToC, one divider per section, content slides, summary, end card.
- One dominant idea per slide; one hero diagram per section.
- Layout budget: no template above 25% of slides, never more than 2 consecutive slides of the same template (a UI tour may run 3), tables ≤20%.
- Screenshot is evidence, never decoration: numeric badges only, no text labels on the image, crop to the region being taught, redact PII across whole columns.
- Arrows only where the slide teaches a real sequence or data direction.
- Speaker notes carry `Doc title (status, checked YYYY-MM-DD): URL` for every factual claim.
- No invented identifiers, no personal data, no absolute claims. Mark GA / Public Preview / Beta per cloud.
- Editable PPTX with PowerPoint-safe primitives; no renderer-specific tricks, no full-slide bitmaps.
- Preserve the original deck when localizing: write `_<lang>` copies, never overwrite the source.

## Workflow

### 1. Plan the skeleton

Lock the slide list first: cover → roadmap → (divider → concept → evidence → decision) × N → lab → summary → appendix → end card. Choose 20–50 slides by narrative need; 24–37 is the observed healthy range for a technical module.

### 2. Choose the topology, not the "chart type"

Ask what relationship the slide teaches (sequence, choice, hierarchy, containment, lifecycle, trade-off, evidence, code). Pick from `references/topology-catalog.md`. Tables are for independent attribute matrices only.

### 3. Build

Start from `assets/deckkit_starter.py`; never define deck-local colors or type sizes. Keep one decision strip per slide at most, and only on ≤25% of slides. Use `references/repetition-rules.md` while drafting, not after.

### 4. Render and inspect

Run `scripts/check_deck.py` for hard failures, then `scripts/render_slides.py` and inspect every slide at readable size. A contact sheet is an index, not evidence.

### 5. Close the gate

`references/qa-gates.md` lists the six gates. A deck is done only when all six pass, including opening the file in real Microsoft PowerPoint.

## Assets

Original visual references (keep unchanged):

- `assets/title.png` — dark cover family
- `assets/textonly.png` — multi-column explanation family
- `assets/textwithimage.png` — two-up / icon-led family
- `assets/withimage.png` — flow / process family

Approved captures from a delivered deck (structure references):

- `assets/example-cover.png` — dark cover with eyebrow, chips, mark
- `assets/example-roadmap.png` — four-stage roadmap
- `assets/example-divider.png` — dark full-bleed section divider
- `assets/example-concept-decision.png` — concept flow + `KEY DECISION` strip
- `assets/example-ui-evidence.png` — screenshot + 1–3 badges + rail callouts
- `assets/example-code.png` — dark code panel with callouts
- `assets/example-summary.png` — summary / self-check
- `assets/example-topology-medallion.png` — layered medallion hero
- `assets/example-topology-containment.png` — nested containment (UC hierarchy)
- `assets/example-topology-pyramid.png` — test pyramid with axes
- `assets/example-topology-quadrant.png` — cost × latency trade-off map
- `assets/example-myth-rows.png` — myth → reality → consequence rows

Tooling:

- `assets/tokens.json` — palette, type scale, geometry, budgets
- `assets/deckkit_starter.py` — dependency-light primitives (python-pptx)
- `scripts/check_deck.py`, `scripts/check_layout_budget.py`, `scripts/render_slides.py`

Captures are layout references only; they contain third-party product screenshots sourced from public documentation and must not be redistributed as Databricks brand assets. See `assets/README.md`.
