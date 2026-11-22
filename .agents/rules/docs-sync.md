# Doc Sync After Tasks and Sprints

A task is not complete when only its code or primary files are done. User-facing and map-level documents must move with the change, in the same scope and — for committed work — the same commit.

## Which documents

- `README.md` when behavior, setup, usage, or structure changed.
- `CHANGELOG.md` for every user-visible change, per `changelog.md` (same commit as the change, never a follow-up).
- The active plan (`docs/PLAN.md`, `sprint-<N>.md`) status for the task: scope/status change, durable decision, blocker, or verified outcome link.
- Directly affected related summaries (e.g. an architecture overview, contract doc, or artifact index that names the changed behavior). No transitive rewrite of the whole docs tree.

## Ownership

- The implementation worker owns content-doc updates (`README.md`, affected summaries, `CHANGELOG.md` entry) as part of its candidate: it scans doc impact before `ready_for_review` or its final handoff, edits the docs inside its assigned scope, and verifies them under its route.
- The evidence reviewer treats missing or stale required docs as a finding: no PASS leaves a required `README.md`/`CHANGELOG.md`/summary update behind as a "docs follow-up".
- Main owns plan-status updates and verifies doc sync before marking `[x]`, authorizing a commit/checkpoint, or closing a sprint. Content changes after PASS — including doc fixes — invalidate the PASS and need a current assessment.
- A full-route checkpoint/commit scope includes the approved doc updates; a checkpoint that captures code without its approved docs is an incomplete snapshot.

## Sprint close

- Closing a sprint requires: every task `[x]` with its gates met, `CHANGELOG.md` current, `README.md` and related summaries consistent with the shipped behavior, and the plan carrying concise outcome links. If any item is missing, the sprint stays open with the concrete gap named.

## Post-commit doc residue

- A doc edit that lands after its task's assigned commit/checkpoint leaves the worktree dirty. The route's committer closes it immediately with a separate follow-up commit containing only the owned doc paths, under the same authorization as the original commit — no new ask.
- Never amend the earlier commit; never include foreign or unrelated paths; standard porcelain only. Verify afterwards (`git status`) that no owned residue remains.
- If ownership is mixed, the base/ref moved, or hooks/signing reject the commit, stop with `commit_pending` and name the cause. Push still needs its own separate authorization.