---
uuid: 57b9ffc5-75e7-4098-9af8-efc001f60eb0
title: BT5 Full pure reaction, dedup and watchlist laws
status: incoming
priority: P2
points: 13
labels: planning, pure-laws, issue-5
---

# Context

[Issue 5](https://github.com/octave-commons/bitch-tracker/issues/5) requests the
whole pure domain/event/policy/shape extraction, not a reaction-only or TTL-only
substitute. Existing personal PR 1 owns the reaction story `acfa4cdf-a7b4-43d2-a165-eeffff40ce3d`
at `64af437938b15b0e0bd37c80cc01610a1dc25992`; this proposed epic stacks on
that parent while preserving its original card/note prefixes and metadata.

# Outcome and scope

Review and then implement all eight original concept bullets, grouped into seven design categories, as plain Clojure data:
normalized add/remove events; stable message/author/reactor/channel/server/emoji
identity; multi-reactor/multi-emoji label state; watchlist membership/threshold
transitions; bounded dedup with supplied time/TTL; pure policy; domain-agnostic
coercion/protocol values and repository-standard event/config/socket law schemas.
The complete [design](../notes/issue5-full-pure-laws-plan.md) owns proposed
interface decisions and proof crosswalk. New states are initial Markdown input,
not operational admission. Whole 13-point estimate is the sum of proposed
reaction (3 points) + dedup (5 points) + watchlist/policy/shape (5 points); review sizing or lawful further
breakdown before implementation, preserving every original requirement.

# Children and relationships

- Existing reaction (3 points) UUID `acfa4cdf-a7b4-43d2-a165-eeffff40ce3d`, original seven criteria retained.
  It is a body-linked component, not a retroactively changed parent assignment.
- New dedup (5 points) UUID `e164efce-36e6-4cbe-9407-ddcb3d7d7509`.
- New watchlist/policy/shape (5 points) UUID `36b20257-9d07-45a7-9246-867706f810cc`.

# Acceptance criteria — complete original issue invariants

1. A target author's message contributes at most once while a qualifying label remains.
2. Removing one reactor/emoji cannot decrement while another qualifying label remains.
3. Removing the final qualifying label decrements exactly once.
4. Duplicate add/remove delivery is idempotent.
5. Supported event reordering has documented deterministic outcomes.
6. Stale dedup entries expire only by supplied time; tests never use wall clock.
7. Threshold crossings and watchlist transitions emit once per state transition.
8. Unknown/malformed identities or envelopes produce typed data, not JS exceptions.

All eight original concept bullets covered by the seven design categories above and all seven original proof obligations below are
additional whole-issue obligations; none is waived by a passing child fixture.

# Verification

Table-driven add/remove, multi-reactor/emoji, TTL boundary, malformed, threshold
and watchlist tests; properties for idempotence and count-at-most-once; injected
time/identity without sleeps/network; zero-warning/error lint of changed source
and tests; hosted CLJS compile+execution; identical JVM/CLJS fixtures when CLJC
is used; immutable SHA, commands, assertion counts and coverage output. Run full
existing lifecycle/export and package gates and the meaningful negative controls
in the design. Implementation requires qualified planning and Rheos Ready.

# Non-goals and risks

No Discord, Socket.IO, filesystem/network, OpenPlanner, provider, notification,
message body, credentials, generated snapshots or raw JS domain authority.
Issues 4 sanitation and 6 adapters are references, not invented foreign UUID
dependencies. Old closed unmerged mega-PRs are provenance, not accepted code.
Domain purity, duplicate-ID conflict, clock/order/pressure policy, thresholds,
coercion, schemas and sizing are explicit review decisions; implementation may
not invent them. No new board config/parser/validator/transition is created.
