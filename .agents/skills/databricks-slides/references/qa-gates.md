# QA Gates

A deck is done only when all six gates pass. "Rendered once" is not a gate. Each gate below names the exact check and the failure it prevents.

## Gate 1 — Structure

```bash
python scripts/check_deck.py deck.pptx --expect 36
```

- Slide count equals the plan.
- Cover, roadmap, one divider per section, summary, end card exist.
- Every section has exactly one hero diagram.

**Prevents:** silently lost slides after a batch patch (a real incident removed 15 slides across three decks).

## Gate 2 — Geometry

Same script; it fails on:

- negative `left`/`top`;
- `left + width` or `top + height` beyond the slide (+9000 EMU tolerance);
- learner-facing text entering the decision band (`6.02–6.58 in`);
- learner-facing text crossing the footer rule (`6.98 in`).

**Prevents:** the four template collisions that hit decision strips and footers.

## Gate 3 — Layout budget

```bash
python scripts/check_layout_budget.py build_deck.py --max-share 25 --max-run 2
```

- No template above 25% of slides.
- No run longer than 2 (UI tours may reach 3 with changing titles).
- Tables ≤20%.

**Prevents:** decks that read as a template instead of a course.

## Gate 4 — Render and read

```bash
python scripts/render_slides.py deck.pptx --dpi 100 --out renders/
```

- Inspect **every** slide at readable size, not a contact sheet.
- A contact sheet is an index for finding slides; it is not evidence that text fits.
- Check: title/subtitle separation, card bottoms, callout caps, badge placement, code contrast.

**Prevents:** "text overlap = 0" being mistaken for "nothing is clipped" — PDF text extraction misses shapes clipped at the slide edge and text overflowing a card.

## Gate 5 — Real PowerPoint

Open the file with Microsoft PowerPoint (COM `Presentations.Open` or manual open) and export to PDF once.

```powershell
$ppt = New-Object -ComObject PowerPoint.Application
$p = $ppt.Presentations.Open("C:\path\deck.pptx", $true, $false, $false)
$p.SaveAs("C:\path\deck.pdf", 32)
$p.Close(); $ppt.Quit()
```

- If the file is locked by an open PowerPoint window, close it first (Windows creates `~$deck.pptx`).
- When COM is unavailable, LibreOffice rendering is an accepted fallback **only** if the limitation is reported.

**Prevents:** decks that look correct in LibreOffice and break in PowerPoint.

## Gate 6 — Content integrity

- Every factual claim has a note line: `- Doc title (status, checked YYYY-MM-DD): URL`.
- GA / Public Preview / Beta stated per cloud; no absolute claims ("always cheaper", "0 s cold start").
- Product names current, with "(formerly …)" where renamed.
- No invented identifiers, no PII, no personal demo names.
- Code snippets use named arguments and valid identifiers; they are never translated.

**Prevents:** the ten-plus factual corrections that required a dedicated fact-check round.

## Overflow detectors: use, don't trust

A text-fit estimator that divides estimated lines by box height produces **false positives** on small shapes: cover chips, section labels, page numbers. Use it to rank slides for human review, never to declare failure.

Rules:

- Skip code shapes (mono font) in any text-fit heuristic.
- Ignore shapes shorter than 0.30 in or narrower than 0.60 in.
- Treat ratio >1.25 as "look at this slide", not "this slide is broken".
- Final authority is the rendered image at readable size.

## Regression set

When changing a template or a shared primitive, re-render a small set that previously failed:

| Slide | What it proves |
|---|---|
| A two-line title with subtitle | Title/subtitle separation |
| A screenshot with 3 badges | Badge math, callout order |
| A 2-line decision value | Decision strip containment |
| A cover with a long title | Cover max 2 lines |
| A quadrant with 4 cards | Card overlap and axis labels |
| A pyramid | Trapezoid widths |
| A code slide | Mono contrast, no translation |

Compare against `assets/example-*.png` where the topology matches.
