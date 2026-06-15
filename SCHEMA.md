# 🧬 SCHEMA — The 10-Artifact Architecture Ontology

> This is the **single source of truth** for what an architecture skeleton *is*.
> The README pitches the idea; this file defines it. Skeletons and templates
> reference this document — they never re-define the artifacts themselves.
> When the definition of an artifact changes, it changes **here**, once.

This repo treats architecture as **information, not code**. Any system —
a tool ecosystem, an agent, an event bus, a cognitive cycle — can be fully
described by the same ten artifacts. That uniformity is the whole point:
it makes architectures *comparable, composable, and fillable by any
intelligent entity* (human, Claude, Copilot, GPT, Gemini, Grok, or whatever
comes next).

---

## The Frontmatter Contract

Every artifact file in this repo — template *or* filled — opens with the same
YAML frontmatter. This is the **machine-parseable layer**: it lets an entity
look at a half-finished skeleton and know exactly what to do next without
re-reading prose.

```yaml
---
artifact: Architecture        # one of the 10 canonical names
status: stub                  # stub | partial | complete
order: 1                      # position in the build pipeline (see PIPELINE.md)
fills: "structural blueprint — subsystems, boundaries, data & control flow"
depends_on: []                # artifacts that should exist before this one
filled_by: both               # human | entity | both
last_decision: null           # optional: ref to a DecisionLog entry id
---
```

### Field meanings

| Field | Meaning |
|-------|---------|
| `artifact` | The canonical artifact name. Never invent new ones. |
| `status` | `stub` = structure only; `partial` = some content; `complete` = ready to depend on. |
| `order` | Build-pipeline position. See `PIPELINE.md`. |
| `fills` | One-line statement of what this artifact is responsible for. |
| `depends_on` | Artifacts that should be at least `partial` before this is filled. |
| `filled_by` | Who is expected to author it — guidance, not a lock. |
| `last_decision` | Optional pointer (e.g. `D-003`) into `DecisionLog.md`. |

**Instantiation Rule:** when a skeleton is copied into a new project, *nothing
is optional at the structural level*. All ten files exist from the start as
stubs. A system is only **valid** once every artifact exists; it is **complete**
once every artifact's `status: complete`. Partial filling is allowed — missing
*structure* is not.

---

## The 10 Artifacts

### 1. Architecture — *the city map*
The structural blueprint. Major subsystems, boundaries, data flow, control
flow, high-level diagrams. The heart of the system.

### 2. Flows — *the movie*
The behavioral blueprint. Request flow, event flow, execution flow, error flow,
state-update flow. The most reusable part of any architecture.

### 3. Contracts — *the constitution*
Guarantees, assumptions, invariants, pre/post-conditions. Contracts prevent
architectural drift. *(They come **after** Flows — you can't constrain a
behavior you haven't described. See `DecisionLog` D-001.)*

### 4. Types — *the vocabulary*
Core domain types, shared primitives, enums, identifiers, structural schemas.
The dictionary the architecture speaks.

### 5. Schemas — *the conceptual ontology*
Entity → State → Event → Evaluation → Decision → Action. Cognitive schemas,
information schemas, transformation schemas. Where architectures become
generalizable.

### 6. Interfaces — *the plug points*
Tool interface, evaluator interface, router interface, state-store interface,
execution interface. Interfaces make modules interchangeable.

### 7. Dependencies — *the dependency graph*
Allowed and forbidden dependency directions, module hierarchy, import rules.
This is what prevents entropy.

### 8. Modules — *the organizational chart*
Module list, ownership, responsibilities, boundaries. The decomposition layer.

### 9. DecisionLog — *the architectural memory*
Decisions, alternatives, reasons, dates. This is the artifact that lets
*different intelligences across time* avoid re-litigating settled choices.
Maintained continuously, not in a single pass.

### 10. README — *the front door*
What is this? Why does it exist? What problem does it solve? What are the major
components? The elevator pitch for the instantiated system.

---

## The Artifact Stack (hierarchy of meaning)

```
          ┌──────────────────────┐
          │     Architecture     │   structure
          └──────────┬───────────┘
                     ↓
          ┌──────────────────────┐
          │        Flows         │   behavior
          └──────────┬───────────┘
                     ↓
          ┌──────────────────────┐
          │       Contracts      │   guarantees
          └──────────┬───────────┘
                     ↓
          ┌──────────────────────┐
          │   Types  +  Schemas  │   vocabulary & ontology
          └──────────┬───────────┘
                     ↓
          ┌──────────────────────┐
          │ Interfaces · Deps ·  │   wiring & decomposition
          │ Modules              │
          └──────────────────────┘

  DecisionLog runs vertically through all of it — it records *why*.
```

---

## Cross-Skeleton Compatibility

Because every skeleton uses these exact ten artifacts with the same meaning:

- `Contracts.md` from an Agent system is directly comparable to `Contracts.md`
  in an Event Bus system.
- `Flows.md` are structurally interchangeable across skeletons.
- `Types.md` define a shared language layer across all systems.

This enables **cross-system reasoning and architectural reuse** — the real
payoff of standardization.
