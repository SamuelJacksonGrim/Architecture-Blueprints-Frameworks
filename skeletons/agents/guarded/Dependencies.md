---
artifact: Dependencies
status: complete
order: 8
fills: "allowed/forbidden dependency directions, hierarchy, import rules"
depends_on: [Modules, Interfaces]
filled_by: both
last_decision: null
---

# Dependencies — Agent

## Module Hierarchy (top = depended-upon, bottom = depends-on-others)
```
Types / Schemas            (pure vocabulary — depend on nothing)
        ▲
Interfaces                 (depend only on Types/Schemas)
        ▲
Memory · Planner · Evaluator · Executor · ToolRegistry   (implement Interfaces)
        ▲
Loop Coordinator           (orchestrates the above via Interfaces only)
        ▲
Intake · Output            (entry/exit; depend on coordinator + Types)
```

## Allowed Directions
- Any module → Types/Schemas.
- Implementations → the Interface they implement.
- Loop Coordinator → Interfaces (never concrete implementations directly).

## Forbidden Directions
- **Planner ⇏ Executor.** The planner must not run tools directly — it proposes;
  the coordinator gates and runs. (Enforces G2.)
- **Tools ⇏ Memory/Planner.** Tools are leaf capabilities; they cannot reach back
  into agent internals. (Enforces G4.)
- **No cycles.** Strictly layered.

## Import Rules
- Modules depend on **interfaces, not implementations** (dependency inversion).
- Crossing the Executor boundary is the only place untrusted code runs;
  nothing downstream of it is trusted until `Evaluator.post`.
