---
artifact: Types
status: complete
order: 4
fills: "Event, Topic, Subscription"
depends_on: [Contracts]
filled_by: both
last_decision: D-002
---

# Types — Event Bus

- `TopicId`, `EventId`, `SubscriptionId`
- `Delivery` — `at_most_once` | `at_least_once`
- `Event` — id, topic, schema_id, payload, idempotency_key?
- `PublishResult` — accepted | refused
