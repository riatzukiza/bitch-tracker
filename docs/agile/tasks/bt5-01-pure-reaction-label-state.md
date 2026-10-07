---
uuid: acfa4cdf-a7b4-43d2-a165-eeffff40ce3d
title: BT5.01 Pure reaction-label state and author-count laws
status: incoming
priority: P2
points: 3
labels: planning, pure-laws, reactions, issue-5
---

# Context

[Issue5](https://github.com/octave-commons/bitch-tracker/issues/5) partitions
pure reaction/dedup/watchlist extraction from artifact hygiene
[issue4](https://github.com/octave-commons/bitch-tracker/issues/4) and effectful
adapters [issue6](https://github.com/octave-commons/bitch-tracker/issues/6).
Accepted main `4f1015bae457e6b4890f80a5d312f4259fce3ddb` contains a lifecycle
scaffold, not the old reaction implementation. Closed, unmerged PR1 source
`693f1388e61bd268814f85d1a40ef15a4485e6a3` and PR2 source
`c48c8e45366e592b30cdbbcf54f016d585b0e646` are reference evidence only. Their
source-only done cards and test claims do not transfer readiness or approval.

This is one standalone 3-point story within issue5. Sibling issues are external
scope references, not foreign UUID dependencies. No accepted sibling card is
present on current main. Points cover one finite state law and fixture/property
coverage. Supplied-time dedup and watchlist thresholds need separate planning.

# Outcome

Specify and, after planning admission, implement a portable pure transition
that maintains qualifying reaction labels per message and derives each author's
active-message count. Multiple reactors or emoji labels on one message keep the
author counted once for that message until its last qualifying label is removed.

# Scope

The proposed boundary and test matrix are detailed in
[reaction-label-law-plan.md](../notes/reaction-label-law-plan.md).

- Plain Clojure maps/sets, explicit state and fixed qualifying-emoji policy.
  Stable server, channel, message, author, reactor and emoji IDs are supplied
  by adapters; no Discord object enters the pure domain.
- Add/remove one reactor-and-emoji membership. Each message contributes zero
  or one to its author's count; distinct active messages contribute separately.
- Preserve message-author binding. Reject malformed state/policy, invalid
  operations, missing/blank IDs and conflicting authors with typed error data.
  Invalid transitions return the original state unchanged.
- Derive counts from labels or maintain them under an explicit equivalence law.
  Choose the representation during admitted implementation without effects.
- Prefer portable `.cljc` when host compatibility is practical; keep domain
  decision separate from shape/law validation and document the host boundary.

# Non-goals

No Discord/BdApi/Socket/HTTP/filesystem integration, runtime activation, message
content, credentials, historical runtime snapshot, generated bundle, sanitation,
global mutable state, clock, TTL/durable/event-ID dedup, watchlist thresholds,
notifications, mentions or common-kernel promotion. No old implementation,
source-only AGENTS file or done card is transplanted. This planning PR changes
no runtime source or established board state.

# Acceptance criteria

1. Two reactor/emoji memberships on one message contribute one active message.
   Removing either keeps the count; removing the last decrements once, never
   below zero.
2. Two messages by one author contribute two. Distinct authors, channels and
   servers remain isolated even if message ID strings coincide.
3. Repeating an add while its membership exists or a remove while it is absent
   is idempotent. Unknown-message removal is a validated no-op; unqualified
   emoji events are no-ops under fixed policy after identity validation.
4. Bad IDs, operations, state/policy or conflicting message-author binding
   produce typed errors and preserve state without partial count changes.
5. Document ordering: disjoint memberships commute; opposite operations on the
   same membership follow supplied order. An old add after removal is a new
   transition; historical-event dedup is outside this slice.
6. Fictional fixtures and generated operation sequences prove the count/label
   invariant, nonnegative counts and isolation, without private bodies or live
   network dependencies.
7. Preserve the lifecycle/export contract through existing tests and the
   hermetic export smoke; add no duplicate exporter or board/state engine.
   Required deterministic implementation checks bind its exact commit and
   report missing tools or failures truthfully.

# Verification

This PR verifies authored planning: full diff hygiene, immutable base/source
ancestry, Receipt River schema/prefix preservation and actual Rheos readback of
this incoming UUID. Readback does not demonstrate readiness.

Before implementation, settle native planning findings and use Rheos for lawful
ready admission. Then write red tests/laws before green domain code. Record
commands, exact SHA, assertion counts and coverage: zero-warning clj-kondo,
hosted CLJS compile/test, deterministic fixtures/properties and, if `.cljc` is
used, the same JVM/CLJS fixtures. Reuse `pnpm test`, `pnpm build` and
`scripts/verify-bd-export.mjs` where applicable. Never connect to live Discord
or label implementation checks passing in a planning-only PR.

# Risks

- Emoji normalization belongs to adapters. Qualification is fixed for a state
  instance; policy migration requires its own reviewed contract.
- ID collisions and inconsistent author identity can corrupt counts; use the
  composite message key and explicit conflict failures.
- Set membership models delivery order, not historical event replay. Conflating
  these silently introduces unsupported dedup semantics.
- Historical source and source-only done cards are unadmitted references.
  Planning review and Rheos ready remain unmet regardless of old test counts.


# Proposed whole-issue coordination refinement

This existing reaction story retains its complete seven acceptance criteria,
Incoming/P2/3 metadata, original scope/non-goals and history. Its three points
size the finite reaction law, not the entire issue 5.

The [whole issue 5 design](../notes/issue5-full-pure-laws-plan.md) and proposed
[epic](bt5-full-pure-laws-epic.md) retain all eight original concept bullets grouped into seven design categories, eight
invariants and seven proofs, including reactions, supplied-time dedup, watchlist
thresholds, policies, pure shape coercion and all event/config/socket schemas.
Proposed epic UUID `57b9ffc5-75e7-4098-9af8-efc001f60eb0` totals 13 points: existing reaction 3,
supplied-time dedup 5 (`e164efce-36e6-4cbe-9407-ddcb3d7d7509`), and watchlist/policy/shape
integration 5 (`36b20257-9d07-45a7-9246-867706f810cc`). All estimates/decomposition require
review. This body reference does not retroactively assign an operational parent
or dependency to this established card. No existing status/frontmatter changes.

Review the shared normalized reaction event/config/socket contract before
implementation; the larger design preserves the existing author/count/membership
laws and adds independent pure sibling outcomes. Old set idempotence is not
TTL replay protection. Existing no-clock/no-watchlist non-goals apply to this
reaction story; sibling integration is coordinated by the new proposed epic.
The old CodeRabbit completion at `64af437938b15b0e0bd37c80cc01610a1dc25992`
does not approve the broadened planning head. Sync-free accepted base
`4f1015bae457e6b4890f80a5d312f4259fce3ddb` is identical on current owning
and personal main; this proposal stacks on personal PR 1 and inherits its
qualification hold. No implementation or Rheos Ready is claimed.
