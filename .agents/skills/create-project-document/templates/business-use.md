# Business / Use

> **Editing scaffold, not a published page.** Copy this file into the project's docs, replace every `SCAFFOLD` block with verified facts, then delete the blocks, the unused sections, and this notice. A publishable page contains no `SCAFFOLD` text, empty heading, bracketed slot, `TBD`, or sample carried over from this scaffold. Never invent a command, path, version, output, link, screenshot, customer, or result; if a claim has no source or recorded run, cut it or mark it plainly as unverified. Before publishing, search the page for `SCAFFOLD`: it must return zero matches.
>
> Write in the language the audience reads. Keep product names, commands, identifiers, and code verbatim. Use the project's existing docs stack; plain Markdown here assumes no generator and no UI framework.

> **SCAFFOLD — title and promise.** Replace the heading with the outcome in the reader's words, not the internal project name. Open with two or three sentences: who this page is for, what they can do after finishing it, and what it does not cover. No product history, version tour, or feature inventory.

## What this is for

> **SCAFFOLD — the problem.** Describe the work that is slow, risky, manual, or impossible today, who feels it, and what it costs them. Then state the change in plain terms and the boundary: what this product replaces, what it leaves alone, and what it deliberately does not do. Explain a domain term where it first blocks the reader instead of assuming internal vocabulary. If the product is not generally available, say that here in the reader's terms; do not imply a release, hosted service, or support contract that does not exist.

## Who it is for

> **SCAFFOLD — the people.** Name the primary and secondary readers by situation and role, not by job title alone. State what they need before starting: access, data, credentials, a supported machine, an approval, or another team. Name who is explicitly not served yet, so the wrong reader can leave early. Keep this to one short paragraph plus a prerequisite list.

## See it work: the canonical example

> **SCAFFOLD — one real scenario.** Use the same scenario and input artifact or fixture as the Technical / Build page's canonical example. Keep the facts identical and link that section directly instead of re-explaining the machinery; this page owns the business view of the result. Show the real input, the few actions that change it, and the visible outcome, and name the sample data, version, and access requirement. Sanitize private data and say that you did. If the example cannot be run with available access, say so and link the access path; never simulate a result. Do not invent a customer, dataset, price, time saving, or output.

## Your first useful task

> **SCAFFOLD — the shortest real win.** Give the smallest path to one piece of work the reader actually needs, not a feature tour. State prerequisites first, then number the steps. For each step give what the reader does, what they should see, and where that evidence came from. End with one verified line: date, version or commit, platform, and any step replaced for safety.
>
> If you cannot run this task safely in a supported environment, say so on the page and do not present it as working. An unverified step is acceptable only when it is labeled as unverified.

> **SCAFFOLD — surface shape.** Keep the row for the surface this project actually ships and delete the others; once the first-task steps are written, delete this table too unless the distinction still helps the reader.

| Surface | What "first useful task" means |
|---|---|
| CLI | One real command with its input and output, not a flag list |
| Library | Install or import, then one call that returns a result the reader can inspect |
| Service | One request to a running instance, with the response the reader should get |
| Web app | One browser task from entry to a saved or otherwise visible state |
| Desktop app | Install and launch, then one workflow that leaves a saved result |

> **SCAFFOLD — the shape.** Use three to seven steps, in order, each starting with a verb. Show the real result once, near the end. If the reader must choose between variants, keep only the variants that were verified and name the condition that picks each one.

## How the work flows

> **SCAFFOLD — the real day.** Describe the workflow around the product: what triggers it, who acts, what passes to whom, where records or outputs live, and how the result reaches the next person. A short numbered list or a small table is enough; use a diagram only when it carries handoffs that prose cannot. Do not repeat the technical architecture or deployment topology.

## What changes, and how you know

> **SCAFFOLD — outcome and evidence.** State the before/after in the reader's terms and the signals that show success: a saved record, a shorter step count, a review state, a report, a cleaner handoff, or another observable result. Keep numbers only when they were measured in the stated conditions; label estimates as estimates. Say how long the first task should take only if you timed a real run.

## When it does not fit or goes wrong

> **SCAFFOLD — limits first.** List the real constraints: scale, data shape, permissions, environment, availability, and support boundary. Then give common mismatches or failures as symptom → likely cause → what the reader can do or whom to ask. Keep it in the reader's language; link technical troubleshooting instead of pasting logs, stack traces, or configuration internals.

## Where to go next

> **SCAFFOLD — crosslinks and owner.** Link the next page on this path, two or three common next tasks with the real page or section for each, the Technical / Build path with a one-line statement of what it answers, and the canonical example. For the Technical / Build link, say it covers boundaries, the end-to-end flow, a clean-checkout run, verification, and a safe first change. Give one real owner, feedback route, or support entry point. Do not send the reader to a generic homepage or an empty issue tracker.
