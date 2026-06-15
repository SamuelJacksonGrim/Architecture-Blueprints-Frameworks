---
artifact: Flows
status: complete
order: 3
fills: "behavioral blueprint — the plan-then-execute loop (delta vs ReAct)"
depends_on: [../react/Architecture.md]
filled_by: both
last_decision: D-PE-1
---

# Flows — Plan-and-Execute (delta vs ReAct)

## The loop
Two phases instead of one. Plan first, then grind through the steps:

```
plan = Planner.make_plan(goal)        # a full ordered list of steps, up front
results = []

for step in plan:                     # EXECUTE phase
    obs = Executor.run(step.action)
    results.append(obs)

    if not on_track(plan, results):    # reality diverged from the plan?
        plan = Replanner.revise(goal, plan, results)   # patch the remaining plan
        # (continue with the revised plan)

return synthesize(goal, results)       # combine step outputs into the answer
```

## What's different from ReAct's flow
- ReAct interleaves one think + one act per turn. Here, **all the thinking that
  can be done up front, is** — the Planner emits the whole step list before any
  action runs.
- A **Replanner** is the safety valve: when an Observation shows the plan won't
  work, it revises the *remaining* steps. (This is the part beginners forget —
  without it, a plan that goes stale just fails.)

## Error Flow
A failed step triggers `Replanner.revise` rather than ending the run. If
replanning can't find a viable path, exit with a partial answer (same G1 budget
backstop as ReAct).
