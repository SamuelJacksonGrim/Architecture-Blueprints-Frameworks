# System Flow — ReAct Agent

The whole pattern in one picture: think → act → observe, looping back until the
model says "I'm done."

```
        ┌─────────────────────────────────────────┐
        ▼                                         │
Goal ─▶ THINK (Reasoner)                          │
        │   │                                     │
        │   └── is this the final answer? ──yes──▶ Output ✅
        │                                          
        ▼ no (here's an action)                    
       ACT (Executor runs the tool)                
        │                                          
        ▼                                          
       OBSERVE (capture the result) ──▶ append to Scratchpad ──┘
                                        (feeds the next THINK)

   safety backstop: if steps > MAX_STEPS, stop and give best partial answer.
```
