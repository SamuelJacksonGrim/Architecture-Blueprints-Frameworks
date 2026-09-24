---
artifact: Interfaces
status: complete
order: 6
fills: "publish and subscribe plugs"
depends_on: [Schemas]
filled_by: both
last_decision: D-003
---

# Interfaces — Event Bus

### PublisherInterface
- publish(Event) → PublishResult

### SubscriberInterface
- handle(Event) → ack | retry | fail

### TopicRegistryInterface
- get(TopicId) → TopicRecord | none
