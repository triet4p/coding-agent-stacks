---
name: databricks-slides
description: Build editable Databricks-style slide decks that follow the bundled visual templates, including a distinct cover, a table of contents, section divider slides, icon-led teaching slides, and PowerPoint-safe content slides. Use when Codex needs to create or restyle lecture, training, technical, or explainer presentations so they match the Databricks red/ink/white aesthetic from the bundled `templates` images while remaining compatible with Microsoft PowerPoint.
---

# Databricks Slides

Use this skill to turn slide requests into an editable deck that visibly follows the bundled Databricks-style references instead of drifting into a generic corporate template.

## Quick start

1. Read [references/layout-spec.md](references/layout-spec.md) at the start of every deck task.
2. Read [references/powerpoint-workflow.md](references/powerpoint-workflow.md) when the task requires a full PPTX, code slides, or strict QA.
3. Inspect the bundled images in `assets/` and map each requested slide to one template family before authoring.
4. Build the deck as editable slides, not a bitmap collage.
5. Render every slide and fix visual regressions before delivery.

## Non-negotiable rules

- Use `Arial` for normal text unless the user explicitly overrides it.
- Use red `32 pt` bold titles on normal content slides.
- Keep regular text at `24 pt`.
- Drop to `22 pt` or `20 pt` only for dense explanatory text or captions.
- Make the cover slide visually distinct from normal slides.
- Include a ToC slide.
- Start every section with a dedicated divider slide that uses a white/red split theme.
- Keep every content slide aligned to one of the four bundled template families.
- Prefer web-sourced icons with acceptable provenance; fall back to `image_gen` only when suitable icons cannot be found.
- Keep code slides in a VS Code-like mono font and syntax-colored dark panel.
- Preserve Microsoft PowerPoint compatibility; avoid renderer-specific tricks.

## Workflow

### 1. Plan the deck skeleton

- Lock the slide list first.
- Require this minimum structure:
  - cover
  - ToC
  - one divider per section
  - content slides mapped to the four template families
- Spread dense text across more slides instead of shrinking everything below the baseline sizes.

### 2. Choose the template family per slide

- Use `title.png` for the cover.
- Use `textonly.png` for frameworks, chapter agendas, and multi-column explanation slides.
- Use `textwithimage.png` for two-up comparisons, definitions, risks, and icon-led explanations.
- Use `withimage.png` for flows, pipelines, and process-heavy concepts.
- Use the custom white/red split divider for section titles.

### 3. Build the visuals

- Favor simple, high-contrast shapes and icons.
- Keep one dominant visual idea per slide.
- Balance text and image weight; if a slide feels prose-heavy, convert part of it into icon-labeled blocks or split it into two slides.
- For code slides, keep the snippet short and pair it with only a few callouts.

### 4. Run slide-by-slide QA

- Render every slide.
- Compare each render back to the intended template family.
- Fix any title drift, alignment drift, inconsistent icon style, unreadable small text, or broken code coloring.
- Do not stop at a contact sheet pass; inspect each slide at readable size.

## Assets

- `assets/title.png`
- `assets/textonly.png`
- `assets/textwithimage.png`
- `assets/withimage.png`

Use these as style references to reconstruct editable slides.
