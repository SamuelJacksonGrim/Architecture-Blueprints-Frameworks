# System Flow — Reflexion

The outer loop learns; the inner loop is plain ReAct.

```
        ┌──────────────────────────────────────────────┐
        ▼                                                │
Goal ─▶ ATTEMPT (run a full ReAct loop, with past lessons in context)
        │
        ▼
       EVALUATE (score the attempt)
        │
        ├── good enough? ──yes──▶ Answer ✅
        │
        ▼ no
       REFLECT → write a lesson ("I failed because…") ──▶ add to lessons ──┘
                                                          (out of tries → best attempt)
```
