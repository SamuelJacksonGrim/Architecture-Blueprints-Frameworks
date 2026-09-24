# 📘 Architecture Blueprints & Frameworks

[![License: AGPL-3.0-only](https://img.shields.io/badge/license-AGPL--3.0--only-blue)](LICENSE)
[![dual-license](https://img.shields.io/badge/dual--license-AGPL--3.0--only%20or%20commercial-blueviolet)](LICENSING.md)

## License

Dual-licensed: [AGPL-3.0-only](LICENSE) or [commercial](COMMERCIAL-LICENSE.md).
See [LICENSING.md](LICENSING.md) and [NOTICE](NOTICE).

*A language and an evidence standard so an AI can design what you asked for —
and you can see why.*

You describe intent in plain English. The AI reasons, chooses an architecture,
writes the code, and tells you whether the main path actually ran. You keep the
right to accept, reject, or redirect. You do not have to invent the design.

---

## Who does what

| | Supplies | Does not have to |
|---|---|---|
| **You** | Intent. Final authority. | Author the architecture. |
| **The AI** | Reasoning, architecture, implementation, verification status. | Hide a decision. Wait for your blueprint. |
| **This repo** | Vocabulary, fill order, depth, inspectability. | A stack, a committee, a score. |

Useful surprise is allowed. "Is this what I meant?" is authority, not a demand
that the AI reproduced a design you already had in your head.

---

## Start here

| File | What it is |
|------|------------|
| [`QUICKSTART.md`](QUICKSTART.md) | Three steps. |
| [`AGENTS.md`](AGENTS.md) | What the AI reads. |
| [`SELECTOR.md`](SELECTOR.md) | Class, depth, load list. |
| [`OPERATOR.md`](OPERATOR.md) | Optional multi-model seams. |
| [`GENERATOR.md`](GENERATOR.md) | After SELECTOR: instantiate, fill, code, test. |
| [`SCHEMA.md`](SCHEMA.md) | The ten artifacts. |
| [`PIPELINE.md`](PIPELINE.md) | Fill order. |
| [`DecisionLog.md`](DecisionLog.md) | Why this repo made its calls. |
| [`QUALITY-BAR.md`](QUALITY-BAR.md) | Rubric when calling something complete. |

---

## The language

`Architecture · Flows · Contracts · Types · Schemas · Interfaces · Modules · Dependencies · DecisionLog · README`

Not every system speaks every sentence. SELECTOR picks how much.

Fill order: Architecture → Flows → Contracts → Types → Schemas → Interfaces → Modules → Dependencies → README. DecisionLog is continuous.

---

## How to use it

1. Say what you want.
2. Point an AI at this repo.
3. Read what it built and whether it ran. Keep or send it back.

The AI chooses class and depth. You may override. You should not have to name them first.

---

## Skeletons

| Skeleton | Status |
|----------|--------|
| [Agents](skeletons/agents/) | complete |
| [Autonomous Cognitive Loop](skeletons/cognitive-cycle/) | complete |
| Tool Ecosystem / Event Bus / Evaluator / Diagnostic | planned |

---

Architecture is information. This is a blueprint for blueprints — not a harness
and not a specification-to-code factory.
