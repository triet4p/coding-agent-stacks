# Task Summary: <Task ID>

**Sprint:** <Sprint ID>  
**Task:** <Task ID and acceptance criterion>  
**Attempt(s):** <current attempt ID and any superseded attempts>

## Worker Handoff

*Worker-owned evidence only. Main does not fill or transcribe this artifact.*

### Scope

- **Classification:** `PROJECT-BACKED` / `EXPLICIT NON-PROJECT`
- **Assigned project repository/worktree/ref, or non-project assignment reference:** <explicit values; never infer from the current directory>
- **Evidence root:** <absolute path from the active plan or assignment>

### Task Routing

- **Task family:** <family used for calibration>
- **Exact role:** `bronze-task` / `silver-task` / `gold-task` (explicit flow role; the obsolete `task`/`hard-task` agent roles are not valid here, and the bundled OMP generic `task` tool is outside this flow)
- **Tier:** `Bronze` / `Silver` / `Gold` (pinned to the exact role above: Bronze `opencode-go/mimo-v2.6-flash:high`; Silver `openai-codex/gpt-6-luna:xhigh`; Gold `opencode-go/muse-spark-1.3-contributor:high`)
- **Exact resolved selector/effort:** <Main-assigned per-call selector for the exact role above>
- **Selection reason:** <why this role/tier fits this family/reasoning need>
- **Relevant historical refs:** <compact refs if any, else `None`; never invent session history>
- **Quota observation:** <observation, or `unknown`; never fabricate quota mechanics>
- **Meaningful progress/blocker:** <concise status>

### Outcome

<Observable behavior delivered; what changed for its consumer.>

### Files Changed

- `<path>` — <reason>

Record routing metadata in this normal artifact only; add no new telemetry, cooldowns, counters, or enforced numeric budgets.

### Verification

- **Command or scenario:** `<exact command>` / <manual steps>
- **Observed result:** <actual output or behavior>
- **Regression test:** <test and result, or why no permanent test was warranted>
- **Limitations:** <unavailable runtime or other evidence limit, or `None`. Verification for a documentation or workflow-only task is an instruction cross-reference check, not an invented automated test.>

### Advisor Consultation Evidence

<None, or bounded task/attempt/consultation IDs, question, blocker, evidence, tried hypotheses/results, diagnostic conclusion, worker action and observed result. If a GPT-6.1 Sol override was used, include the exact model/effort and a reference to explicit approval scoped to this consultation. A bounded request may precede repeated failures when genuinely new discriminating evidence is unavailable; elapsed time or attempt/file counts alone never justify a request. Do not include full prompts, transcripts, or trajectories.>

### Open Findings

<None, or concrete unresolved finding/blocker. Do not label an unverified task complete. Record early uncertainty with no new discriminating evidence here when it required a qualified advisor request, not a tier escalation.>

## Record Ownership

The matching evidence reviewer writes its own report under `<evidence-root>/artifacts/sprint-<N>/reviews/`; a fresh checkpoint-only executor writes its own checkpoint record under `<evidence-root>/artifacts/sprint-<N>/checkpoints/`. Main edits only the plan/status and concise links or summaries to these records. This worker artifact is not review approval, checkpoint evidence, or a commit authorization.
