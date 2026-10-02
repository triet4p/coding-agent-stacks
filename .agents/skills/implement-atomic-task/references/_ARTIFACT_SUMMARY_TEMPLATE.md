# Task Summary: <Task ID>

**Sprint:** <Sprint ID>  
**Task:** <Task ID and acceptance criterion>

## Worker Handoff

*Worker-owned fields; workers do not fill the Main-owned sections below.*

### Outcome
<Observable behavior delivered; what changed for its consumer.>

### Files Changed

- `<path>` — <reason>

### Verification

- **Command or scenario:** `<exact command>` / <manual steps>
- **Observed result:** <actual output or behavior>
- **Regression test:** <test and result, or why no permanent test was warranted>

### Advisor Consultation Evidence
<None, or bounded task/attempt/consultation IDs, question, diagnostic conclusion, worker action and observed result; if a GPT-6.1 Sol override was used, include its exact model/effort and a reference to the explicit approval for that consultation. Do not include full prompts, transcripts, or trajectories.>

### Open Findings
<None, or concrete unresolved finding/blocker. Do not label an unverified task complete.>

## Main-Owned Evidence Gate

*Main completes this section after the matching read-only review has finished.*

- **Verdict:** `PENDING` / `PASS` / `FAIL`
- **Review report/reference:** <artifact or event reference>
- **Reviewed snapshot:** <base SHA and approved tree/diff hash and scope>

## Main-Owned Project Commit Checkpoint

*Main completes this section; a worker artifact is not approval or commit evidence.*

- **State:** `PENDING` / `COMMIT_PENDING` / `COMMITTED` / `NOT_A_PROJECT_COMMIT — EXTERNAL GLOBAL CONFIGURATION ROLLOUT ONLY`
- **Target repository/ref:** <explicit assigned repository and target ref, or exact repository blocker>
- **Base and reviewed snapshot:** <base SHA; approved tree/diff hash and scope>
- **Commit:** <successful SHA, or exact failure and retry status>
- **Post-commit verification:** <expected parent/ref and committed snapshot check; `git diff --cached` and status showing only intended remaining user-staged changes and no task-path reversion>

For an actual project task without an assigned/authorized repository, use `COMMIT_PENDING` and record the blocker; do not use the global-configuration exception. Never infer a target from the current directory or commit an ancestor/home repository. Keep this artifact outside project commits.
