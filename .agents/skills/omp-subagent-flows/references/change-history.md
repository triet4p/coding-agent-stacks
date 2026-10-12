# OMP Subagent Flows Change History

Earlier entries are historical, not current dispatch policy. The 2026-10-11 contract supersedes conflicting Silver-default, uncertain-to-Gold, and universal review/checkpoint/deep-review rules.

- **2026-10-03:** Allowed bounded, evidence-backed diagnostic requests before repeated failures; generalized evidence-root selection to the active plan or assignment.
- **2026-10-05:** Introduced dedicated Bronze/Silver/Gold roles, initially with Silver-default routing and pinned selectors.
- **2026-10-05:** Removed fixed selectors from skills; model/effort comes from effective named-agent definitions.
- **2026-10-05:** Expanded Gold eligibility to medium work and moved attempt lifetime to Main, with progress/attempt reassessment rather than prompt-level budget stops.
- **2026-10-05:** Required detailed replacement handoffs, prior-attempt references, and explicitly authorized successor history reads.
- **2026-10-11:** Added ask-based routing with scoped user authority, no implicit medal default, light execution with optional binding review and explicitly authorized own-scope worker commits, and full execution with Bronze-only exact-snapshot checkpoints at agreed boundaries and conditional deep review. Plans hold stable scope/status, not turn logs; handoffs and temporary state are separate files under the assigned repository's `artifacts/`. Preserved async matching, timer/advisor safety, Main-owned continuation, mandatory replacement handoff/history, and Git ownership safeguards. Supersedes conflicting earlier routing/gate rules.
- **2026-10-11:** Replaced model/selector/effort recording with role-only subagent reporting across asks, briefs, chat, and durable records. Prioritize applicable user overrides over agent defaults; never mask them with cached/per-call selectors or silently fall back.
- **2026-10-11:** Enforced strict minimal context boundaries and pointer delegation for the Main session, eliminating preflight reads of subagent prompt bodies, worker execution skills, codebase files, and past sprint plans; modularized optional protocols (Git checkpoint safety, task advisor, replacement handoff) into `references/`.
