---
artifact: Flows
status: complete
order: 2
fills: "publish, deliver, poison"
depends_on: [Architecture]
filled_by: both
last_decision: D-001
---

# Flows — Event Bus

## Publish
Validate topic exists → validate payload against topic schema id → stamp event id → enqueue.

## Deliver
Dispatcher reads queue → for each subscription, invoke handler with timeout.

## Poison
Handler error after retry budget → dead letter. Happy path does not read dead letter.
