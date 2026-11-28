---
name: create-project-document
description: Create, restructure, or audit project documentation that explains the business and the implementation and gets readers to a verified first result. Use for project docs sites, onboarding, architecture and workflow guides, and reusable engineering patterns. Keep a Business / Use path and a Technical / Build path.
---

# Create Project Documentation

Deliver two self-contained paths from one landing page:

| Path | Reader can explain | Reader can do |
|---|---|---|
| **Business / Use** | Who it serves, what problem it solves, what changes after use, and what is out of scope | Complete the first useful task and recognize the expected result |
| **Technical / Build** | System boundaries, major flows and patterns worth reusing | Run and verify the project, then locate and test a real change in behavior |

Use the project's docs stack and the audience's language. A CLI, SDK, internal service, or desktop product still needs both paths; label them in the audience's terms and do not assume a GUI or public distribution.

## Workflow

1. **Map scope and evidence.** Inventory supported workflows, major subsystems and common changes. Map them to evidence and destination pages. The shared onboarding example is not a coverage limit. [Coverage and depth](references/depth.md) · [Evidence workflow](references/workflow.md)
2. **Outline a corpus.** Keep entrances short and make destination pages complete. Separate quickstarts, workflows, architecture, patterns, change guides and reference as scope warrants. Summaries and generated indexes do not substitute for explanations or task guides. [Outline template](templates/site-outline.md)
3. **Pilot the rendered site.** Render a landing, a real task and a substantial architecture or pattern article. Review desktop and mobile typography, background, navigation and dense content before scaling. [Presentation](references/presentation.md)
4. **Write and edit.** Use evidence and real examples. Preserve useful detail when redesigning. Edit in the audience's language for precise terms, useful headings and consistent step numbering. [Business / Use](templates/business-use.md) · [Technical / Build](templates/technical-build.md)
5. **Verify depth as well as entry.** Walk both starts, explain a pattern's invariant from code and test, and follow a real change guide to an observable result when runnable. Check the coverage map and rendered long articles. Report gaps and verification limits, not completion by page count.

Do not open with inventory metrics or a combined architecture/deployment poster. Do not use generated images as proof of UI, output or architecture. Never invent commands, outputs, links or an installable release.

[Research and rationale](references/research.md) · [Editable docs-shell wireframe](assets/docs-shell.svg)
