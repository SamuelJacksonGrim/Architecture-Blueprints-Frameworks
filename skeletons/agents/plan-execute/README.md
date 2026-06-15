# Plan-and-Execute Agent (variant)

> A **delta on the [ReAct baseline](../react/)**. Read ReAct first; this page
> only describes what changes.

## The one-line difference
Instead of deciding the next step *every* turn, the agent makes a **full plan
up front**, then executes the steps — re-planning only if reality diverges.

## When to use it
Long, multi-step tasks where steps depend on each other. The original paper
reports a **~3.6× speedup** over step-by-step ReAct, because you call the
expensive Reasoner far fewer times.

## What changes vs ReAct
| | ReAct | Plan-Execute |
|---|---|---|
| Reasoner calls | every step | once to plan (+ occasional replans) |
| Structure | one loop | a Planner + an Executor loop + a Replanner |
| Best for | short, exploratory tasks | long tasks with dependent steps |

## What stays the same
Types, Interfaces, Dependencies, Contracts (G1/G2), and the universal Schema
chain are all inherited from the ReAct baseline. Only **Flows** and one
**DecisionLog** entry differ — see this folder's `Flows.md` and `DecisionLog.md`.

> Instantiation note: a variant + the ReAct base together form one complete
> 10-artifact system. The variant folder carries only the artifacts that change.
