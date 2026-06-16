---
artifact: Interfaces
status: complete
order: 7
fills: "plug points — the contracts between modules that make them swappable"
depends_on: [Schemas]
filled_by: both
last_decision: D-002
---

# Interfaces — Autonomous Cognitive Loop

> The decisive split: **ReportingInterface implementers only advise; the
> GovernorInterface alone decides.** That asymmetry is the architecture.

### StateInterface
- **Purpose:** the working state — perceive, commit, age, measure.
- **Inputs:** `perceive(input)`, `commit(action)`, `age()`, `metric(name)`
- **Upholds:** G3, the composite-metric weight invariant.
- **Consumed by:** loop coordinator

### GeneratorInterface
- **Purpose:** propose the next action from current state.
- **Inputs:** `propose(state)`
- **Upholds:** the no-collapse (diversity) check.
- **Consumed by:** loop coordinator

### ReportingInterface  *(trust, validation, abuse-resistance, preferences)*
- **Purpose:** assess the cycle and **emit a Report**. Advice only.
- **Inputs:** `assess(state, action)` → `Report`
- **Upholds:** A1 — **MUST NOT** mutate state or short-circuit the loop.
- **Consumed by:** the Governor

### GovernorInterface
- **Purpose:** the single arbiter.
- **Inputs:** `decide(reports)` → `Decision`; `review_promotion(req)`; `edit_protected_core(req)`
- **Upholds:** G1, G2, G5, I1 — the *only* authority.
- **Consumed by:** loop coordinator

### ClockInterface  *(terminal sink)*
- **Purpose:** the internal clock + health metrics.
- **Inputs:** `tick()`, `update_metrics(state)`
- **Upholds:** G4, I2 — **read by nothing in the loop.**
- **Consumed by:** diagnostics only

### MemoryInterface
- **Purpose:** durable consolidated memory.
- **Inputs:** `consolidate(candidate)`, `recall(query)`
- **Upholds:** consolidation thresholds; Governor-gated promotion.
- **Consumed by:** loop coordinator
