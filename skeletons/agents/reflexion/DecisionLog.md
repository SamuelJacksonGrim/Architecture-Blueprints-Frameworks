---
artifact: DecisionLog
status: complete
order: 99
fills: "the defining decision for this variant"
depends_on: []
filled_by: both
last_decision: null
---

# DecisionLog — Reflexion (delta)

> Inherits D-001..D-003 from the ReAct baseline. Adds:

### D-RX-1 — Turn failures into stored verbal lessons
- **Date:** 2026-06-15
- **Decided by:** both
- **Decision:** After each failed attempt, generate a natural-language critique
  and carry it into the next attempt's context.
- **Alternatives:** Just retry (blind repeat); fine-tune weights on failures
  (expensive, slow, not per-task).
- **Reason:** A verbal lesson is cheap, immediate, and steers the *next* attempt
  without touching the model. It's the smallest change that makes an agent
  improve within a single session.
- **Affects:** Flows; adds Evaluator + Reflector roles and a `lessons` memory.
