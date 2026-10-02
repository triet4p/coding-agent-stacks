# Layout Spec

Read this file before drafting the deck. Treat the bundled PNGs in `assets/` as visual references to rebuild as editable slides, not as backgrounds to drop into the PPTX.

## Visual system

- Use a 16:9 canvas. Prefer `1280x720`.
- Rebuild the style with PowerPoint-safe primitives: text, solid fills, lines, simple crops, and standard images.
- Default font: `Arial`.
- Title font: `Arial Bold`, `32 pt`, Databricks red.
- Regular body text: `Arial`, `24 pt`, lighter than title. Use dark gray or black with reduced visual weight through color and spacing instead of switching families.
- Small explanatory or caption text: `22 pt` or `20 pt` only when needed to fit dense content.
- Code samples: use a VS Code-like mono stack such as `Cascadia Code`, `Consolas`, then `Courier New`. Keep syntax colors differentiated by token type on a dark code panel.

## Approximate palette

- Ink background: `#001013`
- White canvas: `#FEFEFE`
- Main red: `#FD001A`
- Bright accent red: `#FF2237`
- Soft pink accent: `#FE8A90`
- Gold accent for small kicker text on the cover: `#F3C75F`
- Text on white: near-black such as `#111111` or `#222222`
- Secondary text on white: medium gray such as `#444444` to `#666666`

## Required slide types

- Include one cover/title slide with a distinct theme from normal slides.
- Include one table-of-contents slide near the start.
- Include one section divider slide per section.
- Map every non-divider content slide to one of the four bundled template families.

## Template family 1: `assets/title.png`

- Use for the opening cover only unless the user explicitly asks for more dark slides.
- Use a full dark ink background.
- Keep the Databricks-like red illustration on the right half and large title block on the left half.
- Stack the title on 2-4 short lines with generous leading and strong left alignment.
- Allow a small eyebrow line above the title for module, course, or lecture number.

## Template family 2: `assets/textonly.png`

- Use for concept breakdowns, 3-part frameworks, and ToC slides.
- White background, large title at top left.
- Use a thin red rule above each column or content block.
- Prefer 3 columns for frameworks, or 2 columns for longer text.
- Keep copy airy. Do not exceed about 4 short lines per paragraph block when possible.

## Template family 3: `assets/textwithimage.png`

- Use for paired definitions, risks, compare/contrast, or icon-led teaching points.
- White background, large title at top left.
- Use 2 balanced columns.
- Each column should contain:
  - one red icon or illustration near the upper center
  - one bold subheading
  - one short explanatory paragraph
- Favor icons over decorative shapes.

## Template family 4: `assets/withimage.png`

- Use for flows, pipelines, transformations, or process explanations.
- White background, large title at top left.
- Let the center illustration carry the slide.
- Support the main visual with short labels, not long paragraphs.
- For process visuals, make directionality obvious and keep connectors simple.

## Section divider rule

- Create a dedicated section title slide with a split theme:
  - one half white for the section title
  - one half Databricks red for an icon or illustration
- Prefer a clean vertical split.
- Keep the section title large and minimal. One short subtitle is optional.
- Use a single icon or simple scene on the red half; avoid clutter.

## ToC rule

- The ToC should look like part of the same system, not a generic agenda slide.
- Prefer a `textonly` base with 3-6 numbered items.
- Highlight the current chapter or the first chapter using red, while keeping the rest in dark text.

## Icon and imagery rule

- Prefer official or well-made web icons first when license and provenance are acceptable.
- If suitable icons cannot be found quickly, use `image_gen` for simple flat icons or illustrations that match the bundled visual language.
- Keep icon style consistent within a deck: thin-outline or flat-filled, not both mixed randomly.

## Balance rule

- Favor one dominant proof object per slide: a framework, a pair of concepts, a process, or a code block.
- Avoid walls of text.
- When body copy grows, switch to `textonly` with fewer columns or promote some content into icon-labeled bullets.
