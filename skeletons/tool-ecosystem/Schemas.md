---
artifact: Schemas
status: complete
order: 5
fills: "entity-state-event chain for a tool call"
depends_on: [Types]
filled_by: both
last_decision: D-002
---

# Schemas — Tool Ecosystem

Entity: `ToolRecord`.
State: registered | deprecated (callable until removed) | removed (id retired).
Event: `Registered` | `Deprecated` | `Removed` | `Invoked` | `Refused`.
Evaluation: Policy + schema check.
Decision: route or refuse.
Action: Executor run, or none.
