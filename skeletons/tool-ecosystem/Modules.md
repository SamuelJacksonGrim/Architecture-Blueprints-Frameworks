---
artifact: Modules
status: complete
order: 8
fills: "module list"
depends_on: [Interfaces]
filled_by: both
last_decision: D-003
---

# Modules — Tool Ecosystem

| Module | Responsibility | Owns | Implements |
|--------|----------------|------|------------|
| Registry | catalog | ToolRecords | RegistryInterface |
| Policy | allowance vs risk | refusal rules | — |
| Router | choose or refuse | no world | RouterInterface |
| Executor | run | side effects | ExecutorInterface |
| Schemas | input/output checks | validators | — |
