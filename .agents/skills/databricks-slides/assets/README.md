# Skill assets

## Visual references (original, unchanged)

| File | Family |
|---|---|
| `title.png` | Dark cover |
| `textonly.png` | Multi-column explanation |
| `textwithimage.png` | Two-up / icon-led |
| `withimage.png` | Flow / process |

## Approved captures (`example-*.png`)

1280×720 PNG captured at 96 dpi from a delivered 453-slide Databricks technical training program. Use them to copy structure — spacing, callout caps, decision strip proportions, badge discipline — not as slide backgrounds.

| File | What it demonstrates |
|---|---|
| `example-cover.png` | Dark cover: eyebrow, 2-line title, subtitle, 4 chips, product mark |
| `example-roadmap.png` | Four-stage roadmap with current stage marked |
| `example-divider.png` | Dark full-bleed divider: `SECTION 01`, objective, progress bar, section chips |
| `example-concept-decision.png` | Concept flow + `KEY DECISION` strip at 6.02 in |
| `example-ui-evidence.png` | Screenshot + 3 numeric badges + rail callouts `1 ·`…`3 ·` + source caption |
| `example-code.png` | Dark code panel, line numbers, mono type, callouts |
| `example-summary.png` | Summary / self-check with takeaways |
| `example-topology-medallion.png` | Layered medallion hero (Bronze/Silver/Gold with owners) |
| `example-topology-containment.png` | Nested containment: metastore ⊃ catalog ⊃ schema ⊃ object |
| `example-topology-pyramid.png` | Test pyramid with cost/reality/frequency axes |
| `example-topology-quadrant.png` | Cost × latency trade-off map with four levers |
| `example-myth-rows.png` | Myth → reality → consequence rows |

Regenerating: build the deck with the same tokens, then `python scripts/render_slides.py deck.pptx --dpi 96 --pages 1,2,4,5`.

## Rights

The captures are internal layout references. They contain product screenshots sourced from public Databricks documentation and must not be redistributed as Databricks brand assets, used in marketing, or presented as official material. Product glyphs referenced by the catalog are MIT-licensed artwork; keep their attribution file when you copy them into a project.
