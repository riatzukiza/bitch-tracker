---
uuid: 36b20257-9d07-45a7-9246-867706f810cc
title: BT5.03 Watchlist policies and pure shape integration
status: incoming
priority: P2
points: 5
labels: planning, pure-laws, issue-5
parent: 57b9ffc5-75e7-4098-9af8-efc001f60eb0
dependency: [acfa4cdf-a7b4-43d2-a165-eeffff40ce3d, e164efce-36e6-4cbe-9407-ddcb3d7d7509]
---

# Context

Epic `57b9ffc5-75e7-4098-9af8-efc001f60eb0` retains the complete issue 5 outcome;
[the design](../notes/issue5-full-pure-laws-plan.md) coordinates reaction (3 points),
dedup (5 points) and this proposed watchlist/policy/shape (5 points) component.

# Outcome and scope

Plain Clojure data and validated explicit policy/count/previous-membership
facts decide watchlist membership and once-per-transition domain event data.
Pure domain-agnostic coercion/protocol values and event/config/socket schemas
validate replaceable boundaries without introducing a second authority.

# Acceptance criteria

1. Review threshold comparison, range, initial membership and enter/leave rules;
   exact-boundary, increase/decrease, duplicate/no-op and absent-author fixtures
   produce deterministic transitions and no repeated emission while unchanged.
2. Policy is explicit validated data. Unknown/malformed configuration/count/
   membership returns typed rejection and original state unchanged. No hidden
   environment, Discord object, mutable global or clock is consulted.
3. Multiple qualifying labels retain message-at-most-once counts and author
   binding through threshold decisions, including final removal and replay expiry.
4. Define portable pure coercion/protocol value contracts independent of domain
   mutation; no lossy identity normalization or generic utility dumping ground.
5. Reviewed Malli or repository-standard law schemas cover normalized event,
   configuration and socket envelope values, exact vocabulary/version/extra-field
   policies, null/missing/unknown IDs and domain-agnostic roundtrip/refusal tests.
6. Actual pure pipeline integration retains original seven reaction criteria and
   all eight parent invariants. Duplicate/rejected delivery produces no notification
   or threshold event; effect adapters consume data only after validation.
7. Full table/property, JVM/CLJS parity and hosted compile/run/lint/coverage
   obligations remain, with protocol producer/consumer negative controls.

# Verification

Use fictional IDs/policies/injected time, no sleeps/network/real messages.
Meaningful count/membership/threshold generated sequences plus independent
coercion/schema fixtures and actual pipeline tests precede green. Full existing
package/lifecycle/export checks must pass; missing tools/baseline failures are
visible. No runtime adapter or live transport is implemented here.

# Non-goals and risks

No Discord moderation, watchlist persistence, notifications, mentions, Socket.IO
or OpenPlanner transport, live credentials or schema/kernel promotion. Review
policy migration, contract library/placement, legacy compatibility and whole
five-point sizing before admission; no narrower threshold-only substitute.
