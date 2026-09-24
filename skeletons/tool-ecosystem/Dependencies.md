---
artifact: Dependencies
status: complete
order: 9
fills: "allowed and forbidden edges"
depends_on: [Modules, Interfaces]
filled_by: both
last_decision: D-001
---

# Dependencies — Tool Ecosystem

```
Types / Schemas
    ▲
Interfaces
    ▲
Registry · Policy
    ▲
Router          (interfaces only)
    ▲
Executor        (implementations of tools; no path back to Router/Registry writes)
```

Forbidden: Router → tool impl. Tool impl → Registry. Executor → Router.
