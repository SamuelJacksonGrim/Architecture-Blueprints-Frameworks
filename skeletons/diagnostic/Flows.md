---
artifact: Flows
status: complete
order: 2
fills: "the four-beat loop"
depends_on: [Architecture]
filled_by: both
last_decision: D-001
---

# Flows — Diagnostic

1. Observer snapshots signals.
2. Hypothesizer ranks causes. If none pass a minimum confidence, skip Test.
3. For each allowed probe on the top hypothesis: Tester runs, records result.
4. Reporter writes the bundle. Stop.

No implicit loop back from Report into Observer inside one run.
