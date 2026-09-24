# 📘 Architecture Blueprints & Frameworks

[![License: AGPL-3.0-only](https://img.shields.io/badge/license-AGPL--3.0--only-blue)](LICENSE)
[![dual-license](https://img.shields.io/badge/dual--license-AGPL--3.0--only%20or%20commercial-blueviolet)](LICENSING.md)

## License

This project is dual-licensed under **AGPL-3.0-only** OR a commercial license.

- [LICENSE](LICENSE) — GNU AGPL-3.0-only (the free track)
- [LICENSING.md](LICENSING.md) — how the two tracks work
- [COMMERCIAL-LICENSE.md](COMMERCIAL-LICENSE.md) — the commercial agreement
- [NOTICE](NOTICE) — copyright, SPDX identifier, and provenance

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
  what must stay true. Those notes aren't for you; they're how the AI stays
  honest. It only fills them as deep as the thing actually needs.

So: **you → idea. AI → reads this roadmap → designs it, then writes all the
code. Repo → guarantees it's built with precision instead of vibe-coded.**

> ### 🙋 "But I don't know what any of these files are."
> You don't have to. The ten artifacts, the frontmatter, the pipeline — that's
> the AI's instrument panel, not yours. Your whole job is to say what you want
> and, when it shows you the result, tell it whether that's the thing you meant.

> 💡 **One habit that changes everything:** ask the AI *what it would change.*
> See [`COLLABORATION.md`](COLLABORATION.md).

---

## 🧭 Start here

| File | What it is |
|------|------------|
| **[`QUICKSTART.md`](QUICKSTART.md)** | 🟢 **New here? Start here.** The whole workflow in plain terms. |
| **[`AGENTS.md`](AGENTS.md)** | What an AI reads automatically when pointed at this repo. |
| **[`SELECTOR.md`](SELECTOR.md)** | Classify the idea, pick a depth, load only what you need. |
| **[`OPERATOR.md`](OPERATOR.md)** | Optional: how to split work across more than one model. Not required. |
| **[`GENERATOR.md`](GENERATOR.md)** | The procedure an AI follows: idea → design → code. |
| **[`SCHEMA.md`](SCHEMA.md)** | The 10 artifacts + the frontmatter contract. |
| **[`PIPELINE.md`](PIPELINE.md)** | Build order + non-negotiable rules. |
| **[`DecisionLog.md`](DecisionLog.md)** | Why this repo itself made the calls it made. |
| **[`QUALITY-BAR.md`](QUALITY-BAR.md)** | The rigor "complete" must reach. |
| **[`templates/`](templates/)** | Copy-ready stubs, including the Intent Card. |
| **[`skeletons/`](skeletons/)** | Reusable patterns. |
| **[`examples/`](examples/)** | Worked schematics — design-only unless the folder says otherwise. |
| **[`CONTRIBUTING.md`](CONTRIBUTING.md)** | How to add a skeleton without breaking consistency. |
| **[`COLLABORATION.md`](COLLABORATION.md)** | Invite the AI into the design space. |

---

## 🧱 The idea in one breath

Every architecture is described by the **same 10 artifacts**:

`Architecture · Flows · Contracts · Types · Schemas · Interfaces · Dependencies · Modules · DecisionLog · README`

Because every system speaks this same language, they become comparable and
composable.

Not every system needs every sentence of that language spoken out loud.
[`SELECTOR.md`](SELECTOR.md) picks a depth so a CLI does not receive a
constitution meant for a multi-service agent.

---

## 📚 Learn the 10 building blocks (teaching section)

> You don't *need* to know any of this to use the repo. Precise definitions live
> in [`SCHEMA.md`](SCHEMA.md).

| # | Artifact | Metaphor | The question it answers |
|---|----------|----------|--------------------------|
| 1 | **Architecture** | the city map | What are the big pieces, and how are they laid out? |
| 2 | **Flows** | the movie | What actually *happens*, step by step, when it runs? |
| 3 | **Contracts** | the constitution | What must *always* be true? What's promised? |
| 4 | **Types** | the vocabulary | What are the "things" the system talks about? |
| 5 | **Schemas** | the conceptual map | How do those things relate and change? |
| 6 | **Interfaces** | the plug sockets | How do the pieces connect so one can be swapped out? |
| 7 | **Dependencies** | the wiring rules | What's allowed to rely on what? |
| 8 | **Modules** | the org chart | What are the pieces, and who's responsible for what? |
| 9 | **DecisionLog** | the diary | What choices were made, and *why*? |
| 10 | **README** | the front door | What is this, and why does it exist? |

The AI fills these **top to bottom**, only as far as the chosen depth requires.
See [`PIPELINE.md`](PIPELINE.md) and [`SELECTOR.md`](SELECTOR.md).

---

## 🚀 How to use this repo

**Your whole job:**
1. Say what you want, in plain words.
2. Point an AI at this repo and ask it to build that.
3. Look at what it shows you. Say whether it's the thing you meant.

Optional four lines if you already know them: Want / Must not / Runs where / Done when.

**What the AI does:**
1. Reads `SELECTOR.md` — class, depth, Intent Card.
2. Instantiates all 10 stubs + `INTENT.md`.
3. Fills only what that depth requires, in pipeline order, against `QUALITY-BAR.md`.
4. Writes code it can trace to those notes, then smoke-tests — or says it could not.

If you have more than one model and want to split the work, read [`OPERATOR.md`](OPERATOR.md).
A single model is enough.

---

## 🧩 Skeleton catalog

| Skeleton | Status | Notes |
|----------|--------|-------|
| **[Agents](skeletons/agents/)** | ✅ complete | ReAct baseline; Plan-Execute · Reflexion · Tree-of-Thoughts as deltas; Guarded overlay. |
| **[Autonomous Cognitive Loop](skeletons/cognitive-cycle/)** | ✅ complete | Continuous self-governing loop. |
| Tool Ecosystem | 🕛 planned | Router · Registry · Executor. |
| Event Bus | 🕛 planned | Publish/subscribe. |
| Evaluator Engine | 🕛 planned | Scoring/critique pipelines. |
| Diagnostic System | 🕛 planned | Observe→hypothesize→test→report. |

---

## 🧠 Philosophy

Architecture is not code. Architecture is **information**.

This repo exists to standardize how architectures are described, make system
design reusable, create a shared language between humans and models, reduce the
cost of starting, and **preserve intent over time** (`DecisionLog`).

This is a meta-architecture — a blueprint for blueprints — not a pile of
process prompts and not an operating system for a coding harness.
