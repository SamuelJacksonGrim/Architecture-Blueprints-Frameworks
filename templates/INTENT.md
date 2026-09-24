---
artifact: Intent
status: stub
order: 0
fills: "the human's goal, plus the class/depth decision a later entity can inspect"
depends_on: []
filled_by: both
last_decision: null
---

# Intent Card

> Copy this file into the new project as `INTENT.md`.
> The human may leave every line blank. The model fills from the conversation,
> shows it once, and proceeds. Cap: three blocking questions.

- **Want:**
- **Must not:**
- **Who it's for:**
- **Runs where:**
- **Done when:**
- **Secrets / private data / irreversible actions:** none / listed here
- **Language / host (if the human named one):**

## Selector decision

Class and depth are independent axes. Do not treat depth as a complexity score.

```yaml
class:            # cli | library | pipeline | service | ui | agent-loop | cognitive-cycle | unknown
depth:            # thin | standard | full
reasons:          # structural conditions that hold *now*
  - # e.g. single_process | no_network_boundary | no_irreversible_action
escalate_if:
  - network_boundary_added
  - secrets_introduced
  - persistent_state_added
  - module_separation_required
  - reusable_skeleton_requested
```
