---
uuid: e164efce-36e6-4cbe-9407-ddcb3d7d7509
title: BT5.02 Supplied-time bounded event dedup laws
status: incoming
priority: P2
points: 5
labels: planning, pure-laws, issue-5
parent: 57b9ffc5-75e7-4098-9af8-efc001f60eb0
dependency: [acfa4cdf-a7b4-43d2-a165-eeffff40ce3d]
---

# Context

Issue 5's complete scope is retained by epic `57b9ffc5-75e7-4098-9af8-efc001f60eb0` and the
[full design](../notes/issue5-full-pure-laws-plan.md). This is the pure dedup
component, not the whole parent outcome; existing reaction (3 points) remains unchanged.

# Outcome and scope

Given explicit validated state, normalized event identity+payload, supplied time
and TTL/capacity policy, return data describing new delivery, repeat, expiry or
typed rejection. No clock/global/cache/filesystem/provider is read internally.
TTL storage is pure supplied state; runtime delivery/persistence stays issue 6.

# Acceptance criteria

1. Exact duplicate event identity and full payload within retained TTL produce
   no repeated reaction/watchlist domain output; contradictory reuse of an ID is
   a typed conflict, not silent suppression.
2. Review and encode TTL units, half-open boundary, valid numeric range and
   supplied-time ordering. Exact boundary/TTL zero/negative/overflow/regression
   fixtures have deliberate behavior; no wall-clock or sleep.
3. Bound retained entries with explicit capacity/expiry policy. Full capacity
   cannot silently discard a live receipt to admit a replay; invalid policy or
   rejected delivery leaves input state unchanged.
4. Expiration is driven solely by supplied time; source-event timestamps cannot
   impersonate trusted ingestion time. Late/stale input semantics and reordering
   are documented, not claimed commutative for opposing membership operations.
5. Distinct contexts, composite subject keys and event/source identities remain
   isolated; property tests cover repeat, expiry and duplicate-ID conflict.
6. Shared event/config/socket shapes reject unknown/malformed identity/fields
   with typed data before any partial update; domain-agnostic coercion is explicit.
7. Integrate pure dedup→reaction→watchlist decisions without effectful emissions:
   malformed/rejected/duplicate transitions cannot leak count or threshold events.

# Verification

Meaningful table/property and dual-host fixtures, full parent seven proofs,
compiled-host execution and zero-warning changed-source/test lint. Deliberately
broken clock/expiry/duplicate handling must fail official tests. Existing lifecycle
and export smoke remain. Red laws before green functions only after qualification.

# Non-goals and risks

No timer, wall clock, durable cache/store, transport delivery guarantee or
exactly-once claim beyond the reviewed retained-window model. Capacity/TTL/order
choices and five-point sizing are proposed; review before Ready/implementation.
