# Presentation

Use this reference with [workflow.md](workflow.md) for evidence and outlining, and [research.md](research.md) for sources. It covers the rendered surface: first viewport, shell, typography, navigation, tables and media. The editable wireframe is [assets/docs-shell.svg](../assets/docs-shell.svg); its labels are copy you can replace, and its measurements are defaults.

These rules are stack-agnostic. Apply them to MkDocs, Astro/Starlight, Docusaurus, Hugo, a hand-built site or a README, using that stack's existing components and tokens. Numeric values are a starting baseline, not a brand system.

## 1. The first viewport

The first viewport should answer three questions:

- What is this, and who is it for?
- What changes after I use it?
- Where do I actually begin?

### Landing above the fold

| Include | Why |
|---|---|
| One-sentence purpose in plain language | Replaces a name-only title and acronym chain |
| Audience and situation | Lets the reader decide in five seconds |
| Observable outcome or capability | Answers "what changes" |
| One primary action | Sends the reader to a first useful task |
| Both path entries with one-line outcomes | Business / Use and Technical / Build are visible, not hidden in a tab |
| Optional: one real result (snippet, cropped capture, sample output) | Shows the quality of the promise without a feature tour |

Put this above a 1440×900 first viewport. On mobile, the same order survives one 390×844 screen: purpose, audience, action, then the two paths.

### Do not lead with

- Inventory metrics: route counts, module counts, class/function counts, lines of code, file totals, coverage percentages.
- A combined architecture or deployment poster.
- Changelog, release notes or build metadata as the title.
- An audience switcher that hides one reader path.
- A hero illustration or product collage taller than one third of the viewport.

**First-screen test.** Can readers identify a useful outcome and follow a working entry link without scrolling past implementation metrics? Keep module counts and other inventory in reference. Link to the actual starting point (release, sandbox, package or checkout); describing packaging or listing endpoints does not make a task runnable.

If a promised action has no real release or environment, say so at the action's location and name the access path. Do not replace the missing action with metrics or a screenshot.

## 2. Shell

### Wide desktop (≥1440px)

| Region | Baseline | Rules |
|---|---:|---|
| Top bar | 56px, sticky | Brand, both path entries, search, theme. Never a second copy of the sidebar tree |
| Primary nav | 256px (240–280) | One level, 5–9 entries, `aria-current="page"` on the active route |
| Article column | 720px or 68ch max | Same left edge for every block; do not center long prose |
| In-page TOC | 240px (200–240) | H2 only, sticky, secondary to the primary nav |
| Column gaps | 40–48px | Reduce gaps before reducing type or the measure |
| Page gutters | 48px | 64px on very wide screens |

Use one persistent navigation plus, at most, one in-page TOC. The top bar may carry the two path entries because they are the main decision; it must not repeat chapter or section links that already exist in the sidebar.

**Assign each navigation region one job.** The header switches reader paths, the sidebar navigates pages, and the TOC links to headings within the current page. If the same links appear in multiple regions, remove the duplicates rather than decorating each region differently.

Add another navigation layer only for a genuinely different axis — product, version or locale — and implement it as a labeled selector that changes route or content, not as a third list of the same hierarchy.

Below this width, move the TOC into the article before squeezing the prose into a narrow column.

### Mobile and narrow widths

- At ≤900px, collapse the sidebar into a drawer: 44×44 menu button, 85vw maximum width, same order as desktop, focus trapped while open, closes on route change and Escape.
- Keep the top bar 56px; body 16/26; H1 28/34; gutters 20–24px.
- Do not introduce a second bottom navigation for documentation. One drawer is enough.
- No horizontal page scroll at 320px. Tables scroll inside their own labeled container; wide figures link to a full view instead of shrinking the page.
- Keep the skip link as the first focusable element; use `<header>`, `<nav aria-label="Documentation">`, `<main>`, and `<aside aria-label="On this page">`.
- Active navigation must not rely on color alone: add weight, a bar or `aria-current`, and preserve a 2px visible focus ring.

### Language and labels

Write all interface copy, headings, examples and success signals in the audience's working language. Test the longest strings that language produces (German compounds, Vietnamese diacritics, long role names) in the narrowest nav item and button; wrap or widen the control. Do not truncate a path name to fit an English mock.

## 3. Typography, measure and rhythm

### Baseline tokens

| Token | Value | Notes |
|---|---|---|
| Body | 17/28 (16–18px, 1.6–1.7) | Long-form reading size; never below 16px |
| Measure | 60–75ch, 720px cap | Count characters, not just pixels; a 960px column at 15px is roughly 110+ characters |
| H1 | 40/44, `clamp(32px, 4vw, 44px)` | One per page; may be two lines |
| Lede | 20/32 | One to three sentences under the H1 |
| H2 | 26/32 | 48px space above, 12–16px below |
| H3 | 19/28 | 32px above, 8px below |
| Meta and nav | 14/20 | 12–14px is for labels, never body |
| Code and tables | 14/22 | Monospace inherits the measure; tables may use 13–14px |
| Eyebrow/label | 12/16, 0.08em tracking | Uppercase only for short labels |
| Spacing scale | 4, 8, 12, 16, 24, 32, 48, 64, 96 | 4px base; keep line-heights on the same grid |
| Paragraph gap | 16px (1em) | List item gap 8px |

### Reduce information density before changing type

**Reduce cognitive load before reducing font size.** When a narrative, metric grid, comparison table and dense paragraphs compete, keep the block that answers the current question and move the rest to a relevant section or reference. Split paragraphs when they shift from problem to mechanism, evidence or exception.

Fix density structurally: keep body at 16–18px, cap the measure at 60–75ch, cut paragraphs to four sentences, break a block stack with a heading, and move inventories to reference. 15px is a valid dense-application size; it is not a long-form docs size.

### Vertical rhythm

- One spacing scale for margins, padding and gaps. Do not mix 10/15/22px inventions.
- A section is `H2` + one short intro + content. Use 48px before the H2, 16px after.
- Alternate: at most two prose paragraphs, then a list, code block, table or figure. Prose-only stretches longer than about 120 words need a subheading or a structural break.
- Keep one left edge for title, lede, body, lists and code. Full-bleed is only for figures, wide tables and comparison strips.
- Cards inside cards, tinted panels around every section and decorative dividers flatten hierarchy. Use heading level, space and a single surface step.
- Keep all-caps labels short, letter-spaced and sparse; they are metadata, not headings.

### Density budget

| Element | Budget |
|---|---|
| Paragraph | ≤4 sentences or about 70 words |
| Consecutive prose | ≤2 paragraphs without a structural block |
| Block stack before a heading | ≤3 different block types |
| Callout | 1 per screen; only for a guard that changes the next command or decision |
| Step list | 5–9 steps; split or group beyond that |
| Table | ≤6 columns and ~12 rows before splitting or moving to reference |
| Sidebar | 5–9 top-level entries, one expansion level |
| TOC | ≤12 H2 items |
| Task page | 5–12 minutes to first result; split when it serves two outcomes |

The test is not "does it fit" but "what is the one thing to read next". If three blocks compete, the hierarchy is missing.

## 4. Page anatomy

### Landing

1. Plain-language title, then one-sentence purpose.
2. Audience and the situation it applies to.
3. Primary action: the first useful task.
4. Two labeled paths, each with an outcome, not a table of contents.
5. One shared real example or result, with a link to the canonical detail.
6. Scope limits and prerequisites short enough to read.
7. Secondary links: reference, changelog, repository or release.

Keep the landing free of feature grids, version badges that dominate the title, and a site map. The two path cards are the site map at this level.

### Task article

1. Breadcrumb and H1.
2. Lede: outcome plus prerequisites in one or two sentences.
3. First actionable step, visible in the first screen; no concept lecture or "Act" narrative before it.
4. Expected result or success signal immediately after the action that produces it.
5. Next step or next task at the end, with one cross-path link.
6. Decisions, edge cases and reference detail at the bottom or on a child page.

For a task article, move background into a short lede or a linked explanation and get to the first action. For an explanation or architecture page, lead with the answer or the relevant system view instead; do not manufacture a command.

## 5. Tabs, routes and headings

Choose the smallest structure that keeps content addressable.

| Situation | Use | Why |
|---|---|---|
| Same step, same intent, mutually exclusive variants that change a command (conda/uv, OS, SDK language) | Tabs | Keeps the fork adjacent without duplicating the step |
| Different reader outcome, audience, prerequisites or verification | Route | Needs its own URL, title, search entry and deep link |
| Outline or sub-topic inside one page | Heading + TOC anchor | Printable, searchable, no hidden state |
| Short variants readers compare in one glance (<1 screen, no commands) | Headings | Comparison stays visible; no tab state to lose |
| Entire audience views or product families hide most of the content | Routes or stacked sections | Tabs hide content from search, anchors and no-JS readers |

### Meaningful tabs

- Use tabs only at one decision point, one set per section, no nested tab sets, and never for sequential steps.
- Label the actual choice: `conda`, `uv (PyTorch ≥2.10)`, `Windows`, `TypeScript SDK` — not "Option 1".
- Put shared prerequisites outside the tab set. Never place a version floor or warning inside a single pane without repeating it outside.
- Give every pane an anchor or a URL state (`?variant=uv#install`); deep links and reload must restore the same pane. Do not carry a tab choice across pages.
- Never make JavaScript tabs the only access to content. Render all variants as labeled sections in the static fallback, or link to a stable text equivalent for each variant.

Accessible contract:

- `role="tablist"` on the container; `role="tab"` with `aria-selected`, `aria-controls` and stable `id`; `role="tabpanel"` with `aria-labelledby` and `tabindex="0"`.
- Roving `tabindex`; Arrow Left/Right moves, Home/End jump, focus visibly follows the selected tab.
- The panel is reachable and readable without a mouse; focus never disappears into an invisible pane.
- Selected state is not color-only; text contrast and focus rings meet WCAG AA.

**Common choices.**

- Use tabs for a local, mutually exclusive setup choice such as package manager or shell. Give each variant an addressable state and put shared guards outside the control.
- If both variants are short, show them together under labeled headings; readers can compare and copy without changing state.
- Optional browse filters can change the visible cards, but the main reader paths need direct links and must remain discoverable without filters.

Business / Use and Technical / Build are separately addressable: separate routes on a multi-page site, or dedicated heading anchors in a small single-document project. Never hide either path in a tab pair.

## 6. Linkable table of contents

The TOC exists for the current page, not for the site.

- Include H2 only; nest H3 only on a long reference page. Exclude H1, page metadata and sidebars.
- Cap at about 12 items. Beyond that, group the page under stronger H2s or split it.
- Every heading gets a stable, human-readable `id` at authoring time. Set `scroll-margin-top` to the sticky bar height + 16px.
- Make the active item follow scroll with `IntersectionObserver`; mark it with `aria-current="true"` and a 2px bar, not color alone.
- Loading a deep link selects the matching TOC item and scrolls without covering the heading.
- Below the wide layout, replace the rail with a disclosure directly under the lede: `On this page · 3 sections`. Same anchors, same labels, no duplicated site nav.
- Keep the TOC visually secondary: 12–14px, muted, no promotional box, no "story progress" widget, no second chapter list.

**Check long reference pages independently.** A shallow route tree does not replace heading anchors, a scoped TOC or, when the corpus merits it, search. Readers should be able to share the exact flag group, contract or troubleshooting section without sharing the entire page.

Use reader-task headings ("Verify the result", "Make the first change"), not internal names ("Phase 2 validation", "Layer B").

## 7. One shared example, two paths

Choose one safe, real scenario and make it canonical.

| Path | Shows |
|---|---|
| Business / Use | Input, actor, workflow, observable outcome, limits |
| Technical / Build | The same input crossing one boundary: request, log, state change or file, and where to inspect it |

- Link to the exact section that owns the fixture, command or output. Do not paste two copies that can drift.
- Keep the example small enough to run or inspect, and name its version, sample data and access requirement.
- Cross-link at natural decision points: Business → "how it works" in Technical; Technical → "what the result means" in Business.
- If the example cannot be run with available data or access, state that and link the access path. Do not simulate a result.

## 8. Media: capture, diagram, generated image

| Need | Use | Do not |
|---|---|---|
| Prove a real UI state, error, setting or result | Screenshot or screen capture of the running product | Recreate it, generate it or stage an empty mock |
| Explain flow, boundaries, sequence, state or deployment | Mermaid or draw.io source rendered to SVG | A decorative image with arrows that imply behavior |
| Show terminal commands or output | Code block or transcript | A screenshot of a terminal when text would be copyable |
| Simple spatial structure in a text-native product | ASCII tree or table | A heavy diagram for a five-line hierarchy |
| Cover, mood or concept illustration | Labeled generated image or illustration | Using it as proof of UI, output, setup or architecture |

### Screenshots and captures

- Capture the real product at the documented revision, with safe sample data. No production changes for a screenshot.
- Crop to the region that matters; 2× scale; annotate at most five numbered markers. A full 1440px window shrunk into a column has unreadable 9px UI.
- Alt text states what the reader should notice and the expected result, not "screenshot of the app".
- Caption the environment, version and date. Redact credentials, personal data, customer names and local paths.
- Pair every capture with steps and a success signal; never make the image the only instruction.
- If the product cannot run or be accessed, omit the capture and state the gap.

### Diagrams

- Mermaid for simple flows, sequences, state or ER views: about 12 nodes maximum, one question per figure. Commit the `.mmd` source and render at build time; no runtime CDN.
- draw.io for architecture with regions, boundaries, deployment or icons. Commit the `.drawio` source next to the SVG export; label both themes.
- Label text at least 14px at the final rendered size; an overview reads at about 7±2 nodes. Split overview and detail instead of adding nodes.
- A figure's natural width must fit the article measure (720px), or deserve full-bleed width (up to ~1100px) or its own route with zoom. Never use CSS to shrink a wide diagram into the text column.
- Validate every edge against code, a contract or an observed run. Date the figure and name its version.

**Check at actual display size.** If the reader cannot identify labels and follow the primary arrows at normal zoom, split the figure by question (for example, runtime vs deployment). Link to the full-size detail when it serves a separate need; don't use zoom as the only way to read the overview.

**Match visual to claim.** A layering illustration can explain responsibilities; only a real capture can demonstrate what the interface displayed. Label conceptual figures as conceptual when they could be mistaken for an observed run.

**Text first for text-native surfaces.** Use copyable commands and outputs, comparison tables, or a small ASCII tree. Reserve captures for spatial or stateful interactions that text cannot explain as clearly.

### Generated images

Use only for covers, atmosphere or a clearly labeled concept illustration. State that it is illustrative. Never generate a fake UI, fake terminal, fake benchmark chart, fake architecture or fake output; never use generation to fill a missing release, setup or runtime proof.

### Media QA

- [ ] Render at 320, 390, 768 and 1440 widths; no page-level horizontal scroll.
- [ ] At 200% zoom, labels are still legible and nothing is clipped.
- [ ] Figure text is at least 12px rendered (target 14); otherwise split or link to a full view.
- [ ] Light and dark themes both work; contrast holds; color is not the only signal.
- [ ] Alt text carries the information; decorative images use empty alt.
- [ ] Caption names environment, revision and date; no secrets, PII or machine paths.
- [ ] Source (`.mmd`, `.drawio`, capture script) is committed next to the export.
- [ ] Image dimensions are set to avoid layout shift; below-fold media is lazy.
- [ ] Every link resolves; no placeholder, `TODO` or stale screenshot remains.
- [ ] The capture matches the current build, not an older UI.

## 9. Verify the presentation

Run these against the rendered surface, not the source:

1. **First viewport:** at 1440×900 and 390×844, a new reader can state what it is, who it serves and where to start without scrolling; both paths are reachable in one click.
2. **Navigation count:** one route index plus one in-page TOC. If the same chapter labels appear twice outside the TOC, remove one.
3. **Measure:** body measure stays 60–75ch at desktop; no 960px wall of 15px text.
4. **Tabs:** keyboard only; deep link and reload restore the pane; JavaScript disabled still exposes the content; no critical guard lives in one pane.
5. **TOC:** every H2 has a stable anchor; deep links land below the sticky bar; active state uses `aria-current`, not color alone.
6. **Media:** each figure is readable at 100% at the widest layout that shows it; otherwise it links to a full view. Captures came from a real run and contain no secrets.
7. **Content:** no inventory metrics above the first action; one shared example, linked consistently; cross-path links resolve; no invented commands, outputs, downloads or releases.
8. **Language:** the rendered copy is in the audience's language; the longest labels and headings do not clip or overflow.

Record what was actually rendered and at which viewport. If a viewport, browser, account or runtime was unavailable, name it as a verification limit rather than claiming the path works.
