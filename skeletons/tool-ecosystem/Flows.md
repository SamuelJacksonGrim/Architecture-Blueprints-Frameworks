---
artifact: Flows
status: complete
order: 2
fills: "request, refusal, and execution flows"
depends_on: [Architecture]
filled_by: both
last_decision: D-001
---

# Flows — Tool Ecosystem

## Happy path
1. Caller submits `ToolRequest` (name or id + args).
2. Router asks Registry for the record.
3. Policy checks risk class against the caller's allowance.
4. Args are validated against the input schema *before* Executor.
5. Executor runs. Result validated against output schema.
6. `ToolResult` returns. Registry is not mutated by a run.

## Refusal path
Unknown id, schema miss, or forbidden risk class → `Refusal`. Executor is not entered.

## Error path
Executor throws or times out → `ToolResult` with `status: error`. No retry inside Executor unless the tool record says the call is idempotent.

## What never happens
Router calling the world. Executor inventing a `ToolId`. Registry changing because a call succeeded.
