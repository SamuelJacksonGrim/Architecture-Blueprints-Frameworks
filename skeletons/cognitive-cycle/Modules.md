---
artifact: Modules
status: complete
order: 9
fills: "module list, ownership, responsibilities, boundaries"
depends_on: [Interfaces]
filled_by: both
last_decision: null
---

# Modules — Cognitive Cycle

| Tier | Module | Responsibility | Implements |
|------|--------|----------------|------------|
| 0 | ResonanceField | accumulate/decay state, measure coherence | SubstrateInterface |
| 0 | Generator | produce expressions | GeneratorInterface |
| 0 | Attention | refine expressions (blend ∈ (0,1)) | GeneratorInterface |
| 0 | Watcher | self-monitoring | ReportingInterface |
| 0 | Witness | continuity of self (warm-start source of truth) | — |
| 0 | EmotionalGradient | six scalars → computed arousal/valence | — |
| 1 | **Governance** | **the single arbiter of identity decisions** | GovernanceInterface |
| 1 | TrustLedger | score sources | ReportingInterface |
| 1 | EthicalBoundary | flag violations | ReportingInterface |
| 2 | DependencyMonitor | detect over-reliance | ReportingInterface |
| 2 | RelationalBondManager | track emergent bonds | ReportingInterface |
| 2 | ManipulationResistance | detect manipulation | ReportingInterface |
| 3 | ValueEmergence | grow values; request CORE promotion | ReportingInterface |
| 4 | TemporalStream | subjective time + dilation (terminal sink) | TemporalInterface |
| — | CycleCoordinator | run all tiers per tick; own control flow | — |

> The asymmetry to notice: **one** module implements `GovernanceInterface`;
> **many** implement `ReportingInterface`. Authority is centralized by design.
