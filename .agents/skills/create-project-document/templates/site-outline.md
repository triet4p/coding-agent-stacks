# Docs site outline

> **Editing scaffold, not a published page.** Plan the site here and keep this file with the project's planning notes, never with reader documentation. Replace the page rows with the real pages, delete rows the project does not need, and delete this notice when the outline is settled. Every cell must name a page that will exist and evidence the project can show; if a cell has nothing real behind it, cut the page or narrow its claim.

One landing page, two explicit reader paths, and one canonical example shared by both. Name the paths the way the audience speaks: "Business / Use" and "Technical / Build" are roles, not mandatory labels. A CLI, library, service, web app, or desktop app still gets both paths; do not assume a GUI, a hosted site, or a public release. Use the project's existing docs stack and language; the English wording here is scaffolding, so publish the pages in the audience's language. This matrix is plain Markdown and assumes no generator.

## Planning matrix

The rows are the default page set. Merge rows for a small project, split only when a reader goal, prerequisite, or proof changes, and never publish a page whose only content is a heading and a link. Replace the generic persona labels with the roles and situations the project actually serves; one page may serve more than one persona when the question and proof are the same. A single README with both paths is acceptable for a small project; use separate pages when the reader's job or depth genuinely diverges.

| Page | Path | Reader question | Persona | Proof on the page | Next step |
|---|---|---|---|---|---|
| Landing | Shared | Is this for me, and which path should I take? | Evaluator deciding whether to invest time | One real outcome from the canonical example, plus what each path covers | Both path starts, each with a one-line promise |
| What this changes | Business / Use | What problem does this remove, for whom, and what is out of scope? | Sponsor, operator, or buyer who will not run code | The real status quo, who feels it, and the boundary of what changes | See it work |
| See it work | Business / Use | What does a real result look like, and can I trust the proof? | Evaluator who needs evidence before investing time | The canonical example from the reader's side: real input, few actions, visible outcome, evidence source | First useful task |
| Your first useful task | Business / Use | Can I complete one real piece of work now, and what should I see? | Operator doing the job | Verified steps, real expected result, and what to do with it | Workflow and outcome |
| Workflow and outcome | Business / Use | How does this fit the work today, and how do I know it worked? | Operator and their manager | End-to-end workflow grounded in the same example; success signals and records | Limits and support |
| Limits and support | Business / Use | When is this the wrong tool, and who do I ask? | Evaluator or operator at the edge of fit | Real constraints, failure symptoms, support boundary | Technical / Build or stop |
| Overview and boundaries | Technical / Build | What is inside the system, what is outside, and what must I provide? | Engineer or architect taking ownership | Component and dependency boundary, supported environments, real status | Canonical example |
| Canonical example | Technical / Build | What actually happens from entry point to observable result? | Engineer tracing behavior | One real run traced through code or configuration, linked to its evidence | Run from a clean checkout |
| Run from a clean checkout | Technical / Build | Can I get it working from nothing, with the versions you support? | Engineer or operator on a fresh machine | Exact prerequisites, commands, expected signals, verified environment | Verify the setup |
| Verify the setup | Technical / Build | How do I prove this setup is correct before I trust it? | Engineer or maintainer | Narrow verification command and real success/failure output | First small change |
| First small change | Technical / Build | Where can I change something small without breaking the design? | New contributor | One safe edit, the check that proves it, and the observable difference | Patterns and decisions |
| Decisions and patterns | Technical / Build | Why is it built this way, and what should I preserve? | Maintainer or reviewer | Decision table with rejected alternatives and code locations; patterns to copy | Reference |
| Failure and reference | Technical / Build | Where do I look up behavior, and how do I recover? | Maintainer or operator | Symptom → cause → fix from real failures; links to canonical reference | Support or contributing |

## Canonical example register

Choose one real scenario and record it before drafting either path. Both pages link to it and restate only what their reader needs; do not write two examples that drift apart.

- **Scenario:** the real job the example completes, in the user's words.
- **Input:** shareable input, and how it was sanitized.
- **Access:** what a reader needs to reproduce it, and the approved path when access is restricted.
- **Outcome:** what is visibly true when it works, copied from an actual run.
- **Evidence:** the test, transcript, screenshot, or record that proves the outcome, and where it lives.
- **Verified on:** date, version or commit, platform, and any step replaced for safety.
- **Business view:** link to the section that shows the result to a non-builder.
- **Technical view:** link to the trace that shows entry point, transformation, and output.

One example is enough. Add a second only when it proves a different supported path, and link both from the register.

## Link contract

| From | To | The link must promise |
|---|---|---|
| Landing | Both path starts | What the reader can do after each path, not a table of contents |
| Business / Use | Technical / Build | What builders get there: run, verification, internals, extension |
| Technical / Build | Business / Use | The problem, users, and outcome the build serves |
| Either path | Canonical example and limits | Direct anchors; no duplicated prose |
| Every page | A real next action | The next page, section, or external owner |

## Visual pilot (sites)

Before applying a shell to the whole site, select the landing, a real first-task page and an architecture/reference page from the matrix. Record the canvas, subtle surface, text and accent tokens; title/body scale and article measure; and which region owns path switches, page links and heading anchors. Use actual localized copy and one dense block from the project. Capture 1440×900 and 390×844 in each shipped theme and review the [visual acceptance gate](../references/presentation.md#9-verify-the-presentation). Do not publish this planning section.

## Coverage checks

- [ ] The landing page links both paths; neither path is hidden inside the other.
- [ ] Each path works for a reader who never opens the other path.
- [ ] The same canonical example appears in both paths with identical facts and a crosslink.
- [ ] Every command, output, version, and link came from a real source or a recorded run.
- [ ] No release, install, setup, or status claim lacks an artifact or an explicit "source-only / unverified" note.
- [ ] No page is a dead end, an empty heading, or a link list with no proof.
- [ ] Unused rows are deleted; no blank cells survive into the published site.
- [ ] The docs work in the project's real stack and surface; no generator, GUI, or hosted site is assumed.
- [ ] Page titles and body copy use the audience's language; commands and identifiers stay verbatim.
- [ ] A CLI, library, service, web, or desktop product is described in its real surface terms.
- [ ] The outline names who owns updates when behavior or a supported environment changes.
