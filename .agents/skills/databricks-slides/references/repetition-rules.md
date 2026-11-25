# Repetition and Density Budget

Decks fail in review for two reasons: the same layout appears too often, or every slide carries too many words. Both are measurable. Check them while drafting, not after.

## Layout budget per deck

| Rule | Threshold | Why |
|---|---|---|
| Share of one template | ≤ 25% of slides | In a 36-slide deck, 9 flows is the practical ceiling |
| Consecutive same template | ≤ 2 | A third identical layout reads as a template, not a lesson |
| UI tour exception | ≤ 3 consecutive `ui_evidence` | Acceptable only if the title pattern changes (claim → claim → consequence) |
| Tables | ≤ 20% of slides | Tables are for matrices, not for relationships |
| Hero diagrams | exactly 1 per section | A second hero dilutes the first |
| Decision strip | ≤ 25% of slides | Otherwise the strip becomes wallpaper |

Measure with:

```bash
python scripts/check_layout_budget.py path/to/build_deck.py
```

The script reports template counts, share per deck, longest run, and violations. Use it before the first render.

## Text budget per slide

| Element | Limit |
|---|---|
| Displayed characters | ≤ ~700 per slide (footer excluded) |
| Card bullets | ≤ 3 |
| Bullet length | 1 line preferred; 2 lines maximum |
| Architecture notes | ≤ 2 cards |
| Screenshot annotations | ≤ 3 |
| Comparison slides | no note stack |
| Callout card height | ≤ 1.60 in (1.25 in for UI rails) |
| Decision text | 1 line at 13–14 pt; shrink to 11 pt before allowing 2 lines |

## Repetition beyond layout

- **Subtitle formula.** Do not open every subtitle with the same prefix ("Evidence: …", "What to remember: …"). Vary the sentence: scope, condition, consequence, or contrast.
- **Card shape.** Four cards with title + 2 bullets, repeated 10 times, is one layout. Alternate with rows, ladder, quadrant, timeline.
- **Decision labels.** Rotate `KEY DECISION` / `REMEMBER` / `RULE OF THUMB` / `PRODUCT STATUS` / `LIMITATION` / `CAUTION`; each has a fixed accent color.
- **Numbering.** Page counters must be derived, never hardcoded per slide; inserting a slide must not require renumbering.

## Diagnosing a repetitive deck

1. Run `check_layout_budget.py`. Any template >25% or run >2 is a finding.
2. Read only the subtitles in order. If three consecutive subtitles share a formula, rewrite two.
3. Thumbnail the deck at 20%: if two slides are indistinguishable at that size, one of them must change topology.
4. Ask of each slide: "what relationship does this teach?" If the answer is "none, it is a list", convert it to a topology or merge it.

## Remediation patterns

| Symptom | Fix |
|---|---|
| Seven tables in one deck | Keep the two real matrices; convert hierarchy → `uc_hierarchy`, lifecycle → `version_lineage`, trade-off → `cost_latency_map` |
| All slides are 4-card grids | Replace with ladder, pyramid, rings, or timeline depending on the relationship |
| Flow used for alternatives | `arrows=False`, or `tiles_2x2` / `concept_decision` |
| Decision strip on every slide | Keep it on the 6–8 slides where a real decision exists |
| Callout card taller than content | Cap at 1.60 in; center the stack in the body band |
