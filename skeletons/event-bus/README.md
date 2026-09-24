# Event Bus — publish / subscribe

A bus moves events. It does not interpret them. Publishers do not know
subscribers. Delivery policy is explicit per topic.

Default guarantee: **at-most-once**. At-least-once is opt-in and requires an
idempotency key on the event.
