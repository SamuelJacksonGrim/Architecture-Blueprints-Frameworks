---
artifact: DecisionLog
status: complete
order: 99
fills: "architectural memory — decisions, alternatives, reasons, dates"
depends_on: []
filled_by: both
last_decision: null
---

# DecisionLog — Agent

> Append-only architectural memory. Referenced by `last_decision` fields
> throughout this skeleton.

### D-001 — Flows before Contracts
- **Date:** 2026-06-15
- **Decided by:** both
- **Decision:** Build order is Architecture → Flows → Contracts.
- **Alternatives:** Contracts before Flows (the naive ordering).
- **Reason:** A contract constrains a behavior; you cannot write a meaningful
  guarantee for a flow you have not yet described. Inherited from `PIPELINE.md`.
- **Affects:** Flows, Contracts, the build pipeline.

### D-002 — Evaluator gate before every action
- **Date:** 2026-06-15
- **Decided by:** both
- **Decision:** No `Action` reaches the Executor without passing `Evaluator.pre`.
- **Alternatives:** Let the Planner execute directly; evaluate only afterwards.
- **Reason:** The Planner is assumed fallible (A2). A pre-execution gate is the
  cheapest place to stop harmful/invalid actions and is what makes G2/G4
  enforceable. Post-only evaluation cannot prevent side effects.
- **Affects:** Architecture (boundary), Flows (loop), Contracts (G2/G4), Interfaces.

### D-003 — Bounded loop for guaranteed termination
- **Date:** 2026-06-15
- **Decided by:** both
- **Decision:** The agent loop runs at most `MAX_STEPS`; exhaustion yields a
  `partial` Response.
- **Alternatives:** Unbounded loop until the goal is met.
- **Reason:** Termination must be a *guarantee* (G1), not a hope. Unbounded loops
  can't promise halting. A budget makes the worst case explicit and observable.
- **Affects:** Flows (loop), Contracts (G1/I1), Types (RunStatus.partial).
