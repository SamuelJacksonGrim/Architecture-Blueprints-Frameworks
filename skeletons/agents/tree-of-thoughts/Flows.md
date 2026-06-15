---
artifact: Flows
status: complete
order: 3
fills: "behavioral blueprint — the branching search loop (delta vs ReAct)"
depends_on: [../react/Architecture.md]
filled_by: both
last_decision: D-TOT-1
---

# Flows — Tree-of-Thoughts (delta vs ReAct)

## The loop
Search over a tree of partial reasoning paths instead of walking one path:

```
frontier = [ root(goal) ]                      # nodes still worth exploring
best = null

loop (until solved or budget spent):
    node      = frontier.pick_best()            # most promising partial path
    thoughts  = Reasoner.expand(node, k)        # generate k candidate next steps
    children  = [ evaluate(goal, t) for t in thoughts ]   # score each candidate

    for child in children:
        if child.is_solution: return child.path        # ── success ──
        if child.score > PRUNE_THRESHOLD:
            frontier.add(child)                  # keep promising branches
        # low-scoring children are dropped → that's the "backtrack"

    best = max(best, children, key=score)
end
return best.path                                 # best partial path found
```

## What's different from ReAct's flow
- ReAct produces **one** next thought per turn. Here the Reasoner produces **k**,
  and an Evaluator scores them so the search can prefer good branches.
- The **frontier** (the set of live branches) is the new state. Dropping a weak
  branch and returning to a stronger one *is* backtracking — the thing ReAct
  can't do.

## Error Flow
A dead-end branch isn't fatal: it's pruned, and search continues from the next
best node on the frontier. The run ends on a solution or when the search budget
is exhausted (return best path found — the G1 backstop).
