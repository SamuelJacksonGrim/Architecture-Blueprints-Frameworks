---
artifact: Contracts
status: complete
order: 3
fills: "observe-only and probe gates"
depends_on: [Architecture, Flows]
filled_by: both
last_decision: D-001
---

# Contracts — Diagnostic

- **G1.** Observer has no write path into the subject system.
- **G2.** Hypothesizer cannot call Tester.
- **G3.** Every Tester call names `effect_class`: `read` | `write` | `irreversible`. Irreversible requires an explicit allowance.
- **G4.** Report is a terminal sink for the run.
- **G5.** A failed test does not auto-escalate to a write probe.
