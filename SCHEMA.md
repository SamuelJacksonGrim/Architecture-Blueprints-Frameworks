# SCHEMA — the 10-artifact workspace

The ten names are a **network of representations**. They are handles for
thinking. They are not stations on a line.

How much of the language a build must *persist* is [`SELECTOR.md`](SELECTOR.md).
When an artifact may be called `complete` is `depends_on`, below.
The path through the network is free.

---

## Frontmatter

```yaml
---
artifact: Architecture
status: stub                  # stub | partial | complete
order: 1                      # reading hint, not a queue
fills: "structural blueprint"
depends_on: []
filled_by: both
last_decision: null
---
```

### Dependency rule (completeness, not cognition)

- A dependency must be `partial` or `complete` before the dependent artifact
  may itself be marked `complete`.
- Work, draft, and revision on any artifact may happen at any time.
- `depends_on` does not authorize a thought. It does not demand an emission.

### Depth self-consistency

An artifact required `complete` at a given depth may only `depends_on` artifacts
that same depth also requires `complete`.

### Three states

| State | Meaning |
|---|---|
| **structurally valid** | All ten files exist — the workspace is instantiated. |
| **depth-complete** | Every artifact this depth requires is `complete`. A build is done. |
| **fully complete** | All ten `complete`. Reusable skeleton. |

### Construction vs capture

There is no required construction sequence. Capture of *consequential*
decisions is continuous and selective.

**Record** a decision that alters architecture, class or depth, system
boundaries, contracts, authority, security or privacy posture, a significant
dependency, persistence or state semantics, an external interface, irreversible
behavior, or the construction path (including a stack the human did not name).

**Do not record** ordinary implementation, bug fixes, refactors, formatting,
naming, or locally reversible work — unless that work changes a consequential
decision.

Git records what changed. DecisionLog records why the architecture became what
it is. There is no eleventh artifact for the rest.

Writing DecisionLog only at the end is a failure. Writing it for every edit
or every thought is also a failure.

---

## The 10 artifacts

A network, not a line: Architecture, Flows, Contracts, Types, Schemas,
Interfaces, Modules, Dependencies, README. DecisionLog is available at any time.

Changing your mind about an earlier artifact is reasoning, not workflow failure.

---

Same names across skeletons. Shared language. Not a requirement to recite all of it.
