# Task Result: <Task ID>

**Sprint:** <Sprint ID>  
**Task and acceptance criterion:** <Task ID and concise criterion>  
**Attempt:** <current attempt ID>

## Worker Result

*Worker-owned information only. Main does not fill or transcribe this record.*

### Route

- **Workflow and required gates:** `light` / `full`; <only the assigned review/checkpoint/deep-review and commit boundary, or `None`>
- **Task family and assignment basis:** <dispatch-known family/history and the user's selected role or scoped routing authority>
- **Assigned role/tier:** `bronze-task` / `silver-task` / `gold-task`; corresponding tier
- **Configured effective selector/effort:** <effective role-definition value if observed, otherwise `unknown`>
- **Actual runtime selector/effort:** <observed value if available, otherwise `unknown`; never present the configured value as observed runtime>
- **Selection reason:** <concise fit to this task>
- **Relevant history refs:** <compact exact refs or `None`; never invent references>
- **Quota/cost observation:** <observed or `unknown`; no fixed assumptions>

### Outcome

- **Status:** `implementation_complete` / `partial` / `blocked`
- **Observable result:** <what changed and what the evidence actually shows>
- **Remaining criteria/blocker:** <none, or concise concrete detail>
- **Changed files:** <paths and reasons>

### Verification

- **Command or scenario and observed result:** <exactly what was run/observed, or `Not run` with the assignment reason>
- **Regression test:** <actual result, or why no permanent test was warranted / was not assigned>
- **Limitations:** <concrete evidence gap or `None`; documentation/workflow checks are instruction cross-reference checks, not invented automated tests>

### Commit Status

- **Authorization:** <not authorized / not applicable / exact assigned permission>
- **Result:** <not attempted / exact observed outcome; identify only the worker's verified scope and commit if authorized>

### Assigned Gate References

*Omit this section when no review or checkpoint was assigned. Do not copy another role's evidence into this worker-owned record.*

- **Evidence review:** <assigned or not assigned; if assigned, reviewer-owned report path and verdict>
- **Frozen-snapshot manifest:** <required only when a full-route checkpoint is planned; reviewer-owned manifest path, otherwise `Not required`>
- **Full-route checkpoint:** <assigned or not planned; if assigned, executor-owned record path and observed status>

### Separate Handoff File

*Only when paused or replaced: save detailed attempt-scoped handoff state in a separate file under the assigned project's `artifacts/` directory (or explicit non-project output root), and link it here. Never put the handoff section or temporary supervision log in this task summary or a sprint plan. Main owns separate supervision-state files.*

- **Handoff path:** <path or `None`>

## Record Ownership

This worker record is not an independent review, frozen-snapshot manifest, checkpoint record, or commit authorization. Reviewer and checkpoint records are written separately by their assigned owners.
