# Tool Ecosystem — Router · Registry · Executor

Deterministic tool dispatch. The Registry names what exists. The Router
chooses. The Executor is the only place the world changes.

Use this when a system must call tools without letting the chooser also run
them. Pair with an agent-loop if you need a reasoner; this skeleton is the
*hands*, not the *mind*.

Golden rule: **Router never executes. Executor never chooses. Registry never
runs.**

See the ten artifacts in this folder. All `complete`.
