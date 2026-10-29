# Evidence Review Cycles and Early Gate Decisions

Read when an evidence gate is assigned (Main, worker and reviewer), or when evidence suggests a quantitative gate needs owner reconsideration. This is the shared protocol; role definitions retain ownership and verification duties.

## 1. Count assessed candidates, not messages

- Main assigns `review_cycle_id`, `review_round` and the current criterion reference. Two rounds are authorized by default; round 3 requires Main's explicit conditional authorization below. One round is a submitted, worker-verified implementation/evidence candidate followed by the reviewer's consolidated assessment.
- Questions, explanations, links and metadata from existing evidence do not start another round. Reviewer-run checks to assess the unchanged candidate also stay in that round. Batch findings rather than treating every issue or message as a round; avoid indefinite clarification without new evidence.
- Once substantive findings require implementation changes or worker-created evidence that was materially missing, close that assessment as `changes_requested`. Correcting and resubmitting the candidate for reassessment starts the next round, even with the same agents. Never label substantive corrections as metadata repair to hide rounds.
- Preserve assessed outcomes by task/cycle/round. Duplicate or stale messages do not increment or reset counts. Agent replacement, role escalation, a renamed correction, checkpoint drift or deep-review reopening never resets the task's allowance. A PASS followed by substantive changes also requires the next authorized assessment, not a fresh count.

## 2. Keep the live pair and source ownership

1. With an assigned review, the worker saves its artifact and sends `ready_for_review` with task/attempt/agent IDs, cycle/round, criterion, artifact and candidate snapshot references. Disclose known unmet criteria; readiness is not PASS. Remain active and freeze submitted source during assessment. No assigned review means no keep-alive requirement.
2. Main supplies paired runtime IDs and criterion, artifact/history, repository/ref and report pointers. Resolve advisor consultations first: worker plus reviewer occupy the two active-agent slots. Agents communicate directly via `write agent://<id>`, matching task/cycle/round and both identities. Main receives compact transitions/blockers, not implementation transcripts. Use event-driven waits only while blocked; delivery is not acknowledgment.
3. Each agent fixes only its own records. Reviewer remains read-only on source and worker artifacts, independently checks evidence, and owns its report/manifest. Never demand an unassigned artifact or a future checkpoint: full-route checkpoint execution follows evidence PASS. Missing identity or authorization must be established, never invented.
4. Reviewer records the consolidated outcome, findings and snapshot references. `changes_requested` has `advance: false` and consumes that assessment; it is not a gate PASS. After round 1, the default assignment permits round-2 correction unless an early escalation/blocker applies. The worker fixes, verifies and resubmits; reviewer recaptures the candidate and checks corrected evidence. No PASS during edits or on stale/unannounced source/ref/base drift.
5. After round 2 without PASS, the pair stops corrections and sends Main the progress delta, remaining findings and proposed next check. Reviewer may stay active awaiting Main's round-3 decision. Neither agent authorizes round 3 itself. If an agent has already ended, Main replaces it only as needed with handoff/history and the same count; do not revive completed jobs.
6. Reviewer completes with PASS only with no actionable findings; otherwise FAIL when continuation is blocked or not authorized. Preserve all assessed outcomes in its report. Main accepts a gate only from the matching completed result and current snapshot. After PASS, Main releases the worker to finish (including any explicitly authorized post-review light commit); source must remain the reviewed candidate. Full-route checkpoint remains a separate Bronze-only assignment.

## 3. Main's conditional third round

Main may authorize exactly one third round without asking the owner only when all are supported:
- Earlier findings were materially resolved or measurements show meaningful progress; not merely more effort or renamed hypotheses.
- Remaining findings are bounded, with a concrete correction and a discriminating verification step.
- The criterion remains appropriate and the correction stays inside existing scope, resources and permissions. Do not use round 3 to chase a disputed quantitative gate or repeat a failed approach without new evidence.

Record a concise authorization in existing supervision state/dispatch: resolved findings or measurement delta, remaining finding, planned correction/check, and why one more round is justified. Send it to both agents before round-3 work starts. Do not create a new plan log or artifact just for this decision. If these conditions fail, stop for the owner after round 2. After round 3 without PASS, stop for the owner unconditionally; Main cannot authorize round 4 under routing authority.

## 4. Propose quantitative gate reconsideration early

Do not wait for two assessments or prove impossibility. Worker or reviewer notifies Main as soon as credible measurements indicate a gate may need reconsideration: a planning assumption is contradicted, the target is unlikely within current constraints, reaching it needs material scope/resources/quality tradeoffs, or the measured outcome may already meet the actual user need. A first miss alone is not proof; distinguish measurements, hypotheses and unknowns.

Main presents the criterion and its approval status, observed result and measurement conditions, evidence, likely cost/tradeoff of closing the gap, and a concrete alternative with its user-visible consequence. Ask the owner to retain the gate, revise it explicitly, or defer/stop. Proposed targets are not automatically hard gates; agreed requirements remain binding until the owner changes them.

Pause optimization solely aimed at the disputed gate while awaiting the owner. Independent safe work may continue within existing permissions and concurrency/boundary limits. Do not PASS the disputed criterion, silently lower it, spend the third-round exception on it, or cross a required gate. Owner agreement to retain a criterion does not itself reset round counts.

## 5. Owner decision and safe stop

- Keep `[~]` with `blocked: owner_decision_required` for the affected task. Save worker handoff and reviewer report when applicable; safely pause or finish agents and cancel timers for stopped/paused attempts. An early proposal before review does not require inventing a reviewer report.
- Report targets versus observed results and conditions; satisfied/unmet criteria; assessed rounds and changes/checks; unresolved findings; feasibility constraints versus unknowns; source/commit/checkpoint status; and actual artifact/report/handoff references. Present options: revise a criterion, explicitly authorize a bounded further cycle with unchanged criteria, or defer/stop.
- Only the owner may change criteria or authorize a further cycle after the allowance is exhausted. Record old/new criteria and rationale as a durable plan decision; any further cycle gets a new ID linked to prior outcomes. Approval must state the additional scope/round allowance; silence and general auto-routing authority are insufficient. Revised criteria require assessment against the current evidence before PASS, not a retroactive verdict rewrite.
