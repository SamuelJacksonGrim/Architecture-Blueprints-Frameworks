---
artifact: Types
status: complete
order: 4
fills: "Signal, Hypothesis, Probe, Report"
depends_on: [Contracts]
filled_by: both
last_decision: D-002
---

# Types — Diagnostic

- `Signal` — name, value, time
- `Hypothesis` — cause, confidence in [0,1], probes[]
- `Probe` — target, effect_class, timeout
- `ProbeResult` — ok | error | timeout, evidence
- `DiagReport` — signals, hypotheses, results
