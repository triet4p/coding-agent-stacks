---
name: foundry-release-review
description: Diagnose Foundry Global Branching proposal checks and verify dependency versions, conflicts, and live consumer behavior before release.
---

# Foundry release review

Follow [release and governance](../../rules/release-and-governance.md). Use when reviewing a proposal or release candidate. Diagnosing or reporting a check does not authorize changing it.

1. **Identify the proposal.** Record target and source branch, changed Foundry resources, dependencies, and which required checks are actually passing, failing, or unavailable. Inspect the exact failure before editing code, bindings, or branch state.
2. **Fix the correct layer when authorized.**
   - **Custom widget version:** inspect which release the module pins. Select an existing allowed release for that proposal and check parameters, events, and bindings. Do not republish source when only the module pin is wrong.
   - **Function version:** identify the consuming variable or widget and its version or range. Compare against the permitted branch/Main version for that proposal; check input/output compatibility. Update the binding if that is the fault, not a healthy Function implementation.
   - **Conflict with Main:** review both sides, decide the intended final configuration, and use the platform's Review/Rebase workflow if authorized. Review the resulting diff and rerun affected dependency checks. Updating a version is not rebasing; rebasing does not make a missing release exist.
3. **Check the candidate and consumer.** Recheck required proposal gates. Confirm the actual resource/version and exercise the consumer on the intended target candidate; use [Workshop verification](../foundry-workshop-verification/SKILL.md) for affected UI behavior. Do not equate approval, a saved configuration, successful build, or green CI with consumer verification.

Return: proposal and branch, individual check results, changed dependency refs, live consumer scenario and observed result, and any action still requiring approval or verification. Do not claim merge or deployment without evidence that it happened.
