---
artifact: Dependencies
status: complete
order: 8
fills: "allowed/forbidden dependency directions, hierarchy, import rules"
depends_on: [Modules, Interfaces]
filled_by: both
last_decision: null
---

# Dependencies — ReAct Agent

## Module Hierarchy (top = depended-upon)
```
Types / Schemas                 (pure vocabulary)
        ▲
Interfaces                      (depend only on Types/Schemas)
        ▲
Reasoner · Executor · ToolRegistry · Scratchpad   (implement Interfaces)
        ▲
Loop Control                    (orchestrates via Interfaces only)
        ▲
Output                          (formats the final Answer)
```

## Allowed Directions
- Any module → Types/Schemas.
- Implementations → the Interface they implement.
- Loop Control → Interfaces (not concrete implementations).

## Forbidden Directions
- **Reasoner ⇏ Executor.** The Reasoner only *proposes* an Action; Loop Control
  runs it. This keeps the "think" and "act" halves cleanly separated.
- **Tools ⇏ Reasoner/Scratchpad.** Tools are leaves; they can't reach back into
  the agent. (Enforces G2.)
- **No cycles.**

## Import Rules
- Depend on interfaces, not implementations (so any LLM or tool is swappable).
