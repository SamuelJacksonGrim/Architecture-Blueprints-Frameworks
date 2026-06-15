---
artifact: DecisionLog
status: complete
order: 99
fills: "architectural memory — decisions, alternatives, reasons, dates"
depends_on: []
filled_by: both
last_decision: null
---

# DecisionLog — ReAct Agent

### D-001 — Flows before Contracts
- **Date:** 2026-06-15
- **Decided by:** both
- **Decision:** Build order Architecture → Flows → Contracts.
- **Alternatives:** Contracts before Flows.
- **Reason:** A contract constrains a behavior; describe the behavior first.
  Inherited from `PIPELINE.md`.
- **Affects:** Flows, Contracts.

### D-002 — ReAct as the family baseline
- **Date:** 2026-06-15
- **Decided by:** both
- **Decision:** The plain think→act→observe loop is the reference agent; the
  other patterns (Plan-Execute, Reflexion, Tree-of-Thoughts) are documented as
  deltas on top of it.
- **Alternatives:** Lead with a safety-gated / plan-then-execute design.
- **Reason:** The web's clear 2026 consensus: start with the simplest pattern
  that works and only add structure when a failure mode demands it. ReAct is the
  most common, most debuggable starting point, so it's the one to learn first.
- **Affects:** the whole `skeletons/agents/` family layout.

### D-003 — Reasoner owns termination; MAX_STEPS is a backstop
- **Date:** 2026-06-15
- **Decided by:** both
- **Decision:** The loop ends when the Reasoner emits a Final Answer; a step
  budget only exists to guarantee halting.
- **Alternatives:** Fixed step count; external controller decides when done.
- **Reason:** ReAct's whole idea is letting the model judge when it has enough.
  The budget is insurance (G1), not the primary stop condition.
- **Affects:** Flows, Contracts (G1/I1), Types (RunStatus).
