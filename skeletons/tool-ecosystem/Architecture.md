---
artifact: Architecture
status: complete
order: 1
fills: "structural blueprint — Registry, Router, Executor"
depends_on: []
filled_by: both
last_decision: D-001
---

# Architecture — Tool Ecosystem

> Three roles. One side-effect door.

## Purpose
Accept a tool request, resolve it against a catalog, run exactly one matching
implementation, return a typed result. Nothing else.

## Major Subsystems
- **Registry** — source of truth for `ToolId`, input schema, output schema, risk class.
- **Router** — given a request, returns a `ToolId` or a refusal. Never runs.
- **Executor** — given a `ToolId` + args that already passed schema, performs the call. Never chooses.
- **Policy** — hard refusals (unknown id, schema miss, risk class not allowed). Advises Router; does not execute.

## Boundaries
- **Inside / trusted:** Registry, Router, Policy.
- **Outside / untrusted:** whatever the Executor touches.
- **Process line:** Executor only.

## Data Flow
```
Request → Router (+ Policy, Registry) → ToolCall
ToolCall → Executor → ToolResult
Unknown / schema-fail / forbidden → Refusal (no Executor)
```

## Control Flow
Router owns *whether*. Executor owns *whether it happened*. Registry owns *what exists*.
