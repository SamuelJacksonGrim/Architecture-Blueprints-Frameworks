# Architecture Blueprints & Frameworks

[![License: AGPL-3.0-only](https://img.shields.io/badge/license-AGPL--3.0--only-blue)](LICENSE)
[![dual-license](https://img.shields.io/badge/dual--license-AGPL--3.0--only%20or%20commercial-blueviolet)](LICENSING.md)

> **If you are an AI:** read [`AGENTS.md`](AGENTS.md), then [`SELECTOR.md`](SELECTOR.md).
> Build the pass. Do not stop for approval between artifacts.
>
> **If you are a human:** [`QUICKSTART.md`](QUICKSTART.md).

## License

Dual-licensed: [AGPL-3.0-only](LICENSE) or [commercial](COMMERCIAL-LICENSE.md).
See [LICENSING.md](LICENSING.md) and [NOTICE](NOTICE).

You specify intent. The AI runs the construction process and returns artifacts,
implementation, tests, and evidence. You inspect. You keep authority. You do
not have to invent the design, and you do not have to sign each file.

**Intent → autonomous construction → inspection / evidence → your decision.**

Human authority does not mean continuous supervision.
Finishing the pass does not move authority to the AI.

---

## Who does what

| | Supplies | Does not have to |
|---|---|---|
| **You** | Intent. Final authority after the pass. | Author the architecture. Approve each artifact. |
| **The AI** | The construction pass: architecture, implementation, evidence. | Hide a consequential decision. Ask permission between files. |
| **This repo** | Language, construction order, depth, inspectability. | A committee. A score. A gate per artifact. |

---

## Start here

| Who | File |
|-----|------|
| Entity | [`AGENTS.md`](AGENTS.md) |
| Human | [`QUICKSTART.md`](QUICKSTART.md) |

What the entity reads of this repo: [`SELECTOR.md`](SELECTOR.md).

Reference: [`GENERATOR.md`](GENERATOR.md) · [`SCHEMA.md`](SCHEMA.md) · [`PIPELINE.md`](PIPELINE.md) · [`QUALITY-BAR.md`](QUALITY-BAR.md) · [`OPERATOR.md`](OPERATOR.md) · [`DecisionLog.md`](DecisionLog.md)

---

## The language

`Architecture · Flows · Contracts · Types · Schemas · Interfaces · Modules · Dependencies · DecisionLog · README`

Construction order is PIPELINE. Depth decides how much of that order must be
persisted. DecisionLog is continuous and selective.

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

Architecture is information. A blueprint for blueprints — not a harness, not a
spec-to-code factory, not a permission queue.
