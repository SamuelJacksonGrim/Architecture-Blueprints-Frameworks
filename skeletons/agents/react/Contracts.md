---
artifact: Contracts
status: complete
order: 4
fills: "guarantees, assumptions, invariants, pre/post-conditions"
depends_on: [Architecture, Flows]
filled_by: both
last_decision: D-002
---

# Contracts — ReAct Agent

## Guarantees
- **G1 — Termination.** The loop halts in at most `MAX_STEPS` (or sooner, when
  the Reasoner emits a Final Answer).
- **G2 — Bounded blast radius.** All outside-world effects happen inside the
  Executor; the rest of the agent is read/think only.
- **G3 — Transparent trace.** Every step is recorded in the scratchpad, so any
  run can be replayed and inspected. (This is *the* reason ReAct is the popular
  default — it's easy to debug.)

## Assumptions
- **A1** — Tools honor their declared input/output shape.
- **A2** — The Reasoner is fallible: it may pick a wrong or useless action. ReAct
  tolerates this because a bad step just becomes an Observation it can correct.
- **A3** — Tool results are untrusted until the Reasoner has interpreted them.

## Invariants
- **I1** — `step ≤ MAX_STEPS` at all times.
- **I2** — The scratchpad only grows within a run (append-only).
- **I3** — Each loop turn produces exactly one Thought, and at most one Action.

## Pre/Post-Conditions
| Operation | Pre | Post |
|-----------|-----|------|
| `Reasoner.think` | goal + scratchpad available | returns Thought+Action **or** Final Answer |
| `Executor.run` | action references a known tool | returns an Observation; never throws |
