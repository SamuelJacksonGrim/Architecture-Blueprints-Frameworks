# OPERATOR — optional advice if you have more than one model

> This file is **not** part of the build contract.
> `AGENTS.md`, `SELECTOR.md`, and `PIPELINE.md` are the contract.
> A single capable model can finish a build without reading this.
>
> What follows is how a human *routes work across minds* when they have
> more than one. Model strengths change. The **seams** do not.

---

## The seams (these are the ontology, wearing work-order clothes)

| Seam | What gets decided | Lives in |
|---|---|---|
| **Intent** | what, why, must-not, done-when | `INTENT.md` |
| **Shape** | pieces, folders, boundaries | Architecture, Modules, ProjectStructure |
| **Invariants** | what must always be true; secrets; threat edges | Contracts, QUALITY-BAR |
| **Wiring** | code that runs | `src/`, smoke test |

Use different conversations at different seams if you want. Do not make five
vendors mandatory. If you only have one model, you still walk Intent → Shape →
Invariants → Wiring.

---

## A pattern that works *today* (September 2026)

Treat this as a field note, not a law.

1. **Talk the goal to death first.** One long conversation about how the thing
   should work, what would make it a failure, what must never happen. Do not
   open a repo yet. (People often do this with a model that is patient in
   dialogue.)
2. **Lock shape next.** Folders, modules, boundaries. One model that is good at
   structure. Output is a tree and a short Architecture note — not code.
3. **Lock invariants next.** Classes of data, contracts, secret handling,
   “who is allowed to touch what.” A suspicious model earns its keep here.
4. **Wire last.** Write code against the notes, not against a vibe.
5. **When a model says “that cannot be,” treat it as a claim.** Hand the same
   claim to a different model. Keep the hole, not the confidence.

As of this writing, a common split people actually use:

- long intent talk → a conversational model
- repo tree / module map → a structure-strong model
- security, secrets, incident surfaces → Copilot or an equivalent auditor
- careful wiring and locking → Claude
- finding the deadlock Claude just declared → Grok or GPT
- aggressive “make the smoke test pass” → Grok

That roster will rot. The seams will not.

---

## Rules so this does not become a committee religion

- Never require a model the human does not have.
- Never re-derive Architecture in every chat. Point at the files.
- Never let two chats own the same invariant. One `Contracts.md`.
- If the human is the sharp one in the room, they may skip this file entirely
  and just *say* the checklist. That is not a lesser path.
