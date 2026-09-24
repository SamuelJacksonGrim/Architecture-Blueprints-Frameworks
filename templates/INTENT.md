---
artifact: Intent
status: stub
order: 0
fills: "human intent plus the inspectable class/depth decision"
depends_on: []
filled_by: both
last_decision: null
---

# Intent Card

> Copy to the project as `INTENT.md`.
> The human may leave every line blank. You fill from the conversation, show
> once, and proceed. Cap: three blocking questions.
> Class and depth are *your* judgment. The human may override. They do not
> have to name a depth for you to start.

- **Want:**
- **Must not:**
- **Who it's for:**
- **Runs where:**
- **Done when:**
- **Secrets / private data / irreversible actions:** none / listed here
- **Language / host (only if the human named one):**

## Selector decision

Axes and escalation triggers live only in [`SELECTOR.md`](../SELECTOR.md) Step C.
Instantiate them here. Do not invent a second list.

```yaml
class:            # from SELECTOR
depth:            # from SELECTOR governing test — you chose this
reasons:          # structural conditions that hold now
  -
escalate_if:      # copy SELECTOR Step C triggers only
  -
```
