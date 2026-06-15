---
artifact: Contracts
status: complete
order: 4
fills: "guarantees, assumptions, invariants, pre/post-conditions"
depends_on: [Architecture, Flows]
filled_by: both
last_decision: D-002
---

# Contracts — Agent

## Guarantees
- **G1 — Termination.** Every run halts in at most `MAX_STEPS` (D-003).
- **G2 — Evaluation gate.** No `Action` reaches the Executor without a passing
  `Evaluator.pre` verdict (D-002).
- **G3 — Memory integrity.** Long-term memory only ever contains observations
  that passed `Evaluator.post`.
- **G4 — Bounded blast radius.** All world side-effects happen inside the
  Executor; the rest of the system is pure with respect to the outside world.

## Assumptions
- **A1** — Tools are addressable by a stable `ToolId` and honor their declared
  `Interface`.
- **A2** — The Planner is *fallible*: it may propose invalid or harmful actions.
  (This is *why* G2 exists.)
- **A3** — Tool results are *untrusted* until validated by `Evaluator.post`.

## Invariants
- **I1** — `step ≤ MAX_STEPS` at all times.
- **I2** — Working memory is a superset of long-term memory for the current run.
- **I3** — Exactly one of {proceed, retry, replan, terminate} holds per loop step.

## Pre/Post-Conditions
| Operation | Pre | Post |
|-----------|-----|------|
| `Planner.next` | goal valid, context loaded | returns a well-formed `Plan` or signals `no_plan` |
| `Evaluator.pre` | plan well-formed | returns a `Verdict`; no side effects |
| `Executor.run` | verdict == proceed | returns a `ToolResult` (ok or error), never throws |
| `Memory.write` | record validated for tier | record persisted in correct tier |
