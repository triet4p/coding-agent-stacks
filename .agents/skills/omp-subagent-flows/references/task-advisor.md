# Main-Brokered Task-Advisor Consultations Protocol

This protocol applies when Main brokers diagnostic advice to a fresh, non-blocking `task-advisor` subagent — either for a qualified worker request or for a Main-initiated trigger after stuck diagnostic passes. Advice stays diagnostic; the worker tests it independently.

---

## 1. Request Qualification & Boundaries

- A worker may request diagnostic help when it has a bounded, evidence-backed unresolved technical question or material uncertainty that genuinely useful diagnostic input could inform, including competing plausible hypotheses with no safe discriminating next action. Main may also initiate a consultation after two consecutive stuck diagnostic passes with no safe next action, or when the worker signals pending interest (`advisor_needed: true` without a complete payload) and cannot complete the request itself. Elapsed time or a fixed attempt count alone is never sufficient; generic or open-ended task delegation does not qualify.
- Repeated identical errors or failed hypotheses, no new evidence across distinct attempts, and an unchanged blocker without a discriminating next action are examples, not prerequisites.
- Do not confuse a diagnostic consultation with a `scout` evidence-gathering assignment under `references/scout.md`: scouts collect cited facts for Main's own diagnostic pass, advisors reason over an already-bounded question.
- A worker's `advisor_request` must contain:
  - Matching `task_id`, `attempt_id`, and a unique `consultation_id`.
  - Goal / acceptance criterion and current blocker.
  - Bounded relevant evidence/snippets.
  - Tried hypotheses and their results (or an explicit statement that none were safely tested yet).
  - Constraints and one exact actionable question.
- Do not send full conversations, trajectories, histories, logs, or unrelated context. Workers never spawn advisors or change roles/models/config/depth themselves.

---

## 2. Timer Offer & Deduplication

- The timer's `advisor_offer` ("Bạn cần advisor gì không?") is part of the existing progress request, not a separate message.
- `advisor_needed: false` is a cheap decline and triggers no follow-up.
- `advisor_needed: true` without the complete request payload is pending interest, not a consultation; it never launches an advisor. The worker may add the complete request to its next normal progress reply or send one qualified request directly.
- **Deduplication:** At most one consultation per worker and two active subagents total. Omit advisor offers while a request, interest, consultation, scout, or evidence review is active. A live worker/reviewer pair fills both slots; an advisor cannot bypass the continuation/owner-decision policy in `evidence-review-cycle.md`. A scout is evidence gathering, not a substitute consultation: do not broker an advisor merely because a scout pack was inconclusive.
- Before asking again after a consultation, the worker must first try relevant advice and record the observed result, or provide genuinely new discriminating evidence.

---

## 3. Dispatch & Result Handling

- Main brokers a qualified request to a fresh `task-advisor` sibling using `functions.task` with explicit `agent: "task-advisor"`, `task`, and `solutionSpace`.
- Main forwards only the bounded request. While it is pending, the worker continues only independent safe work; otherwise it waits for an event.
- Advice is diagnostic only, never implementation evidence, approval, or a gate verdict; the worker independently tests relevant advice and records the result.
- Before review, checkpoint execution, or replacement, Main resolves or explicitly cancels every outstanding consultation and invalidates its IDs. Worker completion, cancellation/replacement, and gate transition take precedence over late advisor output.

---

## 4. Dispatch-Consent Policy (Sol Family)

- Dispatch the named `task-advisor` directly, trusting the harness for its effective definition and async execution; do not read definition/configuration files as preflight. For the consent rule below, use available runtime metadata. If it cannot establish whether approval is required, request approval for that task/consultation before dispatch rather than inspecting additional files or assuming consent.
- Any effective advisor route resolving to the GPT-6.1 Sol model family, at any provider or effort, requires explicit user approval scoped to that named task and consultation.
- When approval is required, tell the user the role (`task-advisor`), task and consultation IDs, approval requirement, and blocker/escalation reason (without model/provider names or effort values).
- Approval is one-use and bound to that task/consultation pair. Silence, prior approval, urgency, or failure is not consent.
- After denial or while approval is pending, do not silently replace the user's override with a default. Use another configured route only when separately authorized and independently compliant; otherwise wait and report the role and limitation.
