---
artifact: DecisionLog
status: complete
order: 99
fills: "why defaults"
depends_on: []
filled_by: both
last_decision: null
---

# DecisionLog — Event Bus

### D-001 — Default at-most-once?
- **Decision:** yes. At-least-once is opt-in with an idempotency key.
- **Rejected:** at-least-once by default.
- **Reason:** duplicates are a silent corruption. Missing once is louder.

### D-002 — No auto-topics
- **Decision:** unknown topic refuses.
- **Reason:** a typo should not invent a stream.

### D-003 — Dead letter is a sink
- **Decision:** request path never reads it.
- **Reason:** poison must not steer live dispatch.
