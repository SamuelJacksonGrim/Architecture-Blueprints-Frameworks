# SCHEMA — the 10-artifact language

The ten names are the language of the build. Default construction order is
[`PIPELINE.md`](PIPELINE.md). How much must be persisted is [`SELECTOR.md`](SELECTOR.md).

Construction has an order. Cognition may look backward and revise.
Neither is a request for permission.

---

## Frontmatter

```yaml
---
artifact: Architecture
status: stub                  # stub | partial | complete
order: 1                      # construction order hint
fills: "structural blueprint"
depends_on: []
filled_by: both
last_decision: null
---
```

### Dependency rule (completeness)

- A dependency must be `partial` or `complete` before the dependent artifact
  may itself be marked `complete`.
- Revision of an earlier artifact during the same pass is allowed.
- `depends_on` does not authorize a thought and does not pause the pass.

### Depth self-consistency

An artifact required `complete` at a given depth may only `depends_on` artifacts
that same depth also requires `complete`.

If an inherited edge breaks this, the edge to the optional artifact does not
gate completeness at that depth. Do not complete an optional artifact just to
satisfy an edge. That would silently raise the depth. No DecisionLog entry is
needed. This rule already decides it.

### Three states

| State | Meaning |
|---|---|
| **structurally valid** | All ten files exist. |
| **depth-complete** | Every artifact this depth requires is `complete`. |
| **fully complete** | All ten `complete`. Reusable skeleton. |

### Capture

Capture of *consequential* decisions is continuous and selective.

**Record** a decision that alters architecture, class or depth, system
boundaries, contracts, authority, security or privacy posture, a significant
dependency, persistence or state semantics, an external interface, irreversible
behavior, or the construction path (including a stack the human did not name).

**Do not record** ordinary implementation, bug fixes, refactors, formatting,
naming, or locally reversible work — unless that work changes a consequential
decision.

Git records what changed. DecisionLog records why the architecture became what
it is.

---

Same names across skeletons. Shared language. Not a requirement to recite all of it.
