---
artifact: Types
status: complete
order: 5
fills: "core domain types, primitives, enums, identifiers, structural schemas"
depends_on: [Contracts]
filled_by: both
last_decision: null
---

# Types — ReAct Agent

## Core Domain Types
- **Goal** — `{ id: GoalId, statement: text }`
- **Thought** — `{ text, is_final: bool, action?: Action, answer?: text }`
- **Action** — `{ tool: ToolId, args: object }`
- **Observation** — `{ from: ToolId, ok: bool, value?, error?, at }`
- **Triple** — `{ thought: Thought, action: Action, observation: Observation }`
- **Scratchpad** — `Triple[]` (the running transcript)
- **Answer** — `{ status: RunStatus, text }`

## Primitives & Identifiers
- `GoalId`, `ToolId` — opaque stable strings.
- `at` — ISO-8601 timestamp.

## Enums
- **RunStatus** = `success | partial`
  *(`success` = Reasoner emitted Final Answer; `partial` = budget ran out.)*

## Structural Schemas
- A **loop turn** = produce one `Thought`; if not final, run its `Action`,
  capture an `Observation`, append a `Triple`.
