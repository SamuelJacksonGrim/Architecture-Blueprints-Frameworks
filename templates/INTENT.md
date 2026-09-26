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

> Copy to the project as `INTENT.md`. Rules for filling it: SELECTOR Step A.
> Mark guesses inline with *(guess)*. Anything unmarked was stated or implied.
> Class and depth are your judgment. The human may override after the pass.

- **Want:**
- **Must not:**
- **Roles** (who uses it, and what each may do):
- **Runs where / exposed to:**
- **Money:**
- **Private data / secrets:**
- **Irreversible actions:**
- **Done when:**
- **Stack** (named by the human, or chosen: smallest that can smoke-test):

## Implied counterparts

| Named | Expected but unstated | Decision | Why |
|---|---|---|---|
| | | include / exclude | |

## Selector decision

Axes, triggers, and profiles live only in [`SELECTOR.md`](../SELECTOR.md).
Instantiate them here. Do not invent a second list.

```yaml
class:            # one token from SELECTOR Step B
depth:            # thin | standard | full (SELECTOR Step C)
exposure:         # local-single | local-shared | networked | multi-tenant
asked:            # none (and why), or each question and the field it resolved
reasons:          # the Step C triggers that hold now, plus anything that raised depth
  -
escalate_if:      # the Step C triggers that do not hold yet
  -
```
