---
artifact: Schemas
status: complete
order: 6
fills: "conceptual ontology — Entity→State→Event→Evaluation→Decision→Action"
depends_on: [Types]
filled_by: both
last_decision: null
---

# Schemas — Agent

## Core Transformation Chain
This is where the Agent skeleton becomes *comparable to every other skeleton*.
The agent loop is the canonical chain made concrete:

```
Entity      = the Agent (goal-directed actor)
   ↓
State       = Memory (working + longterm)
   ↓
Event       = Percept | Observation
   ↓
Evaluation  = Evaluator.pre / Evaluator.post → Verdict
   ↓
Decision    = the chosen Action within a Plan
   ↓
Action      = ToolCall executed against the world
   ↺ (Observation becomes the next Event)
```

## Cognitive Schemas
- **Belief** ← long-term `MemoryRecord`s (what the agent holds true).
- **Working hypothesis** ← current `Plan.rationale`.
- **Goal** is the apex schema; every Decision is justified by reference to it.

## Information Schemas
- Information enters as raw `Percept`/`ToolResult`, is **validated** (Evaluator),
  then **promoted** working → longterm. Promotion is the only trust transition.

## Transformation Schemas
- `Percept → context`: `Memory.recall` (retrieval/relevance).
- `context → Plan`: `Planner.next` (reasoning).
- `Plan → Verdict`: `Evaluator.pre` (gating).
- `Action → Observation`: `Executor.run` (effecting).
