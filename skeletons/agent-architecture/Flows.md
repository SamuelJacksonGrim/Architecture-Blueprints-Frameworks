---
artifact: Flows
status: complete
order: 3
fills: "behavioral blueprint — request, event, execution, error, state-update flows"
depends_on: [Architecture]
filled_by: both
last_decision: D-003
---

# Flows — Agent

## Request Flow (goal → response)
1. Goal-giver submits a `Goal` to **Intake**.
2. Intake normalizes it and emits the first `Percept`.
3. Loop coordinator enters the **execution loop** (below).
4. When the loop signals done, **Output** assembles a `Response`.

## Execution Flow (the agent loop)
```
loop (step = 1 .. MAX_STEPS):           # bounded — see D-003
  context   = Memory.recall(goal, step)
  plan      = Planner.next(goal, context, last_observation)
  verdict   = Evaluator.pre(plan)        # gate BEFORE acting — D-002
  if verdict == TERMINATE: break
  if verdict == REPLAN:    continue
  result    = Executor.run(plan.action)  # crosses untrusted boundary
  obs       = Observation.from(result)
  Memory.write(obs)
  post      = Evaluator.post(goal, obs)
  last_observation = obs
  if post == DONE: break
end
```

## Event Flow
- `Percept` (from Intake) and `Observation` (from Executor) are the two event
  types entering the loop. Both are written to Memory before being reasoned on.
- The Evaluator emits `Verdict` events that the coordinator consumes; it never
  acts on the world directly.

## Error Flow
- **Tool failure:** Executor returns a `ToolResult{ ok: false }`. It is wrapped
  as an `Observation` like any other — the Planner sees the failure and may
  replan. Failures never throw out of the loop.
- **Planner failure / no valid action:** treated as `verdict = TERMINATE` with
  reason `no_plan`.
- **Step budget exhausted:** loop exits; Output produces a `partial` Response.
- **Boundary violation (untrusted result malformed):** Evaluator.post rejects it
  → replan; never written to long-term memory.

## State-Update Flow
- Working memory is written **every step** (percept, plan, observation, verdict).
- Long-term memory is written **only on `Evaluator.post == DONE` or explicit
  commit** — partial/unvalidated state stays in working memory and is discarded
  at run end.
