# Image Evidence

A screenshot is proof, not decoration. If it cannot prove the claim in the title, delete the slide or change the claim. These rules come from five rounds of marker fixes, two PII leaks, and three replaced images on a delivered 453-slide program.

## Source and rights

- Prefer first-party documentation images or a screenshot of a clean workspace you are allowed to publish.
- Record provenance: doc page title, status, check date, URL — in the caption and in speaker notes.
- Do not embed account identifiers, emails, tenant names, or personal file paths.
- Do not redistribute captures as brand assets; the `assets/example-*.png` files in this skill are layout references only.

## Choose the right screenshot

| Content | Good screenshot | Bad screenshot |
|---|---|---|
| A setting exists | The panel with the setting visible | Full desktop with the setting 4 px wide |
| A flow produces output | Run list / DAG / result table | Marketing illustration |
| A policy applies | The policy row and its scope | A diagram of the concept |
| A result is correct | Output table with the asserted rows | Console with a green checkmark only |

Rule: the screenshot must show the thing the callout names. Never write "Deploy button", "Export", "code diff", or "lineage graph" unless those pixels exist.

## Crop to the teaching region

- Prefer ≥800 px wide sources; never upscale more than 1.5×.
- Full-screen captures: crop to the panel or column the callouts talk about (e.g. a 3452 px settings page → 1300 px navigation column).
- Keep the meaningful UI context (breadcrumb, selected tab) but remove unrelated panels.
- Aspect ratio >3.5 (strip screenshots) leaves whitespace; pair it with a decision strip to close the slide.
- Keep at most 0.55 in of vertical slack above the image. Do not center a short image in a tall frame.
- Caption sits immediately under the image's bottom edge (`fy + fh`), not at the frame's bottom.

## Markers

- Numeric badges only: 1–3, red circle, white numeral, ~0.30 in diameter.
- **No text labels on the image.** A label box covers the control it points at; names belong in the rail.
- Rail callouts use `1 · LABEL` / `2 · LABEL` / `3 · LABEL`, ordered top→bottom exactly as the badges appear.
- Compute positions from the **placed image box**, never the container:

```
fx = (x_in - pic.left) / pic.width
fy = (y_in - pic.top) / pic.height
```

- Where the image is letterboxed inside its frame, `pic.left/top/width/height` are the fitted rectangle, not the frame rectangle. Using the frame produces the classic "badge in empty space" error.
- Badges may cover a small part of a label, but never the label being pointed at. If both are impossible, move the badge to the control's edge.
- Render the slide and verify every badge before delivery.

## Redaction

- Cover the whole column (all rows), not just the rows you noticed.
- Re-open the exported PNG and look for: email, owner, user id, workspace name, source path, branch name with a person's name.
- Prefer re-capturing from a clean workspace over blurring; blur is a fallback.
- Never copy identifiers from a screenshot into slide copy. Generalize: "Ứng dụng nghiệp vụ & AI Chatbot", not the demo app's name.

## Screenshot slide checklist

- [ ] The image proves the title's claim.
- [ ] Crop shows the taught region at readable size.
- [ ] 1–3 badges, each touching its element.
- [ ] No text label boxes over the image.
- [ ] Rail callouts ordered top→bottom and naming only visible controls.
- [ ] Caption: source + check date.
- [ ] No PII, no personal identifiers in copy.
- [ ] No unexplained whitespace above or below the image.
