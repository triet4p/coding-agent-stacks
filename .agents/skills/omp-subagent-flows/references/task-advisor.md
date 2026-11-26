# Main-Brokered Task-Advisor Consultations Protocol

This protocol applies when Main brokers diagnostic advice to a fresh, non-blocking `task-advisor` subagent — either for a qualified worker request or for a Main-initiated trigger after stuck diagnostic passes. Advice stays diagnostic; the worker tests it independently.

---

## 1. Request Qualification & Boundaries

- A worker may request diagnostic help when it has a bounded, evidence-backed unresolved technical question or material uncertainty that genuinely useful diagnostic input could inform, including competing plausible hypotheses with no safe discriminating next action. Main may also initiate a consultation after two consecutive stuck diagnostic passes with no safe next action, or when the worker signals pending interest (`advisor_needed: true` without a complete payload) and cannot complete the request itself. Elapsed time or a fixed attempt count alone is never sufficient; generic or open-ended task delegation does not qualify. Every consultation — worker-requested or Main-initiated — needs explicit user approval before dispatch (see §4). Main must treat its own uncertain judgment as a trigger, not a decision: never resolve a diagnostic question by Main's own guess when a bounded probe, scout, approved advisor, or owner question could settle it.
- Repeated identical errors or failed hypotheses, no new evidence across distinct attempts, and an unchanged blocker without a discriminating next action are examples, not prerequisites.
- Do not confuse a diagnostic consultation with a `scout` evidence-gathering assignment under `references/scout.md`: scouts collect cited facts for Main's own diagnostic pass, advisors reason over an already-bounded question.
- A worker's `advisor_request` must contain:
  - Matching `task_id`, `attempt_id`, and a unique `consultation_id`.
  - Goal / acceptance criterion and current blocker.
  - Bounded relevant evidence/snippets.
  - Tried hypotheses and their results (or an explicit statement that none were safely tested yet).
  - Constraints and one exact actionable question.
- Every consultation also carries a current `scout_pack` for the same blocker: cited facts with exact `file:line` references gathered by a `scout` under `references/scout.md`. When the worker's own evidence already includes bounded code excerpts with paths and line ranges, that evidence counts as the pack and no separate scout is needed. Otherwise Main dispatches the scout first and attaches its pack; never broker an advisor on a thin request alone.

---

## 2. Timer Offer & Deduplication

- The timer's `advisor_offer` ("Bạn cần advisor gì không?") is part of the existing progress request, not a separate message.
- `advisor_needed: false` is a cheap decline and triggers no follow-up.
- `advisor_needed: true` without the complete request payload is pending interest, not a consultation; it never launches an advisor. The worker may add the complete request to its next normal progress reply or send one qualified request directly.
- **Deduplication and top-up pairing:** at most one consultation per worker and three active subagents total. A consultation always runs after its initial `scout_pack`: dispatch the scout first, then broker the advisor with the pack attached. Main pairs the two by exchanging their runtime IDs in both briefs. When the pack is insufficient, advisor and scout talk directly via `write agent://<id>` — one concrete missing observation at a time, matched on task/attempt/consultation/scout IDs, answered with a cited pack, CC'd to Main's parent-visible channel. At most two advisor↔scout rounds per consultation; then the advisor returns a diagnosis with explicit unverified gaps instead of asking again. No second advisor, reviewer, or checkpoint executor runs concurrently with a worker-advisor-scout trio. An advisor cannot bypass the continuation/owner-decision policy in `evidence-review-cycle.md`. Do not start a second consultation merely because the first advice plus its pack was inconclusive — resolve it with the worker's test result or genuinely new discriminating evidence first. No consultation launches without explicit user approval; a qualified worker request waits for that approval and is never self-authorizing.
- Before asking again after a consultation, the worker must first try relevant advice and record the observed result, or provide genuinely new discriminating evidence.

---

## 3. Dispatch & Result Handling

- After explicit user approval, Main brokers a qualified request plus its initial `scout_pack` to a fresh `task-advisor` sibling using `functions.task` with explicit `agent: "task-advisor"`, `task`, and `solutionSpace`, including the paired scout's runtime ID and the consultation scope the top-up must stay inside. The pack is part of the brokered request, not a separate message. Follow-up top-ups flow directly between advisor and scout; Main monitors the CC'd messages but does not relay.
- Main forwards the bounded request with the attached pack. While the consultation is pending, the worker continues only independent safe work; otherwise it waits for an event.
- Advice is diagnostic only, never implementation evidence, approval, or a gate verdict; the worker independently tests relevant advice and records the result.
- Before review, checkpoint execution, or replacement, Main resolves or explicitly cancels every outstanding consultation and invalidates its IDs. Worker completion, cancellation/replacement, and gate transition take precedence over late advisor output.

---


## 4. Universal Approval Before Dispatch
- Every `task-advisor` dispatch needs explicit user approval scoped to that named task and consultation — worker-requested or Main-initiated alike. The former Sol-family-only rule is superseded: approval is now unconditional.
- When asking, Main states the advisor role, task and consultation IDs, blocker/escalation reason, its own leading hypothesis with supporting evidence, and the necessity level (`blocker` vs `accelerator`) — no model/provider names, selectors or effort values.
- Approval is one-use and bound to that task/consultation pair. Silence, prior approval, urgency, or failure is not consent.
- After denial or while approval is pending, do not launch, do not silently substitute another route, and do not treat the worker's qualified request as self-authorizing; the worker continues only independent safe work or waits. Use another configured route only when separately authorized and independently compliant.
- The ask carries Main's own read first: leading hypothesis with supporting evidence, what was already tried (probe/scout and result), why it is insufficient, and a necessity level — `blocker` (no safe forward path; on denial Main narrows, replaces, or stops for the owner) or `accelerator` (Main has a plausible path; the advisor would de-risk or verify it; on denial Main proceeds with the stated risk). Denial never means silently retrying the same ask.
