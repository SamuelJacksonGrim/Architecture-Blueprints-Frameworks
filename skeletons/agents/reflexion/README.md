# Reflexion Agent (variant)

> A **delta on the [ReAct baseline](../react/)**. Read ReAct first.

## The one-line difference
After an attempt fails (or scores poorly), the agent writes itself a short
**verbal self-critique** — "here's what I did wrong" — stores it, and **retries**
with that lesson in context.

## When to use it
Tasks where the agent gets multiple shots and should *learn from its own
mistakes* between tries (coding against tests, puzzles, anything with a
pass/fail signal).

## What changes vs ReAct
ReAct is a single inner loop. Reflexion wraps an **outer loop** around it:

```
attempt → evaluate → reflect (write a lesson) → retry with the lesson → ...
```

The reflection text becomes part of memory, so each retry is informed by every
prior failure — not a blind repeat.

## What stays the same
The inner attempt is just a ReAct loop. Types, Interfaces, Dependencies, and the
Schema chain are inherited. Only **Flows** and one **DecisionLog** entry differ.

> Instantiation note: variant + ReAct base = one complete system.
