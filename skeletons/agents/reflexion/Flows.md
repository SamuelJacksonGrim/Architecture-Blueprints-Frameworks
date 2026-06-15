---
artifact: Flows
status: complete
order: 3
fills: "behavioral blueprint — the reflect-and-retry outer loop (delta vs ReAct)"
depends_on: [../react/Architecture.md]
filled_by: both
last_decision: D-RX-1
---

# Flows — Reflexion (delta vs ReAct)

## The loop
An outer "try again, but smarter" loop around an ordinary ReAct attempt:

```
lessons = []                              # verbal self-critiques, kept across tries
loop (try = 1 .. MAX_TRIES):
    result = run_react(goal, lessons)     # ← the whole ReAct baseline, with lessons in context
    score  = Evaluator.judge(goal, result)

    if score.is_good_enough:
        return result                     # ── success ──

    lesson = Reflector.reflect(goal, result, score)   # "I failed because… next time…"
    lessons.append(lesson)                # remember it; feeds the next attempt
end
return best_result_so_far(lessons)
```

## What's different from ReAct's flow
- ReAct has no memory between *attempts* — it just runs once. Reflexion adds an
  **Evaluator** (scores the attempt) and a **Reflector** (turns the failure into
  a sentence the next attempt can read).
- The growing `lessons` list is the key new state: it's how the agent avoids
  making the same mistake twice.

## Error Flow
A bad attempt isn't a failure — it's *fuel*. It produces a lesson and a retry.
The run only ends on success or when `MAX_TRIES` is spent (then return the best
attempt seen).
