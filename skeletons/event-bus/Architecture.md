---
artifact: Architecture
status: complete
order: 1
fills: "topics, publishers, subscribers, dead letter"
depends_on: []
filled_by: both
last_decision: D-001
---

# Architecture — Event Bus

## Purpose
Accept an event, persist-or-forward per topic policy, deliver to subscribers, isolate poison.

## Major Subsystems
- **Topic Registry** — names, schema id, delivery policy.
- **Publisher API** — only way events enter.
- **Dispatcher** — fan-out to subscriptions.
- **Subscriber runtime** — invokes handlers; failures go to retry or dead letter.
- **Dead letter** — poison events. Observe-only from the happy path.

## Boundaries
Bus core never imports a handler. Handlers never import Dispatcher internals.
