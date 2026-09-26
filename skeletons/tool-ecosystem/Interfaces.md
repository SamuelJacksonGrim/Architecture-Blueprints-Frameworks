---
artifact: Interfaces
status: complete
order: 6
fills: "plug points between the three roles"
depends_on: [Types, Contracts]
filled_by: both
last_decision: D-003
---

# Interfaces — Tool Ecosystem

### RegistryInterface
- lookup(id|name) → ToolRecord | none
- list() → [ToolRecord]
- Implemented by: Registry. Consumed by: Router, Policy.

### RouterInterface
- route(ToolRequest) → ToolCall | Refusal
- Implemented by: Router. Consumed by: caller.

### ExecutorInterface
- run(ToolCall) → ToolResult
- Implemented by: Executor. Consumed by: caller, never Router.
