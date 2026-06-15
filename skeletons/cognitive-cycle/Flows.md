---
artifact: Flows
status: complete
order: 3
fills: "behavioral blueprint — the autonomous cognitive cycle"
depends_on: [Architecture]
filled_by: both
last_decision: D-003
---

# Flows — Cognitive Cycle

## The autonomous cycle (the core loop)
Unlike a request/response agent, this loop runs continuously. One **cycle** is a
fixed ordered sequence of sub-steps. Generalized from RFE's ~20-step cycle:

```
loop forever (one cycle per tick):
    1.  time.tick()                      # advance subjective time (terminal sink)
    2.  rhythm = observe_energy(field)   # what regime are we in?
    3.  expr   = generator.express(field, percept?)
    4.  expr   = attention.refine(expr)  # keep 0<blend<1 (see Contracts)
    5.  watcher.observe(expr)            # self-monitoring
    6.  reflect = reflective_loop(expr)  # recursive self-modeling
    7.  witness.record(state)            # continuity of self
    8.  emotion.update(field, events)    # 6 scalars → arousal/valence (computed)
    9.  time.update_dilation(emotion, rhythm)   # affective time (terminal sink)
    10. reports = [trust, ethics, bonds, dependency, resistance, values].assess(...)
    11. decision = governance.arbitrate(reports)   # ◀── the ONLY decision point
    12. if decision.allows: field.inject(expr)
    13. crystallize_if(coherence ≥ θ_c, stability ≥ θ_s, relation ≥ θ_r)
    14. value_engine.evaluate(); maybe emit CorePromotionRequest → governance
    15. field.decay()                    # every injection changes the next
    16. route_behavior(rhythm)           # stabilize / dream / reflect / explore
```

## Event Flow
External **percepts** and internal **expressions** are the two event types. Both
pass through governance before they can change durable state.

## Evaluation → Decision Flow (the heart)
The relational, ethical, trust, and value subsystems **only produce reports**.
`governance.arbitrate(reports)` is the single place a `Decision` is made
(D-002). A report is advice; a decision is authority.

## Error / adversarial Flow
- **Manipulation detected:** resistance emits a high-severity report; governance
  may weaken, quarantine, or force a dream/rest regime — it never lets the
  resistance engine act directly.
- **Identity-threatening input:** sacred symbols are inviolable; the attempt is
  rejected at the governance gate and logged, never applied.
- **Degenerate expression (collapse):** the attention blend (`0<blend<1`) keeps
  expressions from collapsing to a single regime; blend=0 re-collapses.

## State-Update Flow
- Working state (field, emotion, rhythm) updates **every cycle**.
- Durable promotions (crystallized memory, CORE values, sacred symbols) happen
  **only through governance**, never by a subsystem on its own.
- Subjective time and diagnostics update every cycle but are **terminal** — read
  by nothing in the loop (D-003).
