---
artifact: Interfaces
status: complete
order: 7
fills: "plug points — the contracts between modules that make them swappable"
depends_on: [Schemas]
filled_by: both
last_decision: null
---

# Interfaces — ReAct Agent

### ReasonerInterface
- **Purpose:** produce the next Thought (and Action, or a Final Answer).
- **Inputs:** `think(goal, scratchpad)`
- **Outputs:** `Thought` (with `is_final`, plus `action` or `answer`)
- **Upholds:** A2 (fallible), G3 (every thought is recorded).
- **Implemented by:** Reasoner (any LLM) · **Consumed by:** loop control

### ToolInterface
- **Purpose:** one action the agent can take.
- **Inputs:** `args: object` matching the tool's declared schema.
- **Outputs:** a value or an error — surfaced as an `Observation`.
- **Upholds:** A1, G2.
- **Implemented by:** each tool · **Consumed by:** Executor

### ExecutorInterface
- **Purpose:** run an Action against the world, safely.
- **Inputs:** `run(action)`
- **Outputs:** `Observation` (never throws across the boundary)
- **Upholds:** G2.
- **Implemented by:** Executor · **Consumed by:** loop control

### ScratchpadInterface
- **Purpose:** the run's append-only memory.
- **Inputs:** `append(triple)`, `read()`
- **Outputs:** `Triple[]`
- **Upholds:** I2, G3.
- **Implemented by:** Scratchpad · **Consumed by:** loop control, Reasoner
