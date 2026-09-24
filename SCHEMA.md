# 🧬 SCHEMA — The 10-Artifact Architecture Ontology

> This is the **single source of truth** for what an architecture skeleton *is*.
> The README pitches the idea; this file defines it. Skeletons and templates
> reference this document — they never re-define the artifacts themselves.
> When the definition of an artifact changes, it changes **here**, once.

This repo treats architecture as **information, not code**. Any system can be
fully described by the same ten artifacts. That uniformity makes architectures
comparable, composable, and fillable by any intelligent entity.

The ontology is fixed. How much of it a given build must *speak* is not — see
[`SELECTOR.md`](SELECTOR.md).

---

## The Frontmatter Contract

Every artifact file — template or filled — opens with the same YAML frontmatter.

```yaml
---
artifact: Architecture        # one of the 10 canonical names
status: stub                  # stub | partial | complete
order: 1                      # position in the build pipeline (see PIPELINE.md)
fills: "structural blueprint — subsystems, boundaries, data & control flow"
depends_on: []                # artifacts that must exist before this one
filled_by: both               # human | entity | both
last_decision: null           # optional: ref to a DecisionLog entry id
---
```

### Field meanings

| Field | Meaning |
|-------|---------|
| `artifact` | The canonical artifact name. Never invent new ones. |
| `status` | `stub` = structure only; `partial` = some content; `complete` = ready to be depended on as finished. |
| `order` | Build-pipeline position. See `PIPELINE.md`. |
| `fills` | One-line statement of what this artifact is responsible for. |
| `depends_on` | See **Dependency rule** below. |
| `filled_by` | Who is expected to author it — guidance, not a lock. |
| `last_decision` | Optional pointer (e.g. `D-003`) into `DecisionLog.md`. |

### Dependency rule (`depends_on`)

Stated once, here. PIPELINE and AGENTS do not invent a second meaning.

- A dependency must be **`partial` or `complete`** before dependent work may begin.
- A dependent artifact may **not** become `complete` while a required dependency remains `stub`.
- `partial` is enough to *start* the next artifact. `complete` is required before the next artifact itself may be marked `complete`.

### Instantiation and the three completeness states

When a skeleton is copied into a new project, *nothing is optional at the
structural level*. All ten files exist from the start as stubs. Missing
*structure* is invalid. Missing *prose* at a depth that does not require it is not.

| State | Meaning |
|---|---|
| **structurally valid** | All ten artifact files exist, each with valid frontmatter. |
| **depth-complete** | Every artifact required by the selected SELECTOR depth is `complete`. The rest may remain `stub` or `partial`. A *build* is done at this state. |
| **fully complete** | All ten artifacts are `status: complete`. Required of a reusable skeleton (`full` depth). Not required of a thin or standard *build*. |

Do not call a thin build incomplete because Types is still `stub`. Do not call a
reusable skeleton complete while Schemas is still `stub`.

### What an INVALID instantiation looks like

- ❌ **Missing artifact.** Only 8 of the 10 files exist. All ten must exist, even if some stay `stub`.
- ❌ **Malformed frontmatter.** Missing YAML, or `status` outside `stub \| partial \| complete`.
- ❌ **Invented artifact name.** The ten names are closed.
- ❌ **Out-of-order completion.** An artifact is `complete` while a `depends_on` target is still `stub`. (Starting work on it while the dependency is `partial` is allowed.)
- ❌ **Silent decision.** A non-obvious choice with no `D-XXX` in `DecisionLog.md`.

---

## The 10 Artifacts

### 1. Architecture — *the city map*
Major subsystems, boundaries, data flow, control flow, high-level diagrams.

### 2. Flows — *the movie*
Request flow, event flow, execution flow, error flow, state-update flow.

### 3. Contracts — *the constitution*
Guarantees, assumptions, invariants, pre/post-conditions. After Flows — you
cannot constrain a behavior you have not described. (`DecisionLog` D-001.)

### 4. Types — *the vocabulary*
Core domain types, shared primitives, enums, identifiers.

### 5. Schemas — *the conceptual ontology*
Entity → State → Event → Evaluation → Decision → Action.

### 6. Interfaces — *the plug points*
The surfaces that make modules interchangeable.

### 7. Dependencies — *the dependency graph*
Allowed and forbidden directions. This is what prevents entropy.

### 8. Modules — *the organizational chart*
Module list, ownership, responsibilities, boundaries.

### 9. DecisionLog — *the architectural memory*
Decisions, alternatives, reasons. Maintained continuously.

### 10. README — *the front door*
What is this, why does it exist, what problem it solves.

---

## The Artifact Stack

```
          Architecture     structure
                 ↓
              Flows        behavior
                 ↓
            Contracts      guarantees
                 ↓
         Types + Schemas   vocabulary
                 ↓
    Interfaces · Deps · Modules

  DecisionLog runs through all of it — it records *why*.
```

---

## Cross-Skeleton Compatibility

Every skeleton uses these exact ten artifacts with the same meaning, so a
`Contracts.md` from an agent is comparable to one from an event bus. That is
the payoff of a shared language — not a requirement that every system recite
the entire language.
