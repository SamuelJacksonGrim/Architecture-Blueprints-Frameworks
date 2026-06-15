---
artifact: DecisionLog
status: complete
order: 99
fills: "the defining decision for this variant"
depends_on: []
filled_by: both
last_decision: null
---

# DecisionLog — Tree-of-Thoughts (delta)

> Inherits D-001..D-003 from the ReAct baseline. Adds:

### D-TOT-1 — Explore many branches, prune, backtrack
- **Date:** 2026-06-15
- **Decided by:** both
- **Decision:** At each step generate `k` candidate thoughts, score them, keep a
  frontier of the promising ones, and prune the rest (enabling backtracking).
- **Alternatives:** Single greedy path (ReAct — can't recover from a wrong early
  commitment); exhaustive search (too expensive).
- **Reason:** Many hard problems have a wrong-looking-but-right first move or a
  right-looking-but-wrong one. Keeping several branches alive and scoring them
  lets the agent recover from bad early choices — at the cost of more compute.
- **Affects:** Flows; adds an Evaluator/scorer and a frontier to the baseline.
