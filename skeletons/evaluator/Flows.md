---
artifact: Flows
status: complete
order: 2
fills: "evaluate flow"
depends_on: [Architecture]
filled_by: both
last_decision: D-001
---

# Flows — Evaluator

1. Load rubric by id. Missing rubric → refuse.
2. Open subject as read-only.
3. Critic may emit notes per criterion.
4. Scorer emits Score (weights applied once).
5. Report freezes both. End.
