# KAIZEN — more rounds after the handover

Only when the human asks for more rounds. Each round is a small pass with the
same authority rule: you build, the human inspects.

## What qualifies

An item enters a round only if it is one of these. Each is yes or no, not a
matter of taste:

1. **Broken promise.** The system breaks its own Contracts, invariants, or
   Intent "done when".
2. **Missing include.** The Intent Card marked an implied counterpart
   `include`, and it is not built.
3. **Unproven claim.** A doc states something no test or smoke run shows.

Anything else is new intent (a new feature, taste, a different stack). List it
for the human. Do not build it.

## One round

1. Audit the result against 1–3. Write the list.
2. Pick the item with the worst consequence if left (data loss > wrong result >
   missing convenience).
3. State its cost: what grows (rows, bytes, CPU, dependencies) and the bound.
   Anything that grows without limit gets a bound or a retention rule first.
4. Fix it. Prove it with a test. Update the docs in the same change.
5. Log it in DecisionLog only if it changed a consequential decision.

## Stop

Stop when an audit finds nothing that qualifies, or when everything left needs
the human (an escalation trigger, the live boundary, taste). Report what is
left and why. Also stop when the human says so.
