---
artifact: Contracts
status: complete
order: 3
fills: "delivery and isolation invariants"
depends_on: [Architecture, Flows]
filled_by: both
last_decision: D-001
---

# Contracts — Event Bus

- **G1.** Default delivery is at-most-once. At-least-once requires `idempotency_key`.
- **G2.** The bus does not branch on payload fields other than topic + schema id.
- **G3.** Dead letter is a terminal sink for the request path.
- **G4.** A handler cannot publish on the same topic in the same call stack.
- **G5.** Unknown topic is a refusal, not a silent create.
