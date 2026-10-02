---
name: build-databricks-ui
description: "Build or redesign polished web-based data-workspace interfaces with a Databricks-inspired visual language: dense application shells, navigation, tables, filters, editors, forms, status states, light/dark themes, responsive behavior, and accessibility. Use across frameworks and repositories for frontend/UI implementation, CSS/theme work, component styling, dashboard or admin/data-tool screens, and visual consistency reviews. Do not use to copy Databricks trademarks, logos, proprietary illustrations, or product text."
---

# Build Databricks-Inspired UI

Create calm, dense, work-oriented interfaces. Preserve product contracts and accessibility while applying the supplied tokens and component recipes.

## Required reading

Read these files before editing UI code:

1. Read [references/design-language.md](references/design-language.md) for exact colors, spacing, typography, elevation, and interaction rules.
2. Read [references/page-patterns.md](references/page-patterns.md) for shell, explorer, editor, form, table, and state recipes.
3. Use [references/visual-audit.md](references/visual-audit.md) when fidelity to the observed Databricks workspace matters.

Do not improvise a new palette or spacing scale unless the user requests a different brand direction.

## Workflow

1. Inspect the existing component tree, CSS entry points, routing/state flow, and tests. Preserve API calls and domain behavior.
2. Classify the screen as shell, overview, explorer/list, editor, configuration form, review queue, or diagnostics.
3. Identify the target project's framework, styling conventions, package manager, validation commands, and primary theme stylesheet. Follow its repository instructions.
4. Copy `assets/workspace-theme.css` into the app or map its `--dws-*` tokens into the existing stylesheet. Keep semantic token names.
5. For React projects, use `assets/react-shell.tsx` as a structural example, not as a blind replacement. For other frameworks, translate the structure into native components and conventions. Reuse existing components where possible.
6. Apply density in this order: shell dimensions, typography, spacing, controls, borders, then color. Avoid compensating for loose layout with extra decoration.
7. Implement all states: loading, empty, error, success, disabled, selected, hover, focus-visible, and long-content overflow.
8. Check desktop at 1440×900 and a narrow viewport around 390×844. At narrow widths, collapse navigation before shrinking text or controls.
9. Run the target repository's existing frontend checks. Then resolve this skill's installed directory and run its contract checker against the target project's primary theme stylesheet:

   ```text
   node <skill-directory>/scripts/check-ui-contract.mjs <path-to-theme-stylesheet.css>
   ```

10. Visually compare against `assets/reference-board-dark.svg` and `assets/reference-board-light.svg`. Fix hierarchy, density, and state visibility before polishing icons.

## Non-negotiable rules

- Use a 4px base grid; prefer 4, 8, 12, 16, 24, and 32px.
- Use 13px/18px for normal desktop UI text. Use 12px/16px for metadata and section labels.
- Keep the top bar 48px, desktop sidebar about 200px, controls 32px, and table rows 32–36px.
- Use 4px radius for controls, 8px for cards/panels, and pills only for tags/status/toggles.
- Use borders and surface contrast for separation. Use little or no shadow; never use glassmorphism, neon glow, oversized gradients, or floating marketing cards.
- Keep one clear primary action per toolbar. Use blue for primary actions; reserve red/coral for destructive or creation emphasis only when appropriate.
- Use line icons at 16–18px with consistent stroke. Use text labels for unfamiliar actions.
- Keep light and dark themes semantically equivalent. Never encode meaning by color alone.
- Preserve skip links, landmarks, labels, keyboard operation, `aria-current`, `aria-live`, and visible focus.
- Do not embed authenticated URLs, account identifiers, email addresses, screenshots containing personal data, or Databricks brand assets.

## Assets

- `assets/workspace-theme.css`: production-ready tokens and component recipes for light/dark themes.
- `assets/react-shell.tsx`: dependency-free React shell and example primitives.
- `assets/reference-board-dark.svg`: offline dark-theme composition reference.
- `assets/reference-board-light.svg`: offline light-theme composition reference.

Copy only the assets the target needs. Rename the generic `dws-*` classes to existing application classes when that produces a smaller, safer change.

## Completion gate

Finish only when the interface has:

- A clear shell/content hierarchy without decorative clutter.
- Consistent token use and no accidental one-off color system.
- Keyboard-visible focus and labeled controls.
- Responsive navigation and no horizontal page overflow.
- Explicit loading, empty, error, success, and disabled states.
- Passing repository tests and a passing UI-contract check, or a clearly reported pre-existing exception.
