---
artifact: Dependencies
status: complete
order: 9
fills: "edges"
depends_on: [Modules, Interfaces]
filled_by: both
last_decision: D-001
---

# Dependencies — Event Bus

Forbidden: Dispatcher → handler impl (only SubscriberInterface). Handler → TopicRegistry writes. Happy path → DeadLetter reads.
