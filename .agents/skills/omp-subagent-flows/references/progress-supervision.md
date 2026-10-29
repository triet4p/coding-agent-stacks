# Diagnostic Progress Supervision

Main reads this protocol when launching the first active flow attempt. Workers/reviewers use the progress-response contract in their own role/skill; they need not preload this Main-only reference.

---

## 1. Timer lifecycle

- For every active attempt, start exactly one finite background shell timer with an adaptive observation interval of **10–45 minutes**. Use an existing finite async shell timer (for example, PowerShell `Start-Sleep` through Bash with async enabled) emitting task ID, attempt ID and timer-generation ID. This is an observation prompt, not a worker deadline or a reason to stop work.
- Choose the interval from task context and observed progress. Keep only one timer generation active per attempt; never rearm in a hot loop. Treat a blocker message as an immediate diagnostic trigger; do not wait for the timer when one arrives.
- On attempt completion, completion takes precedence: cancel any active timer and invalidate its generation. If completion races with a timer, process completion first. Ignore stale task/attempt/generation events. Cancel timers for attempts paused for an owner decision and rearm only on authorized resumption.
- On a current timer event, send exactly one outstanding `progress_request` with `task_id`, `attempt_id`, `agent_id`, `progress_request_id`, and `timer_generation`. Do not send another while a reply is pending. For implementation workers only, include `advisor_offer: "Bạn cần advisor gì không?"` when no advisor request/interest/consultation, scout, or evidence reviewer is active. Worker plus reviewer occupy both slots. Reviewers and checkpoint executors never receive the offer.
- The matching reply contains those IDs plus `stage`, `completed_since_last_report`, `new_evidence`, `current_blocker`, `attempts`, `results`, `next_action`, and `help_needed`. Implementation workers additionally return `tried_hypotheses` (ruled-in/ruled-out with the deciding observation) and `advisor_needed: false|true`, and may supply one qualified advisor request. A true flag without a complete request is pending interest, not permission to launch. Reviewers and checkpoint executors do not request advisors.

## 2. Supervision note

Main keeps one short supervision note per attempt in its own separate file under the assigned `artifacts/` directory (never in a plan). Each matched reply appends at most three lines: previous blocker → current blocker, evidence delta, and hypotheses ruled in/out. The note is the loop memory: it detects repetition cheaply without rereading histories.

## 3. Diagnostic pass

Run this pass on every matched reply or blocker message, before deciding anything else:

1. **Compare against the note**, not elapsed time. Stall signals: same `current_blocker` across two replies with empty `new_evidence`; `next_action` repeated verbatim; `results` contradicting `completed_since_last_report`; vague `help_needed` with `advisor_needed: false`; a done claim whose verification does not cover the criteria.
2. **Classify:** progressing (evidence grows, blocker moves), stuck (a stall signal holds), or blocked (missing prerequisite, disputed gate, or no safe discriminating action exists).
3. **Progressing:** continue silently. No probe, no scout, no message beyond the timer rhythm.
4. **Stuck with a testable hypothesis:** send one targeted probe or discriminating check to the worker. At most one outstanding probe; the worker tests and reports back.
5. **Stuck but missing a fact Main must not read directly:** dispatch one `scout` under `references/scout.md` with a single question and explicit read scope. Use the pack only to form the next probe, narrow, or escalation — never paste it raw into a worker brief.
6. **Stuck needing fresh reasoning, not facts:** broker `task-advisor` help — Main-initiated when the worker shows pending interest or two consecutive stuck passes with no safe next action, worker-requested when a qualified `advisor_request` arrives. Apply `references/task-advisor.md`. Advice stays diagnostic; the worker tests it independently.
7. **Blocked:** narrow the brief without dropping criteria, replace with handoff/history, or stop for the owner with criterion-versus-result evidence. Never spend probes, scouts, or advisor consultations to evade an owner decision.

Progress, timer and delivery events never establish completion or a gate verdict. After a matching reply, if the attempt is still active with no pending request, start the next one-shot generation at an adaptive 10–45-minute interval.

## 4. Continuation checkpoints

- After roughly 4–5 matched exchanges, reassess progress, blocker and next safe action against the supervision note. This does not override review-round limits or an early gate-reconsideration stop.
- Follow `replacement-and-handoff.md` only when pause/replacement is actually needed; do not repeatedly poll or use eval wait barriers for supervision.
