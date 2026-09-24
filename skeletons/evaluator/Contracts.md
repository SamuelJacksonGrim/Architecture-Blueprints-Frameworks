---
artifact: Contracts
status: complete
order: 3
fills: "scoring invariants"
depends_on: [Architecture, Flows]
filled_by: both
last_decision: D-001
---

# Contracts — Evaluator

- **G1.** Weights in a rubric sum to 1.0. Change requires auditing every consumer.
- **G2.** Only Scorer produces `Score`. Critic produces notes.
- **G3.** Evaluator has no write path to the subject.
- **G4.** A run uses one rubric id. No mid-run swap.
- **G5.** Report is a sink for this run.
