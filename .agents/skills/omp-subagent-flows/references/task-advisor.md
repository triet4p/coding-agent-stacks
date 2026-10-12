# Main-Brokered Task-Advisor Consultations Protocol

This protocol applies only when an active implementation worker explicitly requests diagnostic advice. Main brokers the consultation to a fresh, non-blocking `task-advisor` subagent.

---

## 1. Request Qualification & Boundaries

- A worker may request diagnostic help when it has a bounded, evidence-backed unresolved technical question or material uncertainty that genuinely useful diagnostic input could inform, including competing plausible hypotheses with no safe discriminating next action.
- Repeated identical errors or failed hypotheses, no new evidence across distinct attempts, and an unchanged blocker without a discriminating next action are examples, not prerequisites.
- Elapsed time or a fixed attempt count alone is never sufficient; generic or open-ended task delegation does not qualify.
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
- **Deduplication:** Allow at most one active consultation per worker and two active subagents total. Omit further advisor offers while any request, pending interest, or consultation exists.
- Before asking again after a consultation, the worker must first try relevant advice and record the observed result, or provide genuinely new discriminating evidence.

---

## 3. Dispatch & Result Handling

- Main brokers a qualified request to a fresh `task-advisor` sibling using `functions.task` with explicit `agent: "task-advisor"`, `task`, and `solutionSpace`.
- Main forwards only the bounded request. While it is pending, the worker continues only independent safe work; otherwise it waits for an event.
- Advice is diagnostic only, never implementation evidence, approval, or a gate verdict; the worker independently tests relevant advice and records the result.
- Before review, checkpoint execution, or replacement, Main resolves or explicitly cancels every outstanding consultation and invalidates its IDs. Worker completion, cancellation/replacement, and gate transition take precedence over late advisor output.

---

## 4. Dispatch-Consent Policy (Sol Family)

- Before each advisor launch, Main verifies that the effective `task-advisor` definition is non-blocking and async execution is enabled.
- Any effective advisor route resolving to the GPT-6.1 Sol model family, at any provider or effort, requires explicit user approval scoped to that named task and consultation.
- When approval is required, tell the user the role (`task-advisor`), task and consultation IDs, approval requirement, and blocker/escalation reason (without model/provider names or effort values).
- Approval is one-use and bound to that task/consultation pair. Silence, prior approval, urgency, or failure is not consent.
- After denial or while approval is pending, do not silently replace the user's override with a default. Use another configured route only when separately authorized and independently compliant; otherwise wait and report the role and limitation.
