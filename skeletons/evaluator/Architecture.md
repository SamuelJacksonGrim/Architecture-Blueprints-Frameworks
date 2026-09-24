---
artifact: Architecture
status: complete
order: 1
fills: "subject, rubric, scorer, critique"
depends_on: []
filled_by: both
last_decision: D-001
---

# Architecture — Evaluator

## Purpose
Take a subject and a rubric, produce a score and a critique, change nothing else.

## Major Subsystems
- **Rubric store** — named criteria, weights, pass threshold.
- **Subject adapter** — read-only view of the thing being judged.
- **Scorer** — the single authority that emits `Score`.
- **Critic** — produces critique text bound to criteria. Advises; does not score.
- **Report** — terminal bundle of score + critique.

## Boundaries
Scorer and Critic read the subject. Neither writes it. Report does not feed back into Scorer in the same run.
