---
artifact: Interfaces
status: complete
order: 7
fills: "plug points — the contracts between modules that make them swappable"
depends_on: [Schemas]
filled_by: both
last_decision: null
---

# Interfaces — Agent

> Every interface upholds a contract from `Contracts.md`. Swapping an
> implementation is legal iff it preserves the interface and its contract.

### PlannerInterface
- **Purpose:** propose the next action.
- **Inputs:** `Goal`, `context: MemoryRecord[]`, `last: Observation?`
- **Outputs:** `Plan | no_plan`
- **Upholds:** A2 (planner is fallible — callers must gate).
- **Implemented by:** Planner · **Consumed by:** loop coordinator

### EvaluatorInterface
- **Purpose:** gate actions and validate observations.
- **Inputs:** `pre(Plan)` → `Verdict`; `post(Goal, Observation)` → `PostVerdict`
- **Outputs:** verdicts only — **no side effects**.
- **Upholds:** G2, G3, I3.
- **Implemented by:** Evaluator · **Consumed by:** loop coordinator

### ToolInterface
- **Purpose:** a single capability the agent can invoke.
- **Inputs:** `args: object` (matching the tool's declared schema)
- **Outputs:** `ToolResult` (never throws across the boundary)
- **Upholds:** A1, G4.
- **Implemented by:** each tool · **Consumed by:** Executor (via Tool Registry)

### ExecutorInterface
- **Purpose:** run a resolved `ToolCall` in isolation.
- **Inputs:** `Action` (verdict == proceed)
- **Outputs:** `ToolResult`
- **Upholds:** G4 (blast radius), Executor.run post-condition.
- **Implemented by:** Executor · **Consumed by:** loop coordinator

### MemoryStoreInterface
- **Purpose:** recall and persist records by tier.
- **Inputs:** `recall(goal, step)`; `write(record, tier)`
- **Outputs:** `MemoryRecord[]` / ack
- **Upholds:** G3, I2.
- **Implemented by:** Memory · **Consumed by:** loop coordinator, Planner
