---
artifact: DecisionLog
status: complete
order: 99
fills: "why report is a sink"
depends_on: []
filled_by: both
last_decision: null
---

# DecisionLog — Diagnostic

### D-001 — Report is a sink
- **Decision:** no auto-feedback from report to observe in one run.
- **Rejected:** continuous self-healing loop as the default.
- **Reason:** QUALITY-BAR §6. A diagnostic that steers is a controller in costume.

### D-002 — Hypothesizer cannot test
- **Decision:** split guess from probe.
- **Reason:** otherwise every guess is already an action.

### D-003 — Irreversible probes need allowance
- **Decision:** effect_class on every probe.
- **Reason:** a restart is not the same as a metric scrape.
