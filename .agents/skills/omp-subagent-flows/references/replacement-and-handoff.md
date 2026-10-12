# Subagent Replacement, Continuation & Handoff Protocol

This protocol applies whenever an active subagent is paused, stopped, replaced, or evaluated after repeated progress exchanges.

---

## 1. Main-Owned Supervision & Evaluation Checkpoints

- With the user-disabled soft request budget, Main supervises attempts through existing completion/message events and the one-shot progress timer; do not reinstate a fixed request, elapsed-time, or token cutoff in prompts.
- Continue an active attempt while it adds discriminating evidence or completes remaining criteria. Workers do not voluntarily submit unfinished work merely because a request or token count was reached.
- **Evaluation checkpoint (~4–5 progress exchanges):** After roughly 4–5 matched progress exchanges on an attempt, Main explicitly reassesses progress, blocker, and next safe action:
  - Continue with a concrete reason.
  - Narrow the remaining brief without dropping acceptance criteria.
  - Or replace with a fresh worker.
  - Repeated hypotheses without new evidence warrant earlier intervention. A sent request or delivery receipt is not a completed exchange.
- An unanswered progress request is not evidence of success or stall. Use an adaptive observation timer to prompt reassessment rather than duplicate polling.
- A finished job with a partial handoff, bare yield, or submission missing material verification ends that attempt only, not the task. Keep the task `[~] in progress`.

---

## 2. Mandatory Attempt-Scoped Handoff File

- Before deliberately replacing any flow subagent, and before stopping a paused attempt for the user or a blocker, Main MUST instruct the outgoing agent to write a **detailed, durable, attempt-scoped handoff file**.
- **File location:** Under the assigned project's `artifacts/` directory:
  - `artifacts/sprint-<N>/handoffs/` for sprint tasks.
  - `artifacts/<task-id>/` for standalone tasks.
  - Explicit non-project work uses its explicitly assigned output root.
  - Never use a plan file, `local://`, another project's artifacts, or a global home log.
- **Required contents:**
  - `task_id`, `attempt_id`, runtime `agent_id`, and assigned role.
  - Goal and acceptance criteria (satisfied vs remaining).
  - Current state, changed paths, and ownership (including unrelated user changes).
  - Decisions and rationale.
  - Verified commands/scenarios and actual observed results.
  - Tried and rejected hypotheses.
  - Blockers and unresolved findings.
  - Next safe actions and required checks.
  - References to all relevant earlier attempts and agents (with artifact paths and `history://<id>` URIs).
- The outgoing agent must acknowledge the exact saved path before Main terminates or cancels it. A compact chat summary, plan entry, or delivery receipt is insufficient.
- Main receives only the compact acknowledgment and path reference; Main never transcribes handoff contents into the plan.

---

## 3. Successor Briefing & History Access

- Main MUST supply the saved handoff reference and an explicit related-attempt list in the successor's assignment:
  - Task ID, attempt ID, runtime agent ID, role, artifact/report path, and actual history URI (`history://<runtime-agent-id>`).
  - Include all relevant earlier attempts, not only the immediate predecessor.
  - Explicitly authorize the successor to read those histories and records directly through supported read tools.
- The successor MUST read the detailed handoff and relevant prior history before substantive work, identify verified results and rejected approaches, and report missing/unreadable references.
- Prior evidence is context, not fresh approval; verify current source state before relying on it.
- Ensure the old job has ended or explicitly cancel it (`proc://<job-id>/kill`) before launching the successor. Invalidate attempt/timer/advisor IDs and ignore late events. Keep the same task ID and assign a new attempt ID.

---

## 4. Pauses, Resumptions & Tier Reassessment

- **Pause/Resume:** A paused attempt resumes on the same attempt ID when the user explicitly authorizes resumption; resume requires no replacement handoff and no new async job.
- **Two-Silver-attempt route reassessment:** After two Silver implementation/correction attempts on the same task leave criteria unmet, Main reassesses the route before launching another attempt:
  - Main MAY propose Gold when the remaining obstacle is reasoning, root cause, design, or integration.
  - Main switches only within the user's routing authority or after asking.
  - Missing inputs, access, or external dependencies must be resolved rather than disguised as a model problem.
  - Count worker attempts, not tool retries or progress messages. There is no mandatory tier ladder or automatic Gold promotion.
