# Docs site outline

> **Editing scaffold, not a published page.** Plan the site here and keep this file with the project's planning notes, never with reader documentation. Replace the page rows with the real pages, delete rows the project does not need, and delete this notice when the outline is settled. Every cell must name a page that will exist and evidence the project can show; if a cell has nothing real behind it, cut the page or narrow its claim.

One landing page, two explicit reader paths, and one canonical example shared by both. Name the paths the way the audience speaks: "Business / Use" and "Technical / Build" are roles, not mandatory labels. A CLI, library, service, web app, or desktop app still gets both paths; do not assume a GUI, a hosted site, or a public release. Use the project's existing docs stack and language; the English wording here is scaffolding, so publish the pages in the audience's language. This matrix is plain Markdown and assumes no generator.

## Planning matrix

Use these as page types, not a page count. Repeat a type for each significant workflow, subsystem, pattern or reader task. Merge only when the reader question and evidence are shared. A single document works only if it really covers the project at that depth.

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
| Modify behavior | Technical / Build | Where do I start, and what else will this affect? | Contributor | Entry point, owner, callers, contract, before/after and focused regression check | Related pattern |
| Learn a pattern | Technical / Build | What fails without this design, and when should I reuse it? | Maintainer | Invariant, normal/failure paths, enforcing symbols, test, cost and limits | Flow or change guide |
| Diagnose a failure | Either | How can I distinguish causes and recover? | Maintainer or operator | Symptom, discriminating check and safe recovery | Workflow or runbook |
| Look up a contract | Either | What command, field or schema is supported? | Practitioner | Canonical reference and version scope | Example or guide |

## Coverage map

Create a row for each significant item using the [coverage rules](../references/depth.md). An overview or generated index does not count as a substantive destination.

| Workflow, subsystem or change | Audience and question | Impact | Evidence | Destination pages | Verification or gap | Owner |
|---|---|---|---|---|---|---|

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

One shared example is enough for orientation. Add the examples needed for substantive workflows, failures and change guides.

## Link contract

| From | To | The link must promise |
|---|---|---|
| Landing | Both path starts | What the reader can do after each path, not a table of contents |
| Business / Use | Technical / Build | What builders get there: run, verification, internals, extension |
| Technical / Build | Business / Use | The problem, users, and outcome the build serves |
| Either path | Canonical example and limits | Direct anchors; no duplicated prose |
| Every page | A real next action | The next page, section, or external owner |

## Visual pilot (sites)

Pilot the landing, a real first-task page and a substantial architecture or pattern article. Use actual localized copy, sidebar labels and representative code, a diagram, a long table or a procedure. Review first and mid-article screens at 1440×900 and 390×844 in each shipped theme; record changes after the [visual review](../references/presentation.md#9-verify-the-presentation).

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
- [ ] Every high-impact row reaches substantive documentation or states an explicit gap; a real change guide and implementation pattern pass the depth checks.
