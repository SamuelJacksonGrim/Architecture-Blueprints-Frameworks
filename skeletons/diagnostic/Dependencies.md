---
artifact: Dependencies
status: complete
order: 9
fills: "edges"
depends_on: [Modules, Interfaces]
filled_by: both
last_decision: D-001
---

# Dependencies — Diagnostic

Forbidden: Observer → writes. Hypothesizer → Tester. Reporter → Observer/Hypothesizer (same run). Tester → irreversible without Allowance.
