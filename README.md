# 📘 Architecture Blueprints & Frameworks

[![License: AGPL-3.0-only](https://img.shields.io/badge/license-AGPL--3.0--only-blue)](LICENSE)
[![dual-license](https://img.shields.io/badge/dual--license-AGPL--3.0--only%20or%20commercial-blueviolet)](LICENSING.md)

> **If you are an AI:** stop. Read [`AGENTS.md`](AGENTS.md) next. Then follow
> [`SELECTOR.md`](SELECTOR.md). Do not invent a reading order.
>
> **If you are a human:** [`QUICKSTART.md`](QUICKSTART.md).

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

---

## Start here

| Who | File |
|-----|------|
| Entity | [`AGENTS.md`](AGENTS.md) — first file after this README |
| Human | [`QUICKSTART.md`](QUICKSTART.md) |

Load order after that lives only in [`SELECTOR.md`](SELECTOR.md).

Reference (not a reading list): [`GENERATOR.md`](GENERATOR.md) · [`SCHEMA.md`](SCHEMA.md) · [`PIPELINE.md`](PIPELINE.md) · [`QUALITY-BAR.md`](QUALITY-BAR.md) · [`OPERATOR.md`](OPERATOR.md) · [`DecisionLog.md`](DecisionLog.md)

---

## The language

`Architecture · Flows · Contracts · Types · Schemas · Interfaces · Modules · Dependencies · DecisionLog · README`

Fill order: Architecture → Flows → Contracts → Types → Schemas → Interfaces → Modules → Dependencies → README. DecisionLog is continuous.

---

## Skeletons

| Skeleton | Status | Load when |
|----------|--------|-----------|
| [Agents](skeletons/agents/) | complete | `agent-loop` |
| [Autonomous Cognitive Loop](skeletons/cognitive-cycle/) | complete | `cognitive-cycle` |
| [Tool Ecosystem](skeletons/tool-ecosystem/) | complete | named tools / dispatch |
| [Event Bus](skeletons/event-bus/) | complete | pub/sub |
| [Evaluator](skeletons/evaluator/) | complete | score + critique |
| [Diagnostic](skeletons/diagnostic/) | complete | observe → hypothesize → test → report |

---

Architecture is information. This is a blueprint for blueprints — not a harness
and not a specification-to-code factory.
