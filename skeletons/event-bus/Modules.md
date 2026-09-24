---
artifact: Modules
status: complete
order: 8
fills: "module list"
depends_on: [Interfaces]
filled_by: both
last_decision: D-003
---

# Modules — Event Bus

| Module | Responsibility | Implements |
|--------|----------------|------------|
| TopicRegistry | catalog | TopicRegistryInterface |
| Publisher | entry | PublisherInterface |
| Dispatcher | fan-out | — |
| SubscriberRuntime | invoke handlers | — |
| DeadLetter | poison store | — |
