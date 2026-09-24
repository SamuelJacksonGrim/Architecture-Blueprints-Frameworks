---
artifact: Modules
status: complete
order: 8
fills: "modules"
depends_on: [Interfaces]
filled_by: both
last_decision: D-003
---

# Modules — Diagnostic

| Module | Responsibility | Implements |
|--------|----------------|------------|
| Observer | read signals | ObserverInterface |
| Hypothesizer | rank causes | HypothesizerInterface |
| Tester | declared probes | TesterInterface |
| Reporter | sink | ReporterInterface |
| Allowance | irreversible gate | — |
