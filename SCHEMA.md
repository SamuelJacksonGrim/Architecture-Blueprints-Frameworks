# 🧬 SCHEMA — The 10-Artifact Architecture Ontology

> Single source of truth for what a skeleton *is*. Fill *order* is `PIPELINE.md`.
> How much to speak is `SELECTOR.md`.

Architecture is information, not code. The ten names are closed. The amount of
language a build must speak is not.

---

## The Frontmatter Contract

```yaml
---
artifact: Architecture
status: stub                  # stub | partial | complete
order: 1
fills: "structural blueprint"
depends_on: []
filled_by: both
last_decision: null
---
```

### Dependency rule (`depends_on`)

Stated once, here.

- A dependency must be **`partial` or `complete`** before dependent work may begin.
- A dependent artifact may **not** become `complete` while a required dependency remains `stub`.
- `partial` is enough to *start*. `complete` is required before the next artifact may itself be marked `complete`.

### Three completeness states

| State | Meaning |
|---|---|
| **structurally valid** | All ten files exist, valid frontmatter. |
| **depth-complete** | Every artifact the selected depth requires is `complete`. A *build* is done. |
| **fully complete** | All ten are `complete`. Required of a reusable skeleton. |

### Invalid

Missing file. Bad frontmatter. Invented artifact name. `complete` while a `depends_on` target is still `stub`. Silent decision (including a hidden stack).

---

## The 10 Artifacts (fill order)

1. Architecture — city map
2. Flows — the movie
3. Contracts — constitution (after Flows; D-001)
4. Types — vocabulary
5. Schemas — ontology
6. Interfaces — plug points
7. Modules — named pieces that implement those plugs
8. Dependencies — allowed/forbidden edges between those modules (after Modules; D-005)
9. DecisionLog — memory, continuous
10. README — front door

```
Architecture → Flows → Contracts → Types + Schemas
         → Interfaces → Modules → Dependencies
DecisionLog runs through all of it.
```

The ten *names* did not change. Only the fill order of Modules vs Dependencies.

---

## Cross-Skeleton Compatibility

Same ten names, same meanings. Shared language. Not a requirement to recite all of it.
