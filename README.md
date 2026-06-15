# 📘 Architecture Blueprints & Frameworks
*A roadmap that lets an AI build what you ask for **right** — not vibe-coded.*

**You don't need to know how to code. You don't need to know what any of the
words in here mean.** You describe what you want in plain English; an
intelligent entity — Claude, Copilot, GPT, Gemini, Grok — reads this repo and
builds it for you, properly, end to end.

This repo is the **roadmap the AI follows** so that "build me a thing" turns into
a real, correctly-structured project instead of a pile of guesses.

> **Describe it in plain words. The AI builds it right. The repo is what keeps
> it honest.**

---

## 🤝 Who does what (read this — it's the whole point)

- **You bring the *idea*, in plain language.** *"I want an app that tracks my
  plants' watering schedules."* That's all you do. You write no code, you read
  no files in here, and you never need to know what a "type" or a "schema" is.
- **The AI does *everything else* — design *and* the actual code.** A capable
  model already knows *how* to build software. What it lacks, left alone, is a
  **structure to build into** — so it improvises, forgets pieces, and
  vibe-codes. The result is shaky, especially for someone who can't tell good
  code from bad.
- **This repo is that structure.** It's a checklist the AI fills out *for
  itself* before and while it builds — what the pieces are, how they connect,
  what must stay true. Those notes (Types, Flows, Contracts…) aren't for you;
  they're how the AI makes sure it builds the *right* thing the *right* way,
  every time.

So: **you → idea. AI → reads this roadmap → designs it, then writes all the
code. Repo → guarantees it's built with precision instead of vibe-coded.**

> ### 🙋 "But I don't know what any of these files are."
> You don't have to. The ten artifacts, the frontmatter, the pipeline — that's
> the AI's instrument panel, not yours. Your whole job is to say what you want
> and, when it shows you the result, tell it whether that's the thing you meant.

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
├── GENERATOR.md         ← the procedure: your idea → finished build
├── SCHEMA.md            ← canonical 10-artifact definitions + frontmatter contract
├── PIPELINE.md          ← deterministic build order
│
├── templates/           ← copy-ready stubs (one per artifact)
│   ├── Architecture.md  Flows.md  Contracts.md  Types.md  Schemas.md
│   ├── Interfaces.md  Dependencies.md  Modules.md  DecisionLog.md  README.md
│   └── diagrams/        ← architecture_graph · system_flow · execution_map
│
├── skeletons/           ← reusable patterns
│   └── agents/          ← ✅ ReAct · Plan-Execute · Reflexion · Tree-of-Thoughts · Guarded
│
└── examples/            ← full generated builds for concrete ideas
    └── webscraper/      ← ✅ the whole procedure run on one plain-English request
```

---

## 🚀 How to use this repo

**Your whole job (no coding, no jargon):**
1. **Say what you want**, in plain words: *"build me an app that tracks my
   plants' watering schedules."*
2. **Point an AI at this repo** and ask it to build that.
3. **Look at what it shows you** and say whether it's the thing you meant. Done.

**What the AI does (the actual building):**
1. **Picks a starting point** — a pattern from `skeletons/`, or the blank
   `templates/` for anything new.
2. **Instantiates it** — all 10 design notes exist as stubs from the start.
   *Nothing is optional at the structural level* (the Instantiation Rule).
3. **Walks the pipeline** in [`PIPELINE.md`](PIPELINE.md): Architecture → Flows →
   Contracts → Types → Schemas → Interfaces → Dependencies → Modules → README,
   recording its reasoning in `DecisionLog`.
4. **Fills each note in order**, then **derives the folder/file tree and writes
   the actual code** against it. Because every piece, connection, and rule was
   pinned down first, the code comes out *precise* — not vibe-coded.

The full step-by-step the AI follows is in **[`GENERATOR.md`](GENERATOR.md)**, and
**[`examples/webscraper/`](examples/webscraper/)** shows the whole thing run once
on a single plain-English request.

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
