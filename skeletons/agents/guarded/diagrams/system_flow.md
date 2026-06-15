# System Flow — Agent

Behavioral view: the bounded loop (D-003) with the pre-execution gate (D-002).

```
Goal
 │
 ▼
Recall context ──▶ Plan next action ──▶ Evaluate (pre-gate)
 ▲                                          │
 │                              terminate ◀──┤
 │                              replan    ◀──┤
 │                                          │ proceed
 │                                          ▼
 │                                    Execute tool
 │                                          │
 └──── Observe ◀── Evaluate (post) ◀────────┘
            │
            ├── done ──▶ Output(success)
            └── budget exhausted ──▶ Output(partial)
```
