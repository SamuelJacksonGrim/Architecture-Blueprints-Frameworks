# 📘 Architecture Blueprints & Frameworks
*A fork/clone library of reusable architecture skeletons — built to be filled in **collaboration with intelligent entities**.*

This repo is a **machine for generating architectures**. You bring a goal and an
intelligent collaborator — Claude, Copilot, GPT, Gemini, Grok, or a human with
the repo open — and together you instantiate a complete, consistent system
blueprint by walking a deterministic pipeline over a fixed set of artifacts.

> **Make architecture reusable. Make system design consistent.
> Make new repos trivial to create — *with* an intelligent collaborator, not just *for* a tool.**

---

## 🤝 Who this is for

The primary consumer is a **collaborative loop**: a person who wants to build
something, working with one or more intelligent entities that have access to
their repo. The structure here is the **shared contract** between them — prose
clear enough for a human, frontmatter structured enough for an entity to read,
fill, and validate. (Experienced engineers can also use it as plain reference
notes.)

---

## 🧭 Start here

| File | What it is |
|------|------------|
| **[`SCHEMA.md`](SCHEMA.md)** | The single source of truth: the 10 artifacts + the frontmatter contract. |
| **[`PIPELINE.md`](PIPELINE.md)** | The deterministic build order for generating any system. |
| **[`templates/`](templates/)** | Copy-ready stubs — one per artifact, all frontmatter in place. |
| **[`skeletons/`](skeletons/)** | Fully-worked, fillable architectures, ready to clone. |

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

1. **Pick a skeleton** from `skeletons/` (or start from `templates/` for a new pattern).
2. **Copy it** into your new repo — all 10 artifacts come with it as stubs.
   *Nothing is optional at the structural level* (the Instantiation Rule).
3. **Walk the pipeline** in [`PIPELINE.md`](PIPELINE.md): Architecture → Flows →
   Contracts → Types → Schemas → Interfaces → Dependencies → Modules → README,
   logging decisions as you go.
4. **Fill with your collaborator.** Each artifact's frontmatter (`status`,
   `depends_on`, `order`) tells any intelligent entity exactly what to do next.

---

## 🧩 Skeleton catalog

| Skeleton | Status | Notes |
|----------|--------|-------|
| **Agent Architecture** | ✅ complete | The worked reference — bounded loop, evaluator gate, memory tiers. |
| Tool Ecosystem | 🔜 planned | Router · Registry · Executor; deterministic tool calls. |
| Event Bus | 🔜 planned | Publish/subscribe, event routing, delivery guarantees. |
| Evaluator Engine | 🔜 planned | Scoring/critique pipelines. |
| Cognitive Cycle / Proto-Consciousness | 🔜 planned | Perceive→reflect→decide loops; the most ambitious. |
| Diagnostic System | 🔜 planned | Observe→hypothesize→test→report. |

> Want one of these next? Open the Agent skeleton to see the bar, then we forge
> the next one the same way: prove it once, end to end, before generalizing.

---

## 🧠 Philosophy

Architecture is not code. Architecture is **information**.

This repo exists to standardize how architectures are described, make system
design reusable, create a shared cognitive language between humans and
intelligent entities, reduce the cost of starting new systems, and **preserve
architectural intent over time** (that last one is what `DecisionLog` is for).

This is a **meta-architecture** — a blueprint for blueprints — and a substrate
for co-creation, not a pile of documentation about itself.
