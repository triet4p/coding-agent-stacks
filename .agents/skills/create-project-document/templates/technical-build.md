# Technical / Build

> **Editing scaffold, not a published page.** Copy this file into the project's docs, replace every `SCAFFOLD` block with verified facts, then delete the blocks, the unused sections, and this notice. A publishable page contains no `SCAFFOLD` text, empty heading, bracketed slot, `TBD`, or sample carried over from this scaffold. Never publish a command, output, version, port, path, link, screenshot, test result, or benchmark you did not run or take from the repository's evidence; label what is source-only or unverified instead of implying it works. Before publishing, search the page for `SCAFFOLD`: it must return zero matches.
>
> Write in the language the audience reads. Keep code, identifiers, product names, and error text verbatim. Use the project's existing docs stack; plain Markdown here assumes no generator and no UI framework.

> **SCAFFOLD — title and promise.** Replace the heading with the system or product name a builder would search for. State in two or three sentences what the reader can do after this page: obtain and run it, prove the setup, trace one flow, and make one small supported change. Put a direct link to the run section at the top for readers who only need setup; do not repeat the setup itself here. Do not claim a supported platform, release, or integration that the project does not actually ship.

## Overview and boundaries

> **SCAFFOLD — scope of the system.** State what is inside: the components a builder runs, owns, or configures, and the interfaces between them. State what is outside: hosted control planes, proprietary data, other teams' services, unsupported platforms, and anything this document does not cover. Name the real status in the reader's terms — released, source-only, internal, beta, archived — and what that status means for support. Finish with what the reader must provide: runtime, credentials, data, or another running service.

## Canonical example

> **SCAFFOLD — one real trace.** Use the same scenario and input artifact or fixture as the Business / Use page's canonical example; link that section directly for why the outcome matters. Trace the scenario once from entry point to observable result: the command, request, or UI action; the components or files that handle it; the state it reads and writes; and where the evidence lives (test, log, transcript, screenshot, or record). Name the sample data, version, and access requirement. Do not describe an idealized flow the code does not take or simulate an unrun result. If part of the path is unverified, mark the boundary and stop the trace there.

## Run from a clean checkout

> **SCAFFOLD — the supported path.** Start from a clean supported environment and the exact source or artifact a reader can obtain; do not assume a preconfigured machine. List the versions, platform, and services that were actually tested, and name the ones that are known not to work. Then show: obtain, install, configure, start. Every command must be copy-pasteable, and each expected signal quoted from a real run. Put secrets in environment variables or the project's real configuration mechanism; never invent a placeholder credential. If no functioning entry point exists, state that and what is missing; do not promise a download, demo, or setup that does not exist.
>
> If you did not verify a step on a clean checkout, say so beside that step and keep it out of the numbered path. Do not fill gaps from memory or from a different version. End the section with the exact environment and date you verified, including the commit or artifact version.

> **SCAFFOLD — run shape.** Keep the row for the surface this project actually ships and delete the others; once the run steps are written, delete this table too unless the distinction still helps the reader.

| Surface | What "run from clean" proves |
|---|---|
| CLI | Fresh install, one invocation, exit status and output |
| Library | Fresh environment, import, one minimal call, inspected result |
| Service | Real configuration, start, readiness check, one request |
| Web app | Install, start the real dev or built server, load the entry page, one critical action |
| Desktop app | Build or install, launch, complete one checked workflow |

> **SCAFFOLD — prerequisites.** Use a small table of requirement, supported value, and why it matters. Include only rows that were tested or that the project explicitly supports; delete the rest. Name the package manager or installer the project really uses.

## Verify the setup

> **SCAFFOLD — proof before trust.** Give the narrowest check that proves the setup works, then any broader suite the project expects. Quote the real success signal and one real failure signal. State what is skipped on purpose — network, credentials, GPU, external service — and what that leaves unproven. If the check leaves state behind, say how to clean it up. Link the test files or scripts instead of pasting an entire suite.

## Make a first small change

> **SCAFFOLD — a safe seam.** Pick an extension point the project already supports: a message, default, validation rule, adapter, handler, or documented configuration path. Name the file or area, the small edit, the narrow check to run, and the observable difference the change makes. Include how to revert. If no safe change is supported, say so and give the closest read-only inspection instead; do not invent an extension point or a feature request.

## How it flows

> **SCAFFOLD — runtime flow.** Explain one end-to-end run beyond the example: entry point, main components, data or control handoffs, where state lives, and the observable output. Name the boundary between owned code and external services, and where failures surface. A diagram is optional; if used, it must match this text and be editable or source-backed. Do not ship an architecture poster that repeats the section.

## Decisions and trade-offs

> **SCAFFOLD — what a maintainer must preserve.** Record only decisions that constrain future work: what was chosen, why, the rejected alternative, the constraint that forced it, and where it lives in code or configuration. Link decision records or design notes instead of retelling history. Add one "revisit this if" condition per decision. If the project has no durable decisions yet, delete this section rather than inventing rationale.

## Patterns and extension points

> **SCAFFOLD — patterns to copy.** List the patterns a contributor must follow — adapter shape, error handling, configuration flow, test style, naming — and link a representative file or test for each. Then name the real places to add a new command, handler, provider, or surface, including the tests and reference entries that must change with it. Omit anything that is already generated reference. If the project has no stable extension pattern yet, say where conventions live or delete this section; do not invent one.

## Failure modes and diagnosis

> **SCAFFOLD — real failures only.** Use failures that actually occurred or are explicitly designed for: the symptom the reader sees, the check that tells the causes apart, the cause, and the fix or workaround. Separate user error, configuration, environment, and unsupported use. Lead with the observable, not the exception class. Include security and support boundaries, and say what the reader should capture before asking for help. Never invent an error message or a recovery path.

## Reference

> **SCAFFOLD — link, do not duplicate.** Point to the canonical or generated reference for commands, API, configuration, events, and version support, and say how it is regenerated if it is generated. Add the source layout and the test entry points a builder needs. Every link must resolve to current content; if a reference does not exist yet, say what is missing instead of writing an unofficial substitute.

## Where to go next

> **SCAFFOLD — the next real action.** Link the Business / Use path for the problem and outcome, saying it covers who the system serves, what changes after adoption, the first useful task, and the support boundary. Then link the contribution or issue route that actually exists and one next technical task: an extension point, a test, or a documented limitation. Give a real owner or feedback route. Do not end on a generic repository link or a call for contributions with no entry point.
