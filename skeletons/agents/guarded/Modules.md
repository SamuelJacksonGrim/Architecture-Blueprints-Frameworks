---
artifact: Modules
status: complete
order: 9
fills: "module list, ownership, responsibilities, boundaries"
depends_on: [Interfaces]
filled_by: both
last_decision: null
---

# Modules — Agent

| Module | Responsibility | Owns (boundary) | Implements interface |
|--------|----------------|-----------------|----------------------|
| Intake | Normalize goal → `Goal` + first `Percept` | input parsing | — |
| Memory | Recall/persist `MemoryRecord`s across tiers | working + longterm store | MemoryStoreInterface |
| Planner | Propose next `Action` as a `Plan` | reasoning state | PlannerInterface |
| Evaluator | Gate actions (pre) + validate observations (post) | verdict policy | EvaluatorInterface |
| ToolRegistry | Resolve `ToolId` → tool impl | tool catalog | — |
| Executor | Run `ToolCall` in isolation → `ToolResult` | world side-effects | ExecutorInterface |
| LoopCoordinator | Drive the bounded loop; own termination | step budget, control flow | — |
| Output | Assemble final `Response` | result formatting | — |
