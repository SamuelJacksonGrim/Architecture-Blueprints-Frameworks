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
| **[`QUICKSTART.md`](QUICKSTART.md)** | 🟢 **New here? Start here.** The whole workflow + a copy-paste prompt. |
| **[`GENERATOR.md`](GENERATOR.md)** | The procedure an AI follows: idea → design → code. |
| **[`SCHEMA.md`](SCHEMA.md)** | The single source of truth: the 10 artifacts + the frontmatter contract. |
| **[`PIPELINE.md`](PIPELINE.md)** | The deterministic build order + the **Non-Negotiable Rules**. |
| **[`prompts/`](prompts/)** | A ready-to-paste system prompt that primes any model with the full contract. |
| **[`templates/`](templates/)** | Copy-ready stubs — one per artifact, all frontmatter in place. |
| **[`skeletons/`](skeletons/)** | Reusable patterns — see [`skeletons/agents/`](skeletons/agents/). |
| **[`examples/`](examples/)** | Full generated builds for concrete ideas — see [`examples/webscraper/`](examples/webscraper/). |
| **[`CONTRIBUTING.md`](CONTRIBUTING.md)** | How to add a skeleton/variant/example without breaking consistency. |

---

## 🧱 The idea in one breath

Every architecture — a tool ecosystem, an agent, an event bus, a cognitive
cycle — is described by the **same 10 artifacts**:

`Architecture · Flows · Contracts · Types · Schemas · Interfaces · Dependencies · Modules · DecisionLog · README`

Because every system speaks this same language, they become **comparable and
composable** — a `Contracts.md` from an agent can be read against a
`Contracts.md` from an event bus.

---

## 📚 Learn the 10 building blocks (teaching section)

> **This repo is also a teaching tool.** You don't *need* to know any of this to
> use it — but if you're curious what the AI is actually thinking about when it
> builds your idea, here's every piece in plain language. (The precise,
> machine-facing versions live in [`SCHEMA.md`](SCHEMA.md).)
>
> Every piece of software, no matter what it does, can be described by these ten
> things. Think of building software like building a house:

| # | Artifact | Metaphor | The question it answers |
|---|----------|----------|--------------------------|
| 1 | **Architecture** | the city map | What are the big pieces, and how are they laid out? |
| 2 | **Flows** | the movie | What actually *happens*, step by step, when it runs? |
| 3 | **Contracts** | the constitution | What must *always* be true? What's promised? |
| 4 | **Types** | the vocabulary | What are the "things" the system talks about? (a User, a Price…) |
| 5 | **Schemas** | the conceptual map | How do those things relate and change? |
| 6 | **Interfaces** | the plug sockets | How do the pieces connect so one can be swapped out? |
| 7 | **Dependencies** | the wiring rules | What's allowed to rely on what? (so it doesn't tangle) |
| 8 | **Modules** | the org chart | What are the pieces, and who's responsible for what? |
| 9 | **DecisionLog** | the diary | What choices were made, and *why*? (so nobody re-argues them) |
| 10 | **README** | the front door | What is this, and why does it exist? |

### How they stack (each layer rests on the one above)

```
          ┌──────────────────────┐
          │  1  Architecture     │   the structure
          └──────────┬───────────┘
                     ↓
          ┌──────────────────────┐
          │  2  Flows            │   the behavior
          └──────────┬───────────┘
                     ↓
          ┌──────────────────────┐
          │  3  Contracts        │   the guarantees
          └──────────┬───────────┘
                     ↓
          ┌──────────────────────┐
          │  4 Types · 5 Schemas │   the vocabulary
          └──────────┬───────────┘
                     ↓
          ┌──────────────────────┐
          │ 6 Interfaces ·       │   the wiring &
          │ 7 Deps · 8 Modules   │   decomposition
          └──────────────────────┘

   9 DecisionLog runs through all of it — it records *why*.
   10 README is the front door visitors read first.
```

> **Why this order matters:** you can't promise what a thing does (Contracts)
> until you've described what it does (Flows); you can't describe that until you
> know its big pieces (Architecture). The AI builds top-to-bottom for exactly
> that reason — see [`PIPELINE.md`](PIPELINE.md).

### The journey: from your words to working software

```
   YOU                    THE AI (following this repo)                RESULT
  ─────                   ────────────────────────────               ────────
 "build me   ─────▶   1. pick a starting pattern                 
  a thing                2. fill the 10 building blocks  ───────▶   a real,
  that does                 (the design above), in order            working,
  X"                     3. lay out the folders/files              correctly-
                         4. write the code to match the design ─▶  built
 (plain words)           5. show you what it does, plainly         project
       ▲                                                              │
       └──────────  "that's it" / "not quite, I meant…"  ◀───────────┘
```

You stay on the left and the right. Everything in the middle is the AI's job —
and this repo is what makes the middle come out *right* every time.

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
