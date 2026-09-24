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

- **Want:** reusable pub/sub skeleton
- **Must not:** let the bus interpret payloads or silently upgrade delivery
- **Done when:** ten artifacts complete
- **Secrets / irreversible:** possible in subscribers, not in the bus

```yaml
class: service
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
