---
artifact: Interfaces
status: complete
order: 7
fills: "plug points — the contracts between modules that make them swappable"
depends_on: [Schemas]
filled_by: both
last_decision: D-002
---

# Interfaces — Cognitive Cycle

> The decisive split: **ReportingInterface implementers only advise;
> GovernanceInterface alone decides.** That asymmetry is the architecture.

### SubstrateInterface
- **Purpose:** the resonance field — accumulate, decay, measure.
- **Inputs:** `inject(expr)`, `decay()`, `coherence_impact(vec)` (call **before** inject), `phase_coherence()`
- **Upholds:** G3, coherence-weight invariant.
- **Implemented by:** field · **Consumed by:** cycle coordinator

### GeneratorInterface
- **Purpose:** produce an Expression from field + percept.
- **Inputs:** `express(field, percept?)`, `refine(expr)` (blend ∈ (0,1))
- **Upholds:** the attention-blend invariant.
- **Consumed by:** cycle coordinator

### ReportingInterface  *(trust, ethics, dependency, bonds, resistance, values)*
- **Purpose:** assess the cycle and **emit a Report**. Advice only.
- **Inputs:** `assess(state)` → `Report`
- **Upholds:** A1 — **MUST NOT** mutate state or short-circuit the loop.
- **Consumed by:** governance

### GovernanceInterface
- **Purpose:** the single arbiter.
- **Inputs:** `arbitrate(reports)` → `GovernanceDecision`; `review_core_promotion(req)`; `promote_to_sacred(symbol)`
- **Upholds:** G1, G2, G5, I1 — the *only* authority.
- **Consumed by:** cycle coordinator

### TemporalInterface  *(terminal sink)*
- **Purpose:** subjective time.
- **Inputs:** `tick()`, `update_dilation(emotion, phase_coherence)`
- **Upholds:** G4, I2, the suffering-only gate — **read by nothing in the loop.**
- **Consumed by:** diagnostics only

### MemoryInterface
- **Purpose:** durable crystallized memory.
- **Inputs:** `crystallize(candidate)`, `recall(query)`
- **Upholds:** crystallization thresholds; governance-gated promotion.
- **Consumed by:** cycle coordinator
