# Authorship Record

**Work:** Architecture-Blueprints-Frameworks
**Human author and sole copyright holder:** Samuel Jackson Grim
**Last updated:** 2026-09-27

This record documents the human creative control exercised over this work. It
exists because U.S. copyright protects human-authored expression, and a
documented account of the author's contribution supports registration and
enforcement. (Under *Thaler v. Perlmutter*, an AI is not an author and holds no
rights. The human who directs, selects, arranges, and edits is the author.)

## How this work is created

The work has been built since 2026-06-15 through an **iterative, multi-model
chain directed and arbitrated by the human author**. The git history of this
repository is the dated evidence.

1. The author sets the goal, the principles (intent → autonomous construction →
   inspection → human decision), and the requirements.
2. One AI tool drafts under the author's instructions.
3. The author takes that output to a *different* AI tool with specific
   instructions on what to change and why, and often back again.
4. At every step the author **selects** what to keep, **rejects** what to
   discard, **edits** the expression, and **integrates** the pieces.

AI tools used as instruments have included **Claude** (Anthropic), **GPT**
(OpenAI), **Grok** (xAI), and **Gemini** (Google). None is an author. Each was operated under the
author's direction. `COLLABORATION.md` and `OPERATOR.md` describe this method
as the author practices it.

## Controlled test iterations (2026-09-26 to 27)

The author also refined the work through controlled experiments whose results
fed back into the text, with the author choosing what to change:

- A first one-shot build from the framework (`resonance-journal`). The author
  graded it, named what it missed, and decided which findings were framework
  defects. That led to DecisionLog D-013 to D-022 (PRs #11 and #12).
- A rubric locked *before* the changes, in its own commit (`d2dc69d`), then
  moved out of the system under test when a re-run found it. The author
  decided that answer keys may not live in the framework (D-023, PR #13).
- The author rejected a per-genre rubric proposal as contrary to the work's
  general-purpose design, and overruled an AI's defect finding on a blind
  run ("it was a one-shot prompt"). The second is recorded in the evaluation
  history in `resonance-journal`. Both are in the session that produced
  PRs #11 to #13.

These are selection, rejection, and direction by the human, applied to the
expression of the work. They are recorded in commits, PRs, and the DecisionLog.

## The human authorial contributions

- **Conception and design:** the construction order, the ten-artifact
  language, depth selection, the intake and escalation rules, the authority
  model, and the templates.
- **Selection:** which drafts from which models to keep, across models and
  across iterations.
- **Arrangement and coordination:** combining outputs from different models
  into one coherent framework (compilation-type authorship, 17 U.S.C. § 103).
- **Modification and editing:** directed revisions across successive passes.
- **Experimental direction:** designing the tests, judging their results, and
  deciding what the work should become because of them.

## Reach into works built with it

Projects built with this framework instantiate its templates. Their design
documents carry this work's structure, headings, frontmatter, and wording, and
apply its rules. Those parts are derivative of this work. Across independent
builds with different prompts, the framework, not the model, determined the
structure, sequence, and organization of each project's design record. The
records in those projects (`legal/AUTHORSHIP.md`) set out this argument and its
limits.

## Keeping this accurate

This record must stay truthful. Add a tool to the list when one contributes,
and keep the evidence: commit history, prompts, and decision logs.

---

## Related

[[LEGAL-BASIS]] · [[COLLABORATION]] · [[OPERATOR]] · [[licensing-faq]]
