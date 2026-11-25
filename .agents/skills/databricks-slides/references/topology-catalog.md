# Topology Catalog

Choose the topology from the **relationship the slide teaches**, never from the shape of the data ("three columns → three cards"). This catalog comes from 15 delivered decks (453 slides) where repeated cards and tables were the main reason decks read like a policy handbook instead of a technical course.

## Selection procedure

1. Write one sentence: what must the learner see that a paragraph cannot say?
2. Match it to a row below.
3. Check the "avoid when" column — if it fires, choose the neighbouring row.
4. Read the geometry trap before implementing.

## Catalog

| Relationship | Topology | Use when | Avoid when | Geometry trap |
|---|---|---|---|---|
| Ordered steps | `flow` | A real sequence with a direction: ingest → clean → serve | Alternatives, parallel tracks, two-way sync | Arrows always imply order; pass `arrows=False` for alternatives |
| Choice with trade-offs | `concept_decision` | 2–3 options, each with a cost | Linear sequence | More than 3 options; decision strip missing |
| Before / after | `before_after` | A state change with a cause | Side-by-side comparison of independent options | Both halves must share identical row heights |
| Failure and repair | `repair_state` | A run fails, then is repaired/reused | Generic pipeline | Legend placed at fixed y collides with the decision strip |
| Layered boundaries | `connector_layers` | Trust/compute/storage planes, connector boundaries | Flat lists | Note stack on the right must not exceed 2 cards |
| Architecture bands | `architecture` | 3–4 horizontal bands with ownership | More than 4 bands | Band labels must not sit inside the boundary line |
| Nested hierarchy | `uc_hierarchy`, `nested_containment` | Ownership, catalog/schema/table, privilege inheritance | Independent options | Inner ring needs ≥0.52 in of band width before a sub-label fits |
| Snapshot → log | `cdc_state` | Two-phase ingestion or change capture | Single-phase flow | Note panel below the second phase collides with the footer |
| Branching | `branch_state` | True/false, pass/fail, condition → two paths | Three or more branches | Join node collides with the decision strip |
| Load over time | `capacity_curve` | Autoscaling, concurrency, queueing | Categorical comparison | `y = 0` is the top of the plot (fast start); do not invert |
| Idle timeline | `idle_timeline` | Auto-stop, warm pool, cold start | Non-temporal data | Segment labels need ≥0.55 in height |
| Cost × latency | `cost_latency_map` | Four levers with trade-offs | Ordered steps | Cards 1.72 × 0.80 in, stepped diagonally; drop quadrant corner labels |
| Priority order | `preference_ladder` | WIF → service principal → secret; fallback order | Equal options | Bar height ≤1.04 in; taller only adds whitespace |
| Cost / fidelity / frequency | `test_pyramid` | Test levels, data quality tiers | Flat list of test types | TRAPEZOID: `w_top = widths[i-1]` (previous band), never `widths[i+1]` |
| Common misconception | `myth_rows` | Myth → reality → consequence | Neutral comparison | Maximum 3 rows; row 2 is the longest in practice |
| Defence in depth | `security_rings` | PrivateLink → IP list → CMK → data | Parallel controls | Sub-labels only when the ring is ≥0.52 in thick |
| Version → artifact → rollback | `version_lineage` | Commit SHA → bundle → deployment | Simple pipeline | Fan-in of more than 4 sources becomes unreadable |
| Code → graph → plan | `dag_triad` | Spark/DLT execution explanation | Non-code topics | Three columns only; a fourth breaks the reading order |
| Ecosystem | `hub` | One centre, many integrations | Sequential steps | Spokes must not cross; keep ≤6 |
| Screenshot + annotations | `ui_evidence` | UI proof with 1–3 numbered badges | Decorative image | Badge coordinates come from the image box, not the frame |
| Wide screenshot | `ui_banner` | Wide UI strip with callouts below | Tall screenshots | Aspect >3.5 requires a decision strip to close the slide |

## Combining topologies

- A slide has **one** primary topology. Secondary elements (a small table, a legend) are support, not a second diagram.
- If you need two topologies, split the slide.
- A hero diagram per section may use a richer topology; the rest of the section should use lighter ones (flow, table, decision).

## Anti-patterns

- `flow` with `arrows` for alternatives → implies a false sequence.
- Four cards where the content is a trade-off → use `cost_latency_map` or `concept_decision`.
- A table of hierarchy rows → use `uc_hierarchy` / `nested_containment`.
- A table of lifecycle stages → use `version_lineage` or `cdc_state`.
- Six equal cards with no relationships → `hub` or `tiles_2x2`.
- A screenshot used as background texture → delete it.

## Implementation notes

- Reference implementations: `assets/deckkit_starter.py` (primitives) and `assets/example-*.png` (approved output).
- Keep every node label ≤ 4 words. Long labels belong in the rail callouts or notes.
- Connectors: orthogonal, 1.25 pt, `#D7DDE3`; red only for the accent path or a blocked link.
- Blocked links: dashed connector + small × marker; explain the cause in the decision strip.
