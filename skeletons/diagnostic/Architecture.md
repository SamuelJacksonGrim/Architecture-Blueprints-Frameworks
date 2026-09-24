---
artifact: Architecture
status: complete
order: 1
fills: "observe, hypothesize, test, report"
depends_on: []
filled_by: both
last_decision: D-001
---

# Architecture — Diagnostic

## Purpose
Explain a symptom without quietly becoming the controller.

## Major Subsystems
- **Observer** — read-only collection of signals.
- **Hypothesizer** — ranked candidate causes. No side effects.
- **Tester** — the only module that may probe. Each probe is declared (target, effect class).
- **Reporter** — terminal sink. Does not write Observer or Hypothesizer.

## Boundaries
Observe is one-way. Test is gated. Report does not feed the request path.
