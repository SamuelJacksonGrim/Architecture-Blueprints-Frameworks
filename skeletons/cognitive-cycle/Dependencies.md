---
artifact: Dependencies
status: complete
order: 8
fills: "allowed/forbidden dependency directions, hierarchy, import rules"
depends_on: [Modules, Interfaces]
filled_by: both
last_decision: D-002
---

# Dependencies — Autonomous Cognitive Loop

## Tier hierarchy (attachment order matters)
```
Tier 0  Substrate (working state, generator, self-monitor)
        ▲
Tier 1  Governance — the GOVERNOR (arbiter), policy, source trust
        ▲
Tier 2  Source integrity — validation, dependency checks, abuse resistance
        ▲
Tier 3  Preference learning
        ▲
Tier 4  Internal clock & metrics (terminal sink)
        ▲
Loop Coordinator  (runs all tiers in fixed sub-step order each tick)
```
> **Attachment order is load-bearing:** the Governor must be wired before any
> subsystem that subscribes to its decisions, or those subscriptions are silently
> missing.

## Allowed Directions
- Any tier → Types/Schemas.
- Advisory subsystems → the Governor (they hand it reports).
- Coordinator → all tiers, through their Interfaces.

## Forbidden Directions
- **Advisory subsystems ⇏ state.** They emit; they never mutate. (G1)
- **Loop ⇏ ClockInterface / metrics.** Terminal sinks are read-only downstream;
  a feedback edge here is the classic subtle bug. (G4, D-003)
- **No cycles** in the *module* graph (the *cognitive* loop is intentional; the
  module dependency graph stays acyclic).

## Import Rules
- Depend on interfaces, not implementations — so the generator, the state
  backend, and the memory store are all swappable.
