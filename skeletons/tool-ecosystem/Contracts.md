---
artifact: Contracts
status: complete
order: 3
fills: "invariants for the three-role split"
depends_on: [Architecture, Flows]
filled_by: both
last_decision: D-001
---

# Contracts — Tool Ecosystem

- **G1.** Router has no import path to any tool implementation.
- **G2.** Executor accepts only a `ToolId` that exists in Registry *now*.
- **G3.** Args that fail the input schema never reach Executor.
- **G4.** A tool implementation cannot write the Registry.
- **G5.** Risk class is part of the Registry record, not a guess at call time.
- **G6.** Side effects happen only in Executor.

Failure if G1 is broken: the chooser becomes the world, and refusals become theater.
