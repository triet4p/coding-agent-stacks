# Coverage and depth

Keep entry pages concise, not the documentation set. A page about one reader question can be long if the answer needs explanation, evidence and a complete procedure. Split at a new goal, prerequisite, ownership boundary or reusable topic, not at a word count. On an audit, preserve useful detail and stable links; move material to its canonical destination rather than replacing it with a summary. Do not size a corpus by lines of code or a fixed page count.

## Map the project before drafting

Inventory supported capabilities and real user workflows, runtime subsystems and data owners, cross-cutting behavior, common change requests, and operational failure modes. Ground the inventory in entry points, contracts, tests, supported deployment paths and recorded decisions. Use repository structure to find evidence, not as the published table of contents.

Make one planning row per meaningful item: **workflow, subsystem or change → audience and question → impact/priority → evidence → destination routes → verification/status → owner**. Document high-impact areas in scope, including exceptions that alter outcomes. For a full-project request, do not silently drop a supported capability, major subsystem or important change path: record the reason for every exclusion, and report gaps as gaps, not as completed coverage. In an audit, mark existing pages to keep, expand or move; never treat a missing page as a reason to drop the item. The reader-facing navigation should link to the actual articles, not publish the planning matrix.

## Build a corpus, not a pair of summaries

- **Business / Use:** organize around capabilities and reader jobs. Give meaningful workflows task pages with inputs, required access, steps, concrete outputs, handoffs, exceptions and recovery. Explain concepts where they affect a decision; keep detailed operational help reachable from the workflow it supports.
- **Technical / Build:** separate getting started from architecture and system flows, implementation patterns, and guides for modifying behavior. Give major subsystems a home and cross-link shared boundaries. Keep API, configuration and module catalogs under reference; a generated catalog or a link to a directory does not satisfy an explanation or a change guide.
- **Progressive disclosure:** overview pages orient and link; tutorials teach end-to-end; how-tos solve a concrete job; explanations teach mechanisms and trade-offs; reference answers precise lookup questions. Use separate addressable pages for substantial topics, scoped sidebar groups, breadcrumbs where depth warrants them, and stable anchors. Reuse an onboarding scenario across both paths, then add evidence and examples for the workflows and failure cases it cannot cover.

## Page contracts

**Architecture or flow.** Lead with the boundary or question. Trace a concrete action or request through named components and symbols. Show inputs, transitions, data ownership, reads/writes and handoffs; include the important failure or retry branch, how to recognize it and a source/test link. Use diagrams for relationships or sequence when they help; keep labels and paths readable and validate the edges. A stack table alone does not explain a flow.

**Pattern worth learning.** Start with the failure or constraint that makes the pattern useful. Explain its invariant in plain language, the normal and failure paths, what it costs, and when not to copy it. Point to source permalinks for the enforcing symbols and a test or recorded example that would fail if the invariant broke. Show the key excerpt or state transition when it explains more than a file list. Separate documented decision rationale from an inference based on code.

**Modify behavior.** Start from a plausible reader request and state the before/after result. Map the observable entry point to the implementation owner, the contract and affected callers or consumers. Identify the files/symbols to change, which boundaries must remain intact, the narrow test to add or adapt, and where to observe success and one relevant failure. Include compatibility, migration, and safe reversal only where relevant; never discard unrelated working changes. Adding a test without changing behavior does not fulfill this contract. If a change cannot be safely demonstrated, give the source-backed map and mark execution unverified.

## Acceptance beyond onboarding

- Trace every high-impact coverage row to substantive pages or an explicit gap. A title, stub, summary or catalog link does not count. For a full-project request, unresolved high-impact gaps block a claim of completeness. Report coverage and verification separately.
- Walk both first-result paths. From Technical / Build, pick a documented pattern and explain where its invariant is enforced and how a violating case is detected. Then pick a real change guide and, in a safe environment, follow it from entry point to a changed observable result and the focused regression check. Record revision and evidence; distinguish source-only inspection from execution.
- Give a reviewer a single real user job and a single maintainer question without filenames. Both should lead to the right pages without searching the repository or having the author explain the navigation. Check the long article in the real shell, not just the home page. Apply the [editorial pass](presentation.md#10-editorial-pass) before publishing.
