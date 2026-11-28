# Foundry metric contracts

Apply when defining, calculating, or consuming a business metric.

- Give each KPI one canonical definition and a named owner or authoritative source. Record its grain, population and filter scope, formula (including numerator and denominator when relevant), event date and time basis, and rules for missing data, fallbacks, exclusions, and zero denominators.
- Workshop, Functions, exports, and pipelines must consume or implement the same contract for the same named KPI. If the business needs two different definitions, give them distinct names. Do not silently change which date or population qualifies.
- Aggregate according to the definition. For a population ratio, compute it from the correct numerator and denominator at the requested grain and scope; do not average precomputed subgroup ratios as a substitute. Check joins for row multiplication before aggregating.
