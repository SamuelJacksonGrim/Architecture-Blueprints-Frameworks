# System Flow — Autonomous Cognitive Loop

One cycle. The loop closes back onto its own state — that's what makes it a self.

```
   ┌───────────────────────────────────────────────────────────────┐
   ▼                                                                 │
 tick (internal clock ─ terminal sink)                              │
   │                                                                 │
 perceive input ─▶ working state                                    │
   │                                                                 │
 generator proposes action ─▶ self-monitor                          │
   │                                                                 │
 update metrics (observe-only, terminal sink)                       │
   │                                                                 │
 collect reports: trust · validation · abuse-resistance · prefs     │
   │                                                                 │
 ▶▶ GOVERNOR.decide(reports)  ── the one decision point ──          │
   │ allow                                                           │
 commit to state ─▶ consolidate? ─▶ preference eval ─▶ age state ───┘
   │
 route next behavior
```
