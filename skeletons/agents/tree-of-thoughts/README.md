# Tree-of-Thoughts Agent (variant)

> A **delta on the [ReAct baseline](../react/)**. Read ReAct first.

## The one-line difference
Instead of committing to one line of reasoning, the agent **explores several
branches at once**, scores them, expands the promising ones, and **backtracks**
away from dead ends — like searching a tree of possible thoughts.

## When to use it
Problems that need exploration and backtracking: puzzles, planning with many
options, anything where the first idea is often wrong and you want to compare
alternatives before committing.

## What changes vs ReAct
ReAct walks a single straight path. Tree-of-Thoughts turns "the next thought"
into "**several** candidate next thoughts," keeps a frontier of the best ones,
and searches:

| | ReAct | Tree-of-Thoughts |
|---|---|---|
| Shape | one line | a search tree |
| Per step | 1 thought | N candidate thoughts, scored |
| Recovery | correct on the next turn | backtrack to a better branch |
| Cost | low | higher (explores more) |

## What stays the same
Each node's reasoning is ReAct-style. Types, Interfaces, Dependencies, and the
Schema chain are inherited. Only **Flows** and one **DecisionLog** entry differ.

> Instantiation note: variant + ReAct base = one complete system.
