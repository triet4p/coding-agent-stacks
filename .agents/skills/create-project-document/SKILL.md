---
name: create-project-document
description: Create, restructure, or audit project documentation that explains the business and the implementation and gets readers to a verified first result. Use for project docs sites, onboarding, architecture and workflow guides, and reusable engineering patterns. Keep a Business / Use path and a Technical / Build path.
---

# Create Project Documentation

Deliver two self-contained paths from one landing page:

| Path | Reader can explain | Reader can do |
|---|---|---|
| **Business / Use** | Who it serves, what problem it solves, what changes after use, and what is out of scope | Complete the first useful task and recognize the expected result |
| **Technical / Build** | System boundaries, one end-to-end flow, important decisions, and where to inspect or extend it | Start from a clean supported environment, verify a working setup, and find a safe first change if supported |

Use the project's docs stack and the audience's language. A CLI, SDK, internal service, or desktop product still needs both paths; label them in the audience's terms and do not assume a GUI or public distribution.

## Workflow

1. **Collect proof.** Read the existing docs, release/setup entry points, contracts and relevant tests. Choose a representative scenario; capture a safe run or locate representative existing evidence. Separate source-supported behavior, runtime observations, and missing evidence. [Evidence and outline](references/workflow.md)
2. **Outline by reader outcome.** Plan the landing page and both paths before drafting. Give every page one reader question, a concrete outcome and a next action. Reuse the scenario across paths, not the prose. [Site outline template](templates/site-outline.md)
3. **Write and build.** Start with a real input/result and a clear next action. Layer concepts, workflows, internals and reference; keep shared facts canonical. Adapt [Business / Use](templates/business-use.md) and [Technical / Build](templates/technical-build.md). Follow [Presentation](references/presentation.md) for layout, typography, tabs and media.
4. **Verify from the landing page.** Follow both reader paths using the published instructions in a supported safe environment; check links and render the actual surface. For a site, check desktop and mobile, keyboard navigation, and figure readability. Remove placeholders and claims the evidence cannot support. If access or a safe runtime is unavailable, say exactly which path was not verified and why; do not claim it works.

Do not open with inventory metrics or a combined architecture/deployment poster. Do not use generated images as proof of UI, output or architecture. Never invent commands, outputs, links or an installable release.

[Research and rationale](references/research.md) · [Editable docs-shell wireframe](assets/docs-shell.svg)
