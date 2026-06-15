---
artifact: Types
status: complete
order: 5
fills: "core domain types, primitives, enums, identifiers, structural schemas"
depends_on: [Contracts]
filled_by: both
last_decision: null
---

# Types — Agent

## Core Domain Types
- **Goal** — `{ id: GoalId, statement: text, constraints: [] }`
- **Percept** — `{ source, content, at: timestamp }` — input from the world.
- **MemoryRecord** — `{ id, tier: MemoryTier, kind, payload, at }`
- **Plan** — `{ rationale: text, action: Action }`
- **Action** — `{ tool: ToolId, args: object }`
- **ToolCall** — a resolved `Action` bound to a tool implementation.
- **ToolResult** — `{ ok: bool, value?, error? }`
- **Observation** — `{ from: ToolId, result: ToolResult, at }`
- **Verdict** — see enum below, plus `{ verdict, reason: text }`
- **Response** — `{ status: RunStatus, summary, artifacts: [] }`

## Primitives & Identifiers
- `GoalId`, `ToolId`, `RecordId` — opaque stable string ids.
- `timestamp` — ISO-8601.

## Enums
- **MemoryTier** = `working | longterm`
- **Verdict** = `proceed | retry | replan | terminate`
- **PostVerdict** = `done | continue | reject`
- **RunStatus** = `success | partial | gave_up`

## Structural Schemas
- A **loop step** is the tuple `(Percept|Observation, Plan, Verdict, ToolResult?)`.
