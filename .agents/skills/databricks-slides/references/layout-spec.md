# Layout Spec

Read this before drafting any deck. The bundled PNGs in `assets/` are references to rebuild as editable slides, not backgrounds to paste into a PPTX. `assets/example-*.png` are approved captures from a delivered deck — copy their proportions and callout discipline.

## Visual system

- 16:9 canvas, `13.333 × 7.5 in` (equivalent to 1280×720 at 96 dpi).
- Rebuild with PowerPoint-safe primitives: text boxes, rectangles, rounded rectangles, ovals, straight connectors, tables, images.
- Arial for text; Consolas for code.
- Flat surfaces: no shadows, no gradients, no glass, no glow. Separation comes from 1 px borders and one-step surface contrast.
- One brand red (`#FF3621`) at 5–10% of the area. Red is an accent, not a background.

## Tokens

| Token | Hex | Use |
|---|---|---|
| `ink` | `#0B1F24` | Dark surfaces, primary text |
| `red` | `#FF3621` | Brand accent, rules, badges, divider labels |
| `bg` | `#F7F8FA` | Secondary panel surface |
| `white` | `#FFFFFF` | Slide canvas, cards |
| `border` | `#D7DDE3` | 0.75–1.2 pt separators |
| `muted` | `#5B6670` | Subtitles, captions, footer |
| `info` | `#2F6BFF` | Product status, neutral facts |
| `success` | `#1A9B62` | Correct, fixed, running |
| `caution` | `#F3B33D` | Warnings, Preview/Beta |
| `ai` | `#7B61FF` | AI/agent content |
| `danger-soft` | `#E05638` | Limitation strip only |

Tints for callout fills: red `#FDE9E6`, info `#E8EFFF`, success `#E6F5EE`, caution `#FDF3DF`, ai `#EEEAFF`, ink `#ECF0F1`. Machine-readable copy: `assets/tokens.json`.

## Type scale

Two sanctioned profiles; pick one per deck (see SKILL.md):

| Role | `training-dense` | `lecture-sparse` |
|---|---|---|
| Title | 30 pt bold (auto 25) | 32 pt bold |
| Subtitle | 17 pt | 20 pt |
| Body | 18 pt | 24 pt |
| Card title | 16.5 pt bold | 20 pt bold |
| Card body | 16 pt | 20 pt |
| Caption / callout | 13 pt | 16 pt |
| Label (uppercase) | 11 pt | 12 pt |
| Footer | 10 pt | 10 pt |
| Code | 13.5 pt | 15 pt |

Displayed copy ≤ ~700 characters per slide. No learner-facing text below 13 pt.

## Geometry

| Constant | Value | Note |
|---|---|---|
| Slide | 13.333 × 7.5 in | 16:9 |
| Margin | 0.70 in | Left/right |
| Content width | 11.933 in | Slide minus margins |
| Header band | 0.30 – 2.02 in | Eyebrow 0.30, title 0.66, subtitle 1.52/1.56 |
| Body band | 2.02 – 6.72 in | All content lives here |
| Decision strip | 6.02 – 6.58 in | 0.66 in total, 0.56 in panel |
| Footer rule | 6.98 in | Label 7.08 in |
| Card radius | 0.10 in | Panels |
| Node radius | 0.05 in | Diagram nodes |
| Frame radius | 0.03 in | Screenshot frames |
| Callout cap | 1.60 in | 1.25 in for UI rails |

Any template that places text at absolute coordinates must prove `y + h ≤ 6.02` when a decision strip exists, and `≤ 6.98` otherwise. This is the single most common collision in real decks.

## Title treatment

- `ink-title`: ink title + 0.075 in red rule at the left edge (default for >20 slides).
- `red-title`: red title, no rule (brand-first, ≤20 slides).
- Measure with Arial Bold before placing. Shrink 30→25 pt before wrapping. A two-line title pushes the subtitle to 1.56 in; never let title and subtitle share a band.
- Eyebrow: `MODULE 0X · <NAME>` in 10.5 pt uppercase muted, with a small red tick.

## Footer

- Left: `MODULE 02 · COMPUTE & RESOURCE MANAGEMENT` (uppercase, 10 pt, muted).
- Right: `07 / 36` (10 pt, muted).
- No program name, no takeaway text in the footer. Takeaway lives in the decision strip.

## Template families (visual grammar)

1. **Dark cover** (`assets/title.png`, `assets/example-cover.png`) — ink background, eyebrow, 2–3 line title, subtitle, 3–4 chips, product mark.
2. **Text-only** (`assets/textonly.png`) — white, title top-left, 2–4 columns with thin red rules; frameworks and agendas.
3. **Text + image** (`assets/textwithimage.png`) — white, two balanced columns, icon or image per column, short paragraphs.
4. **Image-led** (`assets/withimage.png`) — white, one dominant visual, short labels; flows and pipelines.

These four are the visual grammar, not the full catalog. Structural variety comes from `references/topology-catalog.md` (16 topology groups). Any content slide must map to one family **and** one topology.

## Divider variants

- Default: dark full-bleed `#0B1F24`, `SECTION 0X` in red, white title, one objective line, section progress bar, 3 "In this section" chips.
- Allowed alternative: white/red vertical split (classic skill reference) for brand-led decks.
- A divider never reuses a content layout and never carries body paragraphs.

## Roadmap / ToC

- 4–5 numbered stages, one line of scope each, red current stage.
- Looks like part of the system (same type scale, same rules), not a generic agenda slide.

## Icons and imagery

Two icon layers, never mixed on one slide:

- **Line icons** (Tabler/Lucide subset, MIT, 1.5 stroke, 24 px grid, exported 2× in token colors) for concepts.
- **Databricks product glyphs** (MIT, red strokes, 256×256) for products: Lakehouse, Lakebase, Apps, Genie One/Agents/Code, Unity Catalog, Workspace, AI Gateway, Lakeflow/Jobs/Connect, SQL warehouse, MLflow, Model Serving, Agent Bricks, Delta, Auto Loader, Compute, Serverless, System tables, Photon, Bundles.

Rules:

- Never recolor or stretch a glyph; keep its stroke weight.
- On roadmap/tiles, use product glyphs only when ≥50% of items map to one; otherwise use line icons for all.
- Never use `image_gen` for UI or product icons. Generated illustrations are for hero/conceptual diagrams only, normalized to a white background, cropped tight, with the prompt stored next to the PNG.
- Generated images may contain short English labels; all learner-facing text, numbers, and callouts are shapes on top.

## Tables

Use a table only for an independent attribute matrix (privilege × object, tier × SLA). For hierarchy, inheritance, containment, lifecycle, or trade-off, use a topology — flat rows destroy the relationship.

## Balance

- One dominant proof object per slide: a framework, a pair of concepts, a process, or a code block.
- If body copy grows past the budget, split the slide or move detail to notes.
- Never solve density by shrinking type below the profile floor.
