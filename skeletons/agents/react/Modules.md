---
artifact: Modules
status: complete
order: 9
fills: "module list, ownership, responsibilities, boundaries"
depends_on: [Interfaces]
filled_by: both
last_decision: null
---

# Modules — ReAct Agent

| Module | Responsibility | Owns (boundary) | Implements interface |
|--------|----------------|-----------------|----------------------|
| Reasoner | Produce next Thought / Action / Final Answer | the prompting + LLM call | ReasonerInterface |
| ToolRegistry | Resolve `ToolId` → tool implementation | the tool catalog | — |
| Executor | Run an Action, return an Observation | outside-world effects | ExecutorInterface |
| Scratchpad | Hold the append-only run transcript | working memory | ScratchpadInterface |
| LoopControl | Drive think→act→observe; own MAX_STEPS | control flow, termination | — |
| Output | Assemble the final Answer | result formatting | — |
