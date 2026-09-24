---
artifact: DecisionLog
status: complete
order: 99
fills: "why this pattern is three roles"
depends_on: []
filled_by: both
last_decision: null
---

# DecisionLog — Tool Ecosystem

### D-001 — Split choose from run?
- **Decision:** Router ≠ Executor.
- **Rejected:** a single Dispatcher that picks and runs.
- **Reason:** the moment those collapse, refusals cannot be proven.

### D-002 — Schema before run
- **Decision:** validate args against Registry schema before Executor.
- **Rejected:** "the tool will validate."
- **Reason:** a tool that validates after side effects has already happened.

### D-003 — Registry is not a bus
- **Decision:** runs do not mutate the catalog.
- **Rejected:** auto-register on first call.
- **Reason:** identity must be deliberate.
