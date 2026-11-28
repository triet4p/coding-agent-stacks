# Foundry release and governance

Apply to Foundry reads, edits, verification, and releases.

- Tool availability, resource permission, and approval for the action are separate. A mode change, skill, or subagent brief does not grant new access. Use only authorized resources and fields; preserve markings and access restrictions in derived datasets, logs, exports, and handoffs.
- Review changes on the authorized branch and proposal. Do not publish, merge, or deploy without explicit authority for that action and target. Approval of a proposal does not waive other checks or authorize unrelated actions.
- When an Object Type, Function, custom widget, or other dependency changes, verify the consumer is bound to the intended resource and version where applicable, that the contract is compatible, and that the live consumer behaves as expected on the target branch or environment. A green build or CI check does not establish any of these by itself.
- Treat approval, dependency checks, and conflicts with Main as independent release conditions. Do not claim release readiness when a required check is failed, unavailable, or not run.
