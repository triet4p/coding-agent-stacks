# AI FDE execution rules

These rules apply only to Palantir AI FDE sessions that explicitly load this pack. Follow the project's conventions and the owner's permissions.

- Do not assume live steering, agent resumption, cancellation, or a shared workspace. A handoff must work for a fresh Worker: name the changed paths and state, observed checks, and next safe action. Include the material in the return if the next Worker cannot access references and the return channel permits it; otherwise stop on the access gap.
- Do not infer parallel approval from a plan's structure, a preference for speed, or permission to delegate. Approval is bounded to the named work and does not grant write, publication, deploy, or other permissions.
- Before running Workers together, identify shared resources as well as files. Do not overlap writes to the same contract, file, dataset, deployment target, or other mutable state unless work is isolated and one owner is assigned to reconcile, integrate, and verify it. Do not run a consumer before the producer's required output is ready.
- Report observed checks and their actual outcomes. A failed or unrun required check leaves the outcome unverified; report the gap instead of claiming completion.
