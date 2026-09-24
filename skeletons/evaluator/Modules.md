---
artifact: Modules
status: complete
order: 8
fills: "modules"
depends_on: [Interfaces]
filled_by: both
last_decision: D-003
---

# Modules — Evaluator

| Module | Responsibility | Implements |
|--------|----------------|------------|
| RubricStore | catalog | RubricStoreInterface |
| SubjectAdapter | read-only view | SubjectViewInterface |
| Critic | notes | CriticInterface |
| Scorer | the score | ScorerInterface |
| Reporter | freeze output | — |
