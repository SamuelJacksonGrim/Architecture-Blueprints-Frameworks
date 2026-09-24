---
artifact: Interfaces
status: complete
order: 6
fills: "plugs"
depends_on: [Schemas]
filled_by: both
last_decision: D-003
---

# Interfaces — Diagnostic

### ObserverInterface
- snapshot() → [Signal]

### HypothesizerInterface
- rank([Signal]) → [Hypothesis]

### TesterInterface
- run(Probe) → ProbeResult

### ReporterInterface
- write(DiagReport) → void
