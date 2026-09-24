# 🧬 SCHEMA — The 10-Artifact Architecture Ontology

Fill *order* is `PIPELINE.md`. How much to speak is `SELECTOR.md`.

The ten names are closed. How much of the language a build must speak is not.

---

## Frontmatter

```yaml
---
artifact: Architecture
status: stub                  # stub | partial | complete
order: 1                      # sequential artifacts only; DecisionLog is 99
fills: "structural blueprint"
depends_on: []
filled_by: both
last_decision: null
---
```

### Dependency rule

- A dependency must be `partial` or `complete` before dependent work may begin.
- A dependent artifact may not become `complete` while a required dependency remains `stub`.

### Depth self-consistency

An artifact required `complete` at a given depth may only `depends_on` artifacts
that same depth also requires `complete`. Otherwise the depth cannot finish.

### Three states

| State | Meaning |
|---|---|
| **structurally valid** | All ten files exist. |
| **depth-complete** | Every artifact this depth requires is `complete`. A build is done. |
| **fully complete** | All ten `complete`. Reusable skeleton. |

### Construction vs capture

Sequential artifacts have an order. **DecisionLog does not.** Construction is
sequential. Capture is **continuous and selective**.

You may decide freely. You may not hide a consequential decision.
You do not write an entry for every change.

**Record** a decision that alters architecture, class or depth, system
boundaries, contracts, authority, security or privacy posture, a significant
dependency, persistence or state semantics, an external interface, irreversible
behavior, or the construction path (including a stack the human did not name).

**Do not record** ordinary implementation, bug fixes, refactors, formatting,
naming, or other locally reversible work — unless that work changes a
consequential decision.

Git records what changed. DecisionLog records why the architecture became what
it is. There is no eleventh artifact for the rest.

Writing DecisionLog only at the end is a failure. Writing it for every edit is
also a failure.

---

## The 10 artifacts

Sequential: Architecture → Flows → Contracts → Types → Schemas → Interfaces → Modules → Dependencies → README.

Continuous and selective: DecisionLog.

---

Same names across skeletons. Shared language. Not a requirement to recite all of it.
