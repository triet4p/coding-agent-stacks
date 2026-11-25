# PowerPoint Workflow

Read this when building a real PPTX, code slides, or editing generated decks.

## Authoring path

- Generate with `python-pptx` (or the `Presentations` skill if available); never flatten slides into images.
- Start from `assets/deckkit_starter.py`. One tokens module per project; no deck-local colors or type sizes.
- Recreate the reference style; never place the bundled PNGs as full-slide backgrounds.
- Keep a page-counter helper (`pg()`) so inserting a slide does not require manual renumbering.

## Template gallery first

Before building a full deck, generate `Template-Gallery.pptx` with one sample per template you intend to use, and approve it visually. Restyling individual slides before the gallery is approved guarantees rework: a token change must regenerate decks, not be hand-patched into them.

## PowerPoint-safe constraints

- Standard primitives only: text boxes, rectangles, rounded rectangles, ovals, straight connectors, tables, images.
- Solid fills; no gradients, shadows, blur, blend modes, masks, or SVG filters.
- Set `shadow.inherit = False` on shapes and remove the theme `<p:style>` element, otherwise Office adds an inherited shadow.
- Stick to installed fonts: Arial (text), Consolas (code). For CJK, set `a:ea` explicitly.
- 16:9 at 13.333 × 7.5 in; design at 96 dpi equivalent (1280 × 720).
- Verify in real PowerPoint, not only LibreOffice.

## Code slides

- Mono stack: Consolas → Cascadia Code → Courier New; 13.5–15 pt.
- One snippet per slide, ≤ 12 lines, ≤ 3 callouts.
- Dark panel (`#0B1F24`) with four token colors: keyword blue, string orange, number pale green, comment muted.
- Line numbers are optional; if used, keep them dim (`#5F707A`) and aligned.
- Never translate code shapes; never let a text-fit heuristic count them.

## Editing generated decks

- Patch **per slide segment** (marker `# NN`), never a regex that spans the file. A `.*?` patch once removed 15 slides across three decks.
- After every build: assert `len(prs.slides)` and the marker count.
- Back up the build file before a batch patch; keep a dated copy of the PPTX.
- If a patch goes wrong, recover from the session transcript's `write` tool calls instead of reconstructing by hand.
- Prefer regenerating the deck from the build script over editing the PPTX directly.

## Render loop

1. `python scripts/check_deck.py deck.pptx --expect N` — structure and geometry.
2. `python scripts/check_layout_budget.py build_deck.py` — repetition budget.
3. `python scripts/render_slides.py deck.pptx --dpi 100 --out renders/` — PNG per page.
4. Inspect every page at readable size; fix and re-render the changed pages.
5. Open in Microsoft PowerPoint once; export a PDF from PowerPoint as the final artifact.

LibreOffice is acceptable for iteration. It is not proof that PowerPoint will render the same. If COM is unavailable, say so in the delivery note.

## Deck structure checklist

- [ ] Cover is visually distinct (dark, eyebrow, chips, mark).
- [ ] Roadmap/ToC near the start.
- [ ] One divider per section, each with objective and 3 section chips.
- [ ] Every content slide maps to one visual family and one topology.
- [ ] One hero diagram per section.
- [ ] Summary and end card; references in notes + one appendix.
- [ ] Decision strip on ≤25% of slides, labels rotated.

## Failure modes to fix before delivery

| Failure | Check |
|---|---|
| Title not ink/red per declared variant | Sample three slides |
| Body below 18 pt in `training-dense` | Scan all text runs |
| Text crossing the decision band or footer | `check_deck.py` |
| Screenshot with a text label over the control | Visual pass |
| Badge in empty space | Compare badge to the placed image box |
| Four cards where a trade-off belongs | Topology review |
| Same template three slides in a row | `check_layout_budget.py` |
| Code in a proportional font | Font scan on mono shapes |
| Notes without URL/status/date | Spot-check 10 slides |
| File opens in LibreOffice but not PowerPoint | Gate 5 |

## Delivery note

State what was verified and what was not: renders inspected, PowerPoint open, decks/slides counts, pending user screenshots, unverified demos. Do not describe unverified states as complete.
