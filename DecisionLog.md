# DecisionLog — this repository

---

### D-001 — Construction order: Architecture → Flows → Contracts
### D-002 — Instantiation total; completeness tiered
### D-003 — OPERATOR is optional
### D-004 — Class ≠ depth; implicit-decision test
### D-005 — Interfaces → Modules → Dependencies as completeness edges
### D-006 — Authority is not authorship
### D-007 — Planned catalog is forged, not sketched
### D-008 — One agent brief, many loaders
### D-009 — Cognitive-cycle is a class, not a difficulty setting
### D-010 — Continuous does not mean exhaustive
### D-011 — Artifacts are not permission checkpoints

---

### D-012 — Authority is inspection of the pass

**Question:** Did removing the permission-queue also remove the construction order?

**Chosen:** Restore the order. It is how to build. Human authority is the right
to accept, reject, modify, or redirect *the finished pass*. It is not a signature
required between artifacts. Revising an earlier artifact mid-pass is construction.

**Intent → autonomous construction → inspection / evidence → human decision.**

**Rejected:** Asking "is this architecture okay?" before Flows. Treating D-011 as
"there is no order." Transferring final authority to the AI because it finished.

**Date:** 2026-09-26

---

### D-013 — Must Interfaces wait on Schemas at standard depth?

**Question:** `standard` requires Interfaces `complete` and leaves Schemas
optional. Every Interfaces file had `depends_on: [Schemas]`, which broke depth
self-consistency. Every standard-depth build hit it. No full-depth skeleton
showed it.

**Chosen:** Interfaces `depends_on: [Types, Contracts]` in templates, all
skeletons, and the example. The operations and guarantees an interface names
come from Types and Contracts. Schemas is the cross-system ontology, and
nothing plugs into it. Also, `SCHEMA.md`: an inherited edge to an artifact the
depth leaves optional does not gate completeness. So the next template that
makes the same mistake resolves itself, and it does not stall the build or
push depth up without anyone saying so.

**Rejected:** Requiring Schemas at standard (that is `full` under another
name). Leaving each builder to resolve it (the outcome then depends on which
entity builds, and a careless one misses the conflict). Changing construction
order (PIPELINE is unchanged: Schemas is still built before Interfaces when it
is built).

**Found by:** a standard-depth build (Resonance Journal, its D-007).

**Date:** 2026-09-26

---

### D-014 — What does the user expect but not say?

**Question:** The first standard-depth build did exactly the verbs it was given
(export without import, archive without delete, links without traversal) and
scored 0/6 on the category's norms (`evals/journal-rubric.md`).

**Chosen:** The Intent Card lists implied counterparts (each verb's opposite, the
category's norms), each marked include or exclude with a reason. It also gets a
Roles line. Default is include when small, reversible, and inside the current
escalation level.

**Rejected:** Genre checklists (they grow without end and bias toward known
genres). Building every counterpart (it crosses escalation triggers silently).

**Date:** 2026-09-26

### D-015 — When may the builder ask?

**Question:** "Three questions max" said how many, not when. Whether a prompt
is ambiguous is a matter of opinion.

**Chosen:** Ask only when a consequential Intent field (roles, exposure, money,
private data/secrets, irreversible actions, done-when) would be a guess. Taste
is never a reason to ask. An explicit one-shot means no questions: guess, log,
list the guesses first at handover.

**Rejected:** A mandatory pre-plan (it slows the prompts that are already
clear). Asking whenever something is unclear (that depends on the builder).

**Date:** 2026-09-26

### D-016 — Security: a menu for the human or a floor for the builder?

**Chosen:** A floor, by exposure profile (`SECURITY.md`), loaded only when the
profile or data needs it. Controls go into Contracts as guarantees. Skipped
controls are logged.

**Rejected:** Asking the human to pick algorithms. One flat list for every
system (overkill for local tools, and it gets ignored).

**Date:** 2026-09-26

### D-017 — Where does the pass end, and what if it's too big?

**Chosen:** The live boundary: nothing deploys, publishes, charges, or messages
anyone during the pass. The builder hands over the command. A pass too big to
verify whole is designed whole and implemented in end-to-end slices.

**Rejected:** Leaving "hand over, stop" to imply it (autonomy to build was being
read as autonomy to ship). Building everything shallowly.

**Date:** 2026-09-26

### D-018 — What may a follow-up round build?

**Chosen:** `KAIZEN.md`. A round fixes only broken promises, missing includes,
and unproven claims. Each fix states its growth and bound. The loop stops when
nothing qualifies. Everything else is new intent for the human.
QUALITY-BAR §10: nothing grows without a stated bound.

**Rejected:** Open-ended improvement (it drifts into taste). "Keep every
version" as the fix for lost edits (unbounded storage).

**Date:** 2026-09-26

### D-019 — Who checks the rules?

**Chosen:** `tools/validate.py`. Standard-library Python, the same command on
every OS and in every tool. It checks the framework (edges at every depth, links
on the AI path, loaders) and any project built from it (structure, depth
completeness, Intent Card fields). CI may wrap it, but it never requires CI.

**Rejected:** Checking by hand (it missed D-013 across nine files). GitHub-only
CI (the repo is cloned and used locally, from any tool).

**Date:** 2026-09-26

### D-020 — One front door per reader?

**Chosen:** `README.md` is for humans only: what happens, what to expect, and no
mechanics. `AGENTS.md` is the only AI entry point. QUICKSTART was merged into
README. GENERATOR was folded into AGENTS (it restated the same steps). The AI
path is AGENTS → SELECTOR → PIPELINE → skeleton, plus SECURITY or KAIZEN only
when triggered.

**Rejected:** Adding a file per concept (each file is another hop, and another
place for rules to disagree).

**Date:** 2026-09-26

### D-021 — What exactly trips a trigger, and where does it lead?

**Question:** Three cold readers (a journal, a photo store, a one-shot team
tracker) each went back and forth on the same things:
- "Escalate" had no target depth.
- "Private data" caught every personal app, including the operator's own notes.
- "Irreversible" made create↔delete exclude itself.
- One-shot vs. ask had no precedence.
- The load list disagreed with AGENTS and PIPELINE.
- Ordinary web apps got pushed toward the AI-pattern skeletons.

**Chosen:**
- Triggers map to depths: none → thin, any → standard; full when a network
  boundary comes with money, secrets, or private data, or when the design is
  reused as a skeleton. The governing test may only raise it.
- *Private data* means other people's data, or the operator's data leaving their
  machine. *Irreversible* means the system acting outside its own store. A
  guarded delete of your own records is an ordinary feature.
- One-shot overrides asking. *Implied* means any competent reader fills it the
  same way.
- The reading order separates "read now" from "consult at that step".
- Class is one token, and ordinary apps use `templates/`.
- SECURITY splits exposure rows from feature rows (accounts, uploads, protected
  downloads, money, encryption). Sandboxes only if handed.
- Artifacts may be `complete` while later slices are unbuilt.

**Rejected:** Counting triggers (a score). Asking the human to classify their
own data.

**Date:** 2026-09-26

### D-022 — Where is the project built, and is the stack taste?

**Question:** The second round of cold readers converged. A journal reader now
lands on thin, asks nothing, and includes guarded delete, bounded revisions,
multi-hop links, import, and date filters. Four frictions remained.

**Chosen:**
- Build in the human's project, never inside this repo. Never overwrite work
  you did not make in the pass.
- The stack is never asked about, but it is always logged (it decides
  exposure).
- Private data is tested by whose subject the record is.
- The module-separation trigger applies only when a Contract depends on the
  separation.
- A single-user localhost UI behind a per-launch token takes SECURITY's
  networked row, but it is not a network boundary for depth.
- The uploads row protects what is shown to others, not an owner's original
  that is itself the product.

**Date:** 2026-09-26

### D-023 — Where do answer keys live?

**Question:** A re-run of the journal prompt found `evals/journal-rubric.md`
while reading the repo and said so. A per-app rubric inside the framework is an
answer key inside the system under test. And once the framework has been tuned
on a prompt, that prompt can never be a blind test again, because its own
history describes the expected result.

**Chosen:** No eval files in this repo. PIPELINE's Done list is the one
checklist for judging any build, checked against the build's own Intent Card.
It is safe to read because it *is* the instructions. Blind tests use prompts
this repo has never been tuned on. Scores and per-app history live outside the
framework, with the project they graded.

**Rejected:** Hiding the rubric off the reading path (a thorough builder reads
the whole repo). A rubric per app or genre (the template list grows, and each
one leaks).

**Date:** 2026-09-26
