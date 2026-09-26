# Architecture Blueprints & Frameworks

[![License: AGPL-3.0-only](https://img.shields.io/badge/license-AGPL--3.0--only-blue)](LICENSE)
[![dual-license](https://img.shields.io/badge/dual--license-AGPL--3.0--only%20or%20commercial-blueviolet)](LICENSING.md)

> **If you are an AI:** stop. Read [`AGENTS.md`](AGENTS.md) next. Then follow
> [`SELECTOR.md`](SELECTOR.md). The artifacts are a workspace, not a queue.
>
> **If you are a human:** [`QUICKSTART.md`](QUICKSTART.md).

## License

Dual-licensed: [AGPL-3.0-only](LICENSE) or [commercial](COMMERCIAL-LICENSE.md).
See [LICENSING.md](LICENSING.md) and [NOTICE](NOTICE).

*A language and a workspace so an AI can design what you asked for — and you
can see why. Not a procedure the AI must ask permission to walk.*

You describe intent. The AI reasons, chooses an architecture, writes the code,
and tells you whether the main path ran. You keep authority. You do not have
to invent the design.

---

## Who does what

| | Supplies | Does not have to |
|---|---|---|
| **You** | Intent. Final authority. | Author the architecture. Supervise each artifact. |
| **The AI** | Reasoning, architecture, implementation, verification status. | Hide a consequential decision. Emit a turn per file. |
| **This repo** | Vocabulary, completeness graph, depth, inspectability. | A path through the vocabulary. A committee. A score. |

---

## Start here

| Who | File |
|-----|------|
| Entity | [`AGENTS.md`](AGENTS.md) |
| Human | [`QUICKSTART.md`](QUICKSTART.md) |

What the entity *reads of this repo* lives only in [`SELECTOR.md`](SELECTOR.md).

Reference: [`GENERATOR.md`](GENERATOR.md) · [`SCHEMA.md`](SCHEMA.md) · [`PIPELINE.md`](PIPELINE.md) (completeness graph) · [`QUALITY-BAR.md`](QUALITY-BAR.md) · [`OPERATOR.md`](OPERATOR.md) · [`DecisionLog.md`](DecisionLog.md)

---

## The language

`Architecture · Flows · Contracts · Types · Schemas · Interfaces · Modules · Dependencies · DecisionLog · README`

A network. DecisionLog is continuous and selective. Depth decides how much of
the network must be persisted. Traversal is free.

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

Architecture is information. This is a blueprint for blueprints — a cognitive
environment, not a harness and not a specification-to-code factory.
