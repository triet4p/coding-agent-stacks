# Task Result: <Task ID>

**Sprint:** <Sprint ID>  
**Task and acceptance criterion:** <Task ID and concise criterion>  
**Attempt:** <current attempt ID>
**Review cycle / round:** <assigned cycle ID and round; round 3 needs Main's authorization reference; omit without evidence gate>
**Criterion reference:** <current agreed requirements and any explicit owner-approved revision>

## Worker Result

*Worker-owned information only. Main does not fill or transcribe this record.*

### Route

- **Workflow and required gates:** `light` / `full`; <only the assigned review/checkpoint/deep-review and commit boundary, or `None`>
- **Task family and assignment basis:** <dispatch-known family/history and the user's selected role or scoped routing authority>
- **Assigned role/tier:** `bronze-task` / `silver-task` / `gold-task`; corresponding tier
- **Selection reason:** <concise fit to this task>
- **Relevant history refs:** <compact exact refs or `None`; never invent references>
- **Quota/cost observation:** <observed or `unknown`; no fixed assumptions>

*Report the subagent role and work IDs only; never include model/provider names, selectors or effort values, including copied metadata from earlier histories.*

### Outcome

- **Status:** `ready_for_review` / `implementation_complete` / `partial` / `blocked`
- **Observable result:** <what changed and what the evidence actually shows>
- **Remaining criteria/blocker:** <none, or concise concrete detail>
- **Changed files:** <paths and reasons>

### Verification

- **Command or scenario and observed result:** <exactly what was run/observed, or `Not run` with the assignment reason>
- **Regression test:** <actual result, or why no permanent test was warranted / was not assigned>
- **Limitations:** <concrete evidence gap or `None`; documentation/workflow checks are instruction cross-reference checks, not invented automated tests>
- **Targets versus observations:** <for numeric criteria: target, observed result and measurement conditions; distinguish unmet requirements from proposed targets>

### Commit Status

- **Authorization:** <not authorized / not applicable / exact assigned permission>
- **Result:** <not attempted / exact observed outcome; identify only the worker's verified scope and commit if authorized>

### Assigned Gate References

*Omit this section when no review or checkpoint was assigned. Do not copy another role's evidence into this worker-owned record.*

- **Evidence review:** <assigned or not assigned; if assigned, reviewer-owned report path and verdict>
- **Frozen-snapshot manifest:** <required only when a full-route checkpoint is planned; reviewer-owned manifest path, otherwise `Not required`>
- **Full-route checkpoint:** <assigned or not planned; if assigned, executor-owned record path and observed status>
- **Round outcomes / continuation:** <reviewer-owned outcomes, Main's round-3 authorization if granted, or owner decision required; approval reference for changed criteria or further cycles>

### Separate Handoff File

*When paused or replaced: link the separate handoff file saved under `artifacts/`.*

- **Handoff path:** <path or `None`>

## Record Ownership

This worker record is not an independent review, frozen-snapshot manifest, checkpoint record, or commit authorization. Reviewer and checkpoint records are written separately by their assigned owners.
