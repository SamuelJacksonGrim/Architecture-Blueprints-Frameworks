---
artifact: Flows
status: complete
order: 3
fills: "behavioral blueprint — the autonomous loop"
depends_on: [Architecture]
filled_by: both
last_decision: D-003
---

# Flows — Autonomous Cognitive Loop

## The loop (the core behavior)
Unlike a request/response agent, this runs continuously. One **cycle** is a
fixed ordered sequence of sub-steps:

```
loop forever (one cycle per tick):
    1.  clock.tick()                       # advance the internal clock (terminal sink)
    2.  state.perceive(input?)             # fold in any new input
    3.  action = generator.propose(state)  # what would I do next?
    4.  self_monitor.observe(action)       # self-monitoring
    5.  metrics.update(state)              # health/coherence metrics (observe-only)
    6.  reports = [trust, validation, abuse_resistance, preferences].assess(state, action)
    7.  decision = governor.decide(reports)   # ◀── the ONLY decision point
    8.  if decision.allows: state.commit(action)
    9.  if consolidation_thresholds_met(state): memory.consolidate(candidate)
    10. preferences.evaluate(); maybe request promotion → governor
    11. state.age()                        # decay/forget so state stays bounded
    12. route_next_behavior(decision)
```

## Event Flow
External **input** and internally generated **actions** are the two event types.
Both pass through the Governor before they can change durable state.

## Evaluation → Decision Flow (the heart)
The trust, validation, abuse-resistance, and preference subsystems **only
produce reports**. `governor.decide(reports)` is the single place a decision is
made (D-002). A report is advice; a decision is authority.

## Error / adversarial Flow
- **Bad/abusive input detected:** the abuse-resistance subsystem raises a
  high-severity report; the Governor may reject, sandbox, or downgrade trust —
  it never lets that subsystem act directly.
- **Input that targets the protected core:** identity invariants are immutable;
  the attempt is rejected at the Governor and logged, never applied.
- **Degenerate action (collapse to one behavior):** a diversity check in the
  generator keeps the system from locking into a single repeated output.

## State-Update Flow
- Working state (perception, metrics) updates **every cycle**.
- Durable changes (consolidated memory, promoted preferences, protected-core
  edits) happen **only through the Governor**, never by a subsystem alone.
- The internal clock and metrics update every cycle but are **terminal** — read
  by nothing in the loop (D-003).
