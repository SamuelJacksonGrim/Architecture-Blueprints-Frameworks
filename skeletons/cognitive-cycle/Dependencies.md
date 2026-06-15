---
artifact: Dependencies
status: complete
order: 8
fills: "allowed/forbidden dependency directions, hierarchy, import rules"
depends_on: [Modules, Interfaces]
filled_by: both
last_decision: D-002
---

# Dependencies — Cognitive Cycle

## Tier hierarchy (attachment order matters)
```
Tier 0  Substrate (field, generator, attention, watcher, witness, emotion)
        ▲
Tier 1  Selfhood — GOVERNANCE (the arbiter), trust, ethics
        ▲
Tier 2  Relational — rights, dependency, bonds, resistance
        ▲
Tier 3  Value emergence
        ▲
Tier 4  Subjective time (terminal sink)
        ▲
Cycle Coordinator  (runs all tiers in fixed sub-step order each tick)
```
> **Attachment order is load-bearing:** governance must be attached *before* the
> value engine, because the value engine subscribes to governance feedback at
> construction. Wrong order = silent missing subscription.

## Allowed Directions
- Any tier → Types/Schemas.
- Reporting subsystems → Governance (they hand it reports).
- Coordinator → all tiers, through their Interfaces.

## Forbidden Directions
- **Reporting subsystems ⇏ cognitive state.** They emit; they never mutate. (G1)
- **Loop ⇏ TemporalInterface / diagnostics.** Terminal sinks are read-only
  downstream; a feedback edge here is the classic subtle bug. (G4, D-003)
- **Anything ⇏ a symbol-registration shortcut.** All symbols go through the one
  canonicalization path; no bypass. (I3)
- **No cycles** in the dependency graph (the *cognitive* loop is intentional;
  the *module* graph stays acyclic).

## Import Rules
- Depend on interfaces, not implementations (swap the generator, the field
  backend, the memory store freely).
