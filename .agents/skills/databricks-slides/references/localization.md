# Localization

Localizing a finished deck means re-fitting every layout, because the template measured the source language at build time. Follow this order; it survived a 15-deck, 7,057-string Japanese pass with zero missing strings.

## 1. Extract

- Walk every slide: text frames, table cells, grouped shapes.
- Skip shapes whose runs are all mono/code (SQL, identifiers, JSON). Never translate code.
- Deduplicate strings across the deck; translate unique strings once.
- Keep a per-deck JSON map: `{"source string": "translated string"}`.

## 2. Translate

- Translate **per paragraph**, not per run. Runs are split by formatting, not by meaning.
- Preserve: product names, feature names, SQL, URLs, identifiers, and template labels (`KEY DECISION`, `PRODUCT STATUS`, `CAUTION`, `LIMITATION`). Template accent colors key off those labels.
- Preserve sentence shape where possible: titles stay noun phrases, decision strips stay one clause.
- Use one glossary per deck; "compute", "cluster", "job", "pipeline" must be translated the same way everywhere.

## 3. Apply

- Join the paragraph's runs → translated text → write into the first run → delete the remaining runs.
- Keep the bullet run (`•  `) intact so bullets stay red.
- Never rebuild the text frame; keep paragraph spacing and line spacing.
- For CJK, set the East Asian font (`a:ea`) to a real face (e.g. Yu Gothic) on every run containing CJK, or PowerPoint substitutes unpredictably.

```python
from pptx.oxml.ns import qn
rPr = run._r.get_or_add_rPr()
ea = rPr.find(qn("a:ea"))
if ea is None:
    ea = rPr.makeelement(qn("a:ea"), {})
    rPr.append(ea)
ea.set("typeface", "Yu Gothic")
```

## 4. Re-fit

Measure with the **target** font, not Arial.

| Element | Rule |
|---|---|
| Slide title | 1 line preferred; 2 lines must fit the title box; push subtitle to 1.56 in when 2 lines |
| Cover title | Max 2 lines; if translation needs 3, shorten the translation deliberately |
| Decision value | 13–14 pt; shrink to 11 pt; allow 2 lines only inside the 0.56 in panel |
| Card titles | Max 2 lines; body may drop one step but never below 13 pt |
| Table cells | Re-check row height after translation; CJK wraps at character boundaries |

Do not shrink below the profile floor to force a translation in. Rewrite the translation.

## 5. Verify

- Strings translated == strings extracted; zero empty; zero source-language characters left.
- Zero code shapes modified.
- 15/15 decks open in real PowerPoint.
- 0 shape bounds violations.
- Visual pass on: 15 covers, 15 roadmaps, plus every slide whose title changed line count.

## Failure modes seen in practice

| Symptom | Cause | Fix |
|---|---|---|
| Title runs into subtitle | Template measured source text | Shrink to fit or shorten the translation; move subtitle down |
| Decision strip text spills below the band | 2 lines at 14 pt in a 0.56 in panel | 11–12 pt, or rewrite to one clause |
| Cover becomes 3 lines | Literal translation of a long title | Rewrite the title; do not shrink to 28 pt |
| SQL translated | Code shapes not skipped | Detect mono font and skip |
| Inconsistent CJK glyphs | No `a:ea` set | Set the East Asian font explicitly |
| Vietnamese diacritics clipped | Line spacing too tight | Keep line spacing ≥1.0 for the target font |
