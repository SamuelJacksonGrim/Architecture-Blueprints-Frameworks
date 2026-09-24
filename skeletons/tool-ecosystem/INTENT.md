---
artifact: Intent
status: complete
order: 0
fills: "intent plus inspectable class/depth"
depends_on: []
filled_by: both
last_decision: D-001
---

# Intent Card

- **Want:** a reusable skeleton for deterministic tool dispatch
- **Must not:** let the chooser run tools, or the runner invent tools
- **Who it's for:** any system that needs named, schema-checked side effects
- **Runs where:** in-process library; Executor may cross a process/network line
- **Done when:** all ten artifacts complete and the three-role split is explicit
- **Secrets / irreversible actions:** possible at the Executor boundary
- **Language / host:** unspecified — smallest that can implement the three roles

```yaml
class: library
depth: full
reasons:
  - reusable_skeleton_requested
  - modules_must_not_import_each_other
  - executor_may_cross_process_or_network
escalate_if:
  - network_boundary_added
  - secrets_introduced
  - module_separation_required
  - reusable_skeleton_requested
```
