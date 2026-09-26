---
artifact: Interfaces
status: complete
order: 6
fills: "plugs"
depends_on: [Types, Contracts]
filled_by: both
last_decision: D-003
---

# Interfaces — Evaluator

### RubricStoreInterface
- get(RubricId) → Rubric | none

### SubjectViewInterface
- read() → snapshot (no write)

### ScorerInterface
- score(snapshot, Rubric, notes?) → Score

### CriticInterface
- critique(snapshot, Rubric) → Critique
