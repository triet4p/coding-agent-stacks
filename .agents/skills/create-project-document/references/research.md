# Research and Rationale

Optional reading: public examples of documentation choices, not templates to clone. The skill does not require these projects, frameworks or visual identities.

| Evidence | Borrow | Avoid |
|---|---|---|
| [LeRobot landing](https://huggingface.co/docs/lerobot/index), [imitation-learning tutorial](https://huggingface.co/docs/lerobot/il_robots), [installation](https://huggingface.co/docs/lerobot/installation) | Show a real artifact before setup. Make one end-to-end scenario the spine. Use tabs for variants of the same step (`conda`/`uv`). | Duplicate the tutorial across every variant page; bury prerequisite differences behind a tab. |
| [OMP overview](https://omp.sh/docs), [quickstart](https://omp.sh/docs/quickstart), [RPC](https://omp.sh/docs/rpc) | Keep navigation grouped and shallow. Finish onboarding at an observable outcome. Introduce comparable interfaces with a choice table, then give pasteable commands or events. | Make a long reference searchable only by route; replace selectable examples with screenshots. |
| [Foundry Architecture Center](https://www.palantir.com/docs/foundry/architecture-center/overview/), [AIP Architecture](https://www.palantir.com/docs/foundry/architecture-center/aip-architecture/), [Flow Capture](https://www.palantir.com/docs/foundry/flow-capture/generate-documentation/) | Give distinct architectural views distinct jobs. Capture a real workflow first; curate assets and review the rendered result before publishing. | Copy enterprise navigation depth or mistake an illustrative system map for a runtime trace. |

The [Foundry entry](https://www.palantir.com/docs/foundry/) separates capabilities, getting started, architecture and API lookup. The [Pipeline Builder overview](https://www.palantir.com/docs/foundry/pipeline-builder/overview/) leads to concepts and specific tasks. The [batch-pipeline tutorial](https://www.palantir.com/docs/foundry/building-pipelines/create-batch-pipeline-pb/) carries named inputs and an output through detailed stages, exact controls and screenshots. Borrow the separation and depth, not the brand or size of its navigation tree.

[Diátaxis](https://diataxis.fr/) helps distinguish tutorials, how-tos, explanations and reference **within** the reader paths. [C4](https://c4model.com/diagrams) provides levels of zoom for architecture; use only the views that answer real questions.
