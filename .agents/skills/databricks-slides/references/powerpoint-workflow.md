# PowerPoint Workflow

Read this file when building a real deck with this skill.

## Authoring path

- If the `Presentations` skill is available, use it for editable PPTX generation and slide render QA.
- Keep the final deck editable. Do not flatten whole slides into images.
- Recreate the reference style; do not place the PNG templates as full-slide bitmap backgrounds unless the user explicitly asks for a non-editable mockup.

## PowerPoint-safe constraints

- Prefer standard text boxes, rectangles, circles, lines, arrows, tables, and images.
- Use solid fills or very simple gradients only when they survive Microsoft PowerPoint cleanly.
- Avoid unusual SVG effects, masks, blend modes, heavy shadows, unsupported filters, or LibreOffice-only behaviors.
- Stick to installed fonts or common fallbacks. For this skill, default to `Arial` and common mono fonts for code.
- Keep all icons and illustrations as simple PNG or SVG assets that render consistently.
- Avoid layouts that depend on pixel-perfect browser CSS behavior.

## Code slide guidance

- Use a dark code panel inspired by VS Code Dark+.
- Keep token colors intentionally different:
  - keywords: blue
  - strings: orange
  - numbers: light green or pale yellow
  - comments: muted gray-green
  - function and variable names: light text with selective accenting
- Limit each code slide to one main snippet plus 1-3 short callouts.

## Render review loop

- Render every slide after authoring.
- Inspect each slide at readable size, not just the contact sheet.
- Check:
  - title size and color consistency
  - body text remains legible at `24 pt`
  - captions at `22 pt` or `20 pt` are still readable
  - icons are aligned and visually balanced
  - code colors remain distinct after export
  - no crowding near the slide edges
  - section divider split is clean
  - ToC slide spacing is even

## Deck structure checklist

- Cover slide present and visually distinct
- ToC slide present
- Every section begins with a divider slide
- Every content slide maps back to one of the four template families
- Visual and text density feel balanced across the deck

## Failure modes to fix before delivery

- title is black or gray instead of red
- regular body text drifts away from the `24 pt` baseline without reason
- too many unrelated icon styles in one deck
- divider slide looks like a generic content slide
- ToC looks disconnected from the rest of the theme
- code block uses proportional fonts or washed-out syntax colors
- slide looks fine in one renderer but breaks in Microsoft PowerPoint
