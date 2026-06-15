---
artifact: Flows
status: complete
order: 3
fills: "behavioral blueprint — request, event, execution, error, state-update flows"
depends_on: [Architecture]
filled_by: both
last_decision: D-001
---

# Flows — ReAct Agent

## The ReAct loop (the core of everything)
This is "the loop." Read it top to bottom — it's just think, act, look, repeat:

```
scratchpad = []
loop (step = 1 .. MAX_STEPS):                 # MAX_STEPS = safety backstop
    thought = Reasoner.think(goal, scratchpad)  # "what should I do next?"

    if thought.is_final:                        # model decides it has the answer
        return thought.answer                   # ── normal exit ──

    action      = thought.action                # e.g. search("budget 2026")
    observation = Executor.run(action)          # do it; see what comes back
    scratchpad.append(thought, action, observation)   # remember this step
end
return best_effort_answer(scratchpad)           # budget ran out → partial answer
```

## Request Flow
Goal in → enter the loop above → Final Answer (or partial) out. That's it.

## Event Flow
The only recurring "event" is an **Observation** coming back from the Executor.
It gets appended to the scratchpad and fed into the next Thought.

## Error Flow
- **Tool fails:** the Observation just says so (`ok: false`). The Reasoner sees
  the failure on the next turn and can try something else. Failures don't crash
  the loop.
- **Reasoner can't produce an action:** treat as Final Answer with low confidence.
- **Budget exhausted:** exit with the best partial answer assembled so far.

## State-Update Flow
The scratchpad is the only state, and it's append-only within a run. Each loop
turn adds exactly one `(Thought, Action, Observation)` triple.
