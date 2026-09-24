---
artifact: Types
status: complete
order: 4
fills: "ToolId, request, result, risk"
depends_on: [Contracts]
filled_by: both
last_decision: D-002
---

# Types — Tool Ecosystem

- `ToolId` — stable string. Never reused for a different schema.
- `RiskClass` — `read` | `write` | `irreversible`.
- `ToolRecord` — id, schemas, risk class, idempotent: bool.
- `ToolRequest` — id or name, args, caller allowance.
- `ToolCall` — resolved id + validated args.
- `ToolResult` — status `ok` | `error` | `timeout`, payload or error.
- `Refusal` — reason `unknown` | `schema` | `forbidden`.
