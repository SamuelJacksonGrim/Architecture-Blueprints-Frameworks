---
artifact: Schemas
status: complete
order: 6
fills: "conceptual ontology — Entity→State→Event→Evaluation→Decision→Action"
depends_on: [Types]
filled_by: both
last_decision: null
---

# Schemas — ReAct Agent

## Core Transformation Chain
How the ReAct loop maps onto the repo's universal ontology (this is what makes
it comparable to the other skeletons):

```
Entity      = the Agent
   ↓
State       = the Scratchpad (everything it knows so far this run)
   ↓
Event       = an Observation coming back from a tool
   ↓
Evaluation  = the Reasoner's next Thought ("did that help? what now?")
   ↓
Decision    = is_final? answer : choose an Action
   ↓
Action      = the tool call the Executor runs
   ↺ (the Observation becomes the next Event)
```

> Note: in ReAct, **Evaluation is implicit** — it happens *inside* the Reasoner's
> Thought, not as a separate module. The Reflexion and Tree-of-Thoughts variants
> pull Evaluation out into its own explicit step. Same ontology, different
> emphasis.

## Information Schemas
Raw tool output → interpreted by the next Thought → folded into the scratchpad.
The scratchpad is the single growing knowledge structure.

## Transformation Schemas
- `(goal, scratchpad) → Thought`: reasoning.
- `Action → Observation`: acting (Executor).
