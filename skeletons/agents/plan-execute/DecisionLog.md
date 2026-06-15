---
artifact: DecisionLog
status: complete
order: 99
fills: "the defining decision for this variant"
depends_on: []
filled_by: both
last_decision: null
---

# DecisionLog — Plan-and-Execute (delta)

> Inherits D-001..D-003 from the ReAct baseline. Adds:

### D-PE-1 — Plan up front, replan on divergence
- **Date:** 2026-06-15
- **Decided by:** both
- **Decision:** Generate the full step list before executing; only re-invoke the
  Reasoner (as a Replanner) when an Observation shows the plan is off track.
- **Alternatives:** Re-decide every step (that's just ReAct); or never replan
  (brittle — any surprise breaks the run).
- **Reason:** Far fewer expensive Reasoner calls (~3.6× faster on long tasks),
  while the Replanner keeps it from shattering on the first surprise.
- **Affects:** Flows; adds Planner + Replanner roles to the baseline's Reasoner.
