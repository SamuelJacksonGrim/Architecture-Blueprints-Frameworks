# 📘 Architecture Blueprints & Frameworks
*A fork/clone library of reusable architecture skeletons — built to be filled in **collaboration with intelligent entities**.*

This repo is a **machine for generating architectures**. You bring a goal and an
intelligent collaborator — Claude, Copilot, GPT, Gemini, Grok, or a human with
the repo open — and together you instantiate a complete, consistent system
blueprint by walking a deterministic pipeline over a fixed set of artifacts.

> **Make architecture reusable. Make system design consistent.
> Make new repos trivial to create — *with* an intelligent collaborator, not just *for* a tool.**

---

## 🤝 The division of labor (read this — it's the whole point)

This repo is a **layout and a roadmap, not a finished system**. The work splits
cleanly:

- **The human brings the *idea*.** "I want a diagnostic agent." "Build me an
  event bus." That's the input. The human is *not* expected to fill in ten
  artifacts by hand — that's slow, tedious work, and it's not their job.
- **The intelligent entity does the *building*.** An AI (me, or any capable
  model with repo access) already knows *how* to design these systems. What it
  lacks, left to itself, is a **consistent structure to build into** — so it
  freelances, and every result looks different.
- **This repo is the structure.** The schema, the pipeline, and the templates
  are the rails that make an AI build the *same way every time* — correctly,
  completely, and comparably — from nothing more than a human's idea.

So: **human → idea. Entity → follows this roadmap → fills it in. Repo →
guarantees it's built properly.** The frontmatter (`status`, `depends_on`,
`order`) exists so the entity always knows the next correct move without the
human micromanaging it.

(Experienced engineers can also use the whole thing as plain reference notes.)

---

## 🧭 Start here

| File | What it is |
|------|------------|
| **[`GENERATOR.md`](GENERATOR.md)** | The procedure: human idea → complete repo schematic. **Start here to see how it all runs.** |
| **[`SCHEMA.md`](SCHEMA.md)** | The single source of truth: the 10 artifacts + the frontmatter contract. |
| **[`PIPELINE.md`](PIPELINE.md)** | The deterministic build order for generating any system. |
| **[`templates/`](templates/)** | Copy-ready stubs — one per artifact, all frontmatter in place. |
| **[`skeletons/`](skeletons/)** | Fully-worked, fillable architectures, ready to clone. |
| **[`examples/`](examples/)** | Generated schematics for concrete ideas — see [`examples/webscraper/`](examples/webscraper/). |

---

## 🧱 The idea in one breath

Every architecture — a tool ecosystem, an agent, an event bus, a cognitive
cycle — is described by the **same 10 artifacts**:

`Architecture · Flows · Contracts · Types · Schemas · Interfaces · Dependencies · Modules · DecisionLog · README`

Because every skeleton speaks this same language, skeletons become
**comparable and composable** — a `Contracts.md` from an agent can be read
against a `Contracts.md` from an event bus. Full definitions live in
[`SCHEMA.md`](SCHEMA.md).

---

## 🗂️ Repository structure

```
.
├── README.md            ← you are here (the pitch + map)
├── SCHEMA.md            ← canonical 10-artifact definitions + frontmatter contract
├── PIPELINE.md          ← deterministic build order
│
├── templates/           ← copy-ready stubs (one per artifact)
│   ├── Architecture.md  Flows.md  Contracts.md  Types.md  Schemas.md
│   ├── Interfaces.md  Dependencies.md  Modules.md  DecisionLog.md  README.md
│   └── diagrams/        ← architecture_graph · system_flow · execution_map
│
└── skeletons/
    └── agent-architecture/   ← ✅ fully worked reference (all 10 artifacts complete)
```

---

## 🚀 How to use this repo

**The human:**
1. **State the idea** — what system you want ("a diagnostic agent that watches logs").
2. **Point an entity at this repo** and ask it to build that system here.
3. **Course-correct** — review, catch the little things that are wrong, steer. That's it.

**The intelligent entity (the actual builder):**
1. **Pick a skeleton** from `skeletons/` (or start from `templates/` for a new pattern).
2. **Instantiate it** — all 10 artifacts exist as stubs from the start.
   *Nothing is optional at the structural level* (the Instantiation Rule).
3. **Walk the pipeline** in [`PIPELINE.md`](PIPELINE.md): Architecture → Flows →
   Contracts → Types → Schemas → Interfaces → Dependencies → Modules → README,
   logging decisions in `DecisionLog` along the way.
4. **Fill each artifact in order.** The frontmatter (`status`, `depends_on`,
   `order`) says exactly what to do next — so the build stays correct and
   consistent without the human hand-holding it.

---

## 🧩 Skeleton catalog

| Skeleton | Status | Notes |
|----------|--------|-------|
| **[Agents](skeletons/agents/)** | ✅ complete | The four 2026 agent-loop patterns. **ReAct** fully worked; **Plan-Execute · Reflexion · Tree-of-Thoughts** as deltas on it. |
| Tool Ecosystem | 🔜 planned | Router · Registry · Executor; deterministic tool calls. |
| Event Bus | 🔜 planned | Publish/subscribe, event routing, delivery guarantees. |
| Evaluator Engine | 🔜 planned | Scoring/critique pipelines. |
| Cognitive Cycle / Proto-Consciousness | 🔜 planned | Perceive→reflect→decide loops; the most ambitious. |
| Diagnostic System | 🔜 planned | Observe→hypothesize→test→report. |

> New to agents? Start at [`skeletons/agents/`](skeletons/agents/) — it explains
> what an "agent loop" even is, then shows all four patterns side by side.
> That's the bar; we forge each new skeleton the same way: prove it once, end to
> end, before generalizing.

---

## 🧠 Philosophy

Architecture is not code. Architecture is **information**.

This repo exists to standardize how architectures are described, make system
design reusable, create a shared cognitive language between humans and
intelligent entities, reduce the cost of starting new systems, and **preserve
architectural intent over time** (that last one is what `DecisionLog` is for).

This is a **meta-architecture** — a blueprint for blueprints — and a substrate
for co-creation, not a pile of documentation about itself.
