# Scout Evidence Gathering

Main dispatches a `scout` when a diagnostic pass needs facts Main must not
collect by reading source itself. A scout gathers evidence; it never
diagnoses, decides, or implements.

---

## 1. When to dispatch

- Dispatch only after a diagnostic pass identified a concrete missing fact
  that blocks the next decision (which discriminating test to suggest,
  whether to narrow/replace, or what to ask the owner).
- Do not dispatch when the progress reply plus supervision note already
  supports a decision, when the worker can cheaply observe the fact itself,
  or as a substitute for reading the worker's own artifact.
- At most one scout per attempt at a time; at most two scout dispatches per
  progress exchange. A scout never justifies delaying an overdue owner
  escalation.

## 2. Assignment contract

Each scout assignment carries exactly one question plus its bounds:

- Matching `task_id`, `attempt_id`, and a unique `scout_id`.
- One exact question naming the missing fact.
- Explicit `read_scope`: allowed paths/ranges or grep patterns. No scope
  means no dispatch.
- A result budget: at most a handful of files, a few cited lines each.
- The assigned output root when non-project work applies; otherwise the
  scout returns its pack to Main and writes no record.

## 3. Scout boundaries

- Read-only on the assigned scope. Do not read `history://`, `agent://`, session logs, full trajectories, or anything outside the assigned scope. Do not run commands, edit or write files, spawn agents, or contact the worker. The only reads permitted are the mandatory `~/.agents/rules/*` reads plus the assigned scope.
- Return an evidence pack, not a diagnosis: observed facts with exact
  `file:line` citations, quoted lines where decisive, and an explicit
  statement of what was not found within scope. No conclusions, no
  recommendations, no architecture notes.
- Ephemeral: report and end. A scout owns no durable record and holds no
  slot beyond its single question.
- Main cross-checks the pack against the worker's own reply before using
  it. A pack never overrides worker-observed evidence and never becomes a
  gate verdict; the worker still verifies independently. Never paste a raw
  pack into a worker brief — Main translates it into one targeted question
  or discriminating check.

## 4. Limits

- Timeout is short (a few minutes). On timeout, treat the fact as
  unavailable and decide on current evidence rather than redispatching
  immediately.
- A scout fills no advisor, reviewer, or checkpoint slot permanently, but
  counts toward the two-active-subagent limit while running.
- Do not chain scouts speculatively. Each new dispatch needs a fresh
  diagnostic reason, not merely an inconclusive prior pack.
