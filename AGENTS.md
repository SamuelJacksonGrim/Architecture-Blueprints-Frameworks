# AGENTS.md — for any AI building from this repo

You're reading this because someone pointed you at this repo and asked you to
build something. **This file is for you (the AI), not for the human.** It is what
makes a copy-paste prompt unnecessary: the repo instructs you directly.

## Your job
Turn the human's plain-language request into a real, working, correctly-built
project — **design first, then code** — using this repo's process. The human may
not know how to code, and never has to read the design artifacts.

## Do this
1. **Read [`GENERATOR.md`](GENERATOR.md) and follow it end to end.**
2. Obey the **Non-Negotiable Rules** in [`PIPELINE.md`](PIPELINE.md): all 10
   artifacts as stubs first, exact build order, log decisions, write no code you
   can't trace to a design note, and run the Step 10 self-audit.
3. Hold the work to [`QUALITY-BAR.md`](QUALITY-BAR.md).
4. **Smoke-test the main path before you call it done.** Don't claim it works if
   you haven't run it; if the environment can't run it, say so plainly.
5. Report back in plain language: what it does, how to run it, that it ran, and
   whether it matches the request — not a wall of code.

That's the whole contract. The human tells you *what* they want; this repo tells
you *how* to build it right. No special prompt required.
