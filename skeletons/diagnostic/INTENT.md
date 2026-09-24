---
artifact: Intent
status: complete
order: 0
fills: "intent plus class/depth"
depends_on: []
filled_by: both
last_decision: D-001
---

# Intent Card

- **Want:** reusable observe-hypothesize-test-report skeleton
- **Must not:** let observe write, or let report become a control signal by default
- **Done when:** ten artifacts complete

```yaml
class: pipeline
depth: full
reasons:
  - reusable_skeleton_requested
  - modules_must_not_import_each_other
escalate_if:
  - network_boundary_added
  - secrets_introduced
  - module_separation_required
  - reusable_skeleton_requested
```
