# Evidence, Outline and Verification

## 1. Identify the reader's jobs

| Project | Business / Use first result | Technical / Build first result |
|---|---|---|
| Web or desktop product | Complete a representative task in a sample workspace | Start a supported local instance and inspect the relevant flow |
| CLI or library | Install/import and get meaningful output on a sample input | Build/test from checkout and trace the command/API to its implementation |
| API or service | Send one supported request against a sandbox or local instance and interpret the response | Start dependencies, check readiness, and trace the request through the service |
| Internal or restricted project | Use the approved sandbox or follow a genuine recorded walkthrough when access is unavailable | Follow the authorized checkout/setup path; state access requirements and how to request them |

Use the actual names of roles and jobs, not assumed personas. The same reader may need both paths: a library consumer belongs in Use, a library maintainer in Build. An overview can explain both audiences' shared domain vocabulary without duplicating either path.

## 2. Collect evidence before drafting

- Check README, manifests/lockfiles, release artifacts, setup scripts, defaults, entry points, tests and relevant decision history. Prefer the public or authorized environment readers will actually have.
- Select a scenario with **input → meaningful result**. Record the revision/version, environment, commands/steps, observed output and relevant source/test anchors. Group claims as **observed at runtime**, **supported by source/contract**, or **unverified**. Keep one row per consequential claim rather than including an entire scan or transcript.
- Capture the successful path plus the first common blocker or critical boundary when evidence supports it. Redact identifiers, customer data, credentials and local machine paths before publishing any log or image. Use safe sample data; do not make production changes for screenshots.
- Prefer source permalinks at the documented version for behavior, and a stable release/index link for downloads. Never infer business goals or decision rationale from dependency names. If evidence conflicts, narrow the claim to the confirmed scope and report the discrepancy. Do not turn a filename into a plausible but unverified startup command.

## 3. Outline by questions, not inventory

Start with the [outline template](../templates/site-outline.md). For each candidate page ask: **Who opens this, what single question does it answer, what proves the answer, and where should the reader go next?** Merge pages that answer the same question. Split a page when the reader's goal, prerequisites or depth changes, or the content needs a stable share link.

- **Landing:** what the project enables, for whom, one real example result, and links to both paths. Prefer a runnable or inspectable sample over a generic architecture graphic. Do not use API/module counts as proof of value.
- **Business / Use:** problem and actors → example outcome and limits → first real task → common next tasks. Explain domain terms where they first matter. Put a necessary prerequisite before the action it gates.
- **Technical / Build:** quickstart link at the top; show context/boundaries → one trace through the system; add focused subpages for state, deployment, extension points or decisions only when each answers a distinct question. End with how to verify and where to make a first supported change. Keep flags, schemas and catalogs under Reference.
- **Shared facts:** setup safety, terminology and contracts get one canonical owner. Cross-link to the exact section; don't paste two copies. Reuse the example artifact or fixture across both paths so the reader can connect the business result to its technical mechanism.

A single README with headings is fine for a small project. If the project already has a docs site, retain its stack and working navigation; use separate routes when justified. Keep architecture diagrams and excerpts maintainable and update affected guides with behavior changes.

## 4. Verify as the reader

- **Use:** start at the landing page, find the correct entry point without repo knowledge, follow the written steps, and compare a real result with the documented success signal. A recorded walkthrough shows what to expect but does not prove self-start.
- **Build:** in a clean or isolated supported setup, follow only the documented commands from checkout to readiness. Check one representative request/output and the narrow test for the example or first change. Record environment and revision; avoid assuming the author's cache, credentials or ambient services.
- **Content/UI:** check section and cross-path links, shared example consistency, screenshot freshness, diagram edges against evidence and readability on the rendered surface. A first-time reader should be able to paraphrase the business result and trace one important boundary without opening the full reference.
- A gated environment can have a valid documented access path. If you cannot observe it, mark verification limits in the handoff; do not mark either path passed on source review alone. If there is no functioning entry point, report that missing prerequisite rather than promising a download, demo or setup that does not exist.
