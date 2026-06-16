---
artifact: Modules
status: complete
order: 9
fills: "module list, ownership, responsibilities, boundaries"
depends_on: [Interfaces]
filled_by: both
last_decision: null
---

# Modules — Autonomous Cognitive Loop

| Tier | Module | Responsibility | Implements |
|------|--------|----------------|------------|
| 0 | WorkingState | hold/age state, expose metrics | StateInterface |
| 0 | Generator | propose actions (with a no-collapse check) | GeneratorInterface |
| 0 | SelfMonitor | self-observation; continuity record | — |
| 1 | **Governor** | **the single arbiter of identity decisions** | GovernorInterface |
| 1 | SourceTrust | score input sources | ReportingInterface |
| 1 | Policy | encode hard limits / protected core | — |
| 2 | InputValidation | structural validation/sanitization | ReportingInterface |
| 2 | DependencyMonitor | detect over-reliance on one source | ReportingInterface |
| 2 | AbuseResistance | detect manipulation/abuse | ReportingInterface |
| 3 | PreferenceLearning | grow preferences; request promotion | ReportingInterface |
| 4 | Clock | internal clock + metrics (terminal sink) | ClockInterface |
| — | LoopCoordinator | run all tiers per tick; own control flow | — |

> The asymmetry to notice: **one** module implements `GovernorInterface`;
> **many** implement `ReportingInterface`. Authority is centralized by design.
