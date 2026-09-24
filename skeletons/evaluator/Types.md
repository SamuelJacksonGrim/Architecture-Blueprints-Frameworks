---
artifact: Types
status: complete
order: 4
fills: "Rubric, Score, Critique"
depends_on: [Contracts]
filled_by: both
last_decision: D-002
---

# Types — Evaluator

- `RubricId`, `CriterionId`
- `Criterion` — id, weight, description
- `Rubric` — id, criteria[], threshold
- `Score` — value in [0,1], pass: bool, rubric_id
- `Critique` — notes[] bound to CriterionId
- `EvalReport` — score + critique + subject ref
