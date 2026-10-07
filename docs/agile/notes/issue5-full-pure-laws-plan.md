# Proposed full issue 5 pure-law contract

Planning only. [Issue 5](https://github.com/octave-commons/bitch-tracker/issues/5)
retains eight original concept bullets grouped into seven design categories, eight invariants and seven proof obligations. Proposed
epic `57b9ffc5-75e7-4098-9af8-efc001f60eb0` sums existing reaction (3 points) + dedup (5 points) + watchlist/policy/shape (5 points)
to 13. Existing reaction UUID `acfa4cdf-a7b4-43d2-a165-eeffff40ce3d` and all its original
seven criteria/non-goals/Incoming / P2 / 3 points remain unchanged. No new-head approval,
Ready, human acceptance, software implementation or whole-outcome size reduction.

## Current source, ownership and authority

Owning and personal main are exactly
`4f1015bae457e6b4890f80a5d312f4259fce3ddb`. Personal PR 1 at
`64af437938b15b0e0bd37c80cc01610a1dc25992` is the proposed stack parent:
its whole seven-file scope and original note/card were read after successful
canonical status. It expressly excludes timed dedup/watchlist followups. Its
current CodeRabbit completion and zero rounds do not qualify this broadened head.
Personal PR 2 handles issue 4 sanitation; issue 6 effect adapters remain separate.
Closed origin mega-PRs 1/2 and their test/done claims are evidence, not accepted
code or lawful readiness. No foreign branches or real payloads are adopted.

Accepted source is a BetterDiscord lifecycle scaffold with Date/timers at its
outer adapter. There is no current reaction/dedup/watchlist domain implementation.
README/package.json/shadow-cljs.edn govern pnpm/build/test/export. There is no
repository-root AGENTS/PROCESS/local SKILL file at accepted main; the applicable
user/global contract and current canonical pr-flow/planning pack apply. The
committed PRINCIPLE history remains evidence; it is not a live service/model
capability or permission to execute nested `.eta-mu` ownership.

## Complete concepts and architecture

1. Normalized added/removed reaction events: closed operations and validated
   event/source/subject identity.
2. Stable author/reactor/message/channel/server/emoji IDs, with composite message
   keys `[server channel message]` and retained author binding. Raw Discord/JS
   values normalize only at the issue 6 edge.
3. Multiple reactor/emoji memberships per message and count-at-most-once while
   at least one qualifying label exists. Existing finite reaction law remains.
4. Watchlist membership and threshold transitions over trusted explicit
   policy/count/previous-membership data.
5. Bounded event dedup state using explicit supplied ingestion time, TTL and
   capacity; no Date/timer/sleep/global.
6. Pure policy decisions, with proposed threshold/comparison/migration rules
   reviewed rather than invented in implementation.
7. Domain-agnostic pure shape coercion/protocol values plus event/config/socket
   schemas, reviewed Malli or repository-standard law choice, producer/consumer
   validation. No new event kernel, board engine or common-law promotion.

Pure contracts, identity validation, normalization/coercion, state decisions and
TTL/threshold algorithms prefer `.cljc` when practical. Host adapters may consume
these laws; pure code cannot depend on Discord.js, Socket.IO, filesystem/network,
mutable globals, JS native payloads or clock. Runtime sampling supplies time;
provider output remains untrusted. Error outputs are typed data with original
state, not incidental JS exceptions. Portable library/dependency/tool choice and
new namespace layout require review; no generic utils dumping ground.

## Shared interface and deliberate decisions

The pure pipeline takes explicit validated state/policy/normalized event/time
and returns updated state/domain-event data or typed unchanged-state rejection.
Validate the entire relevant boundary before mutation. Qualifying emoji policy
is fixed for a reaction-state instance as already proposed; review any migration
as a versioned operation, never silently reinterpret stored labels. Event identity
includes trusted source scope and full canonical payload equality. A repeated
ID/payload within retention is a duplicate; contradictory ID reuse is a typed
conflict. Changing irrelevant host object identity cannot manufacture a new event.
Do not conflate set idempotence with durable replay or exactly-once transport.

Propose half-open retention `[first-seen, first-seen+TTL)` with explicit bounded
portable integer units/range, but review the exact ABI first. TTL zero/negative,
overflow, time regression, far-future input and source timestamp versus supplied
ingestion time all have explicit fixtures and approved semantics. Capacity is
explicit; pressure cannot silently evict a retained receipt and admit replay.
Review deterministic rejection/expiry rules, monotonic-time requirements and
late-event treatment. No hidden pruning of author bindings changes reaction
identity; identity-retention lifecycle remains an explicit future runtime decision.

Disjoint memberships commute; opposing same-membership add/remove follows
supplied order, preserving the original reaction contract. Retained-window dedup
filters repeated deliveries; it cannot promise unbounded historical replay
protection. Threshold relation/range, initial membership and crossing direction
are proposed review choices. Once per state transition means unchanged membership
emits nothing; final-label removal may cross down exactly once. Pure emission
returns data only. Unsupported or ambiguous ordering/configuration is typed
refusal rather than accidental last-write authority.

Domain-agnostic coercion handles declared Clojure-shaped protocol values, not
Discord-specific raw payload access. Preserve IDs without lowercasing/truncation/
fuzzy equality; document Unicode/custom emoji identity at the adapter contract.
Schemas name operation/version/required and optional fields/extra-field policy
and typed errors for event/config/socket envelopes. Add shared contracts once,
validate both producer and consumer; no repeated divergent schemas per adapter.
A schema library absent from accepted dependencies is a review/install decision,
not a claim that a validator already ran or a license for a board parser.

## Complete original invariant crosswalk

1. At most one author contribution per actively qualifying labeled message.
2. Removing one membership leaves count unchanged if another qualifies.
3. Removing the final membership decrements exactly once.
4. Duplicate add/remove is idempotent in the documented model.
5. Supported reordered inputs have documented deterministic outcomes.
6. Dedup expiry uses only supplied time; tests never read wall clock.
7. Threshold crossings/watchlist transitions emit once per state transition.
8. Unknown/malformed IDs/envelopes reject as typed data, not JS exceptions.

The existing reaction story's seven literal criteria remain additional controls.
Each child contributes to the complete issue; none may independently close it.
New child dependency links reference existing reaction UUID and proposed dedup
UUID only; no foreign issue/title is fabricated as a UUID dependency. The existing
reaction card receives body coordination only, no retroactive metadata parent.

## Meaningful red/green and all seven proof obligations

After actual planning qualification and lawful Rheos Ready, author failing laws
first, then pure domain functions, then reviewed edge consumers. This proposal
adds no code/test mirror. Required original proofs are:

1. Table-driven add/remove parity, multi-reactor/emoji, TTL boundaries, malformed
   event, threshold and watchlist transition tests.
2. Properties for idempotence and count-at-most-once while labeled.
3. Inject time/identity without sleeps or network.
4. Zero clj-kondo errors and warnings over changed source/tests.
5. Hosted CLJS compile and actual test execution.
6. For CLJC, the same law fixtures execute on JVM and CLJS.
7. Attach immutable SHA, actual command lines, assertion counts and coverage.

Negative controls include duplicate IDs with conflicting full payload, expired
versus retained receipts at exact boundary, time regression/range/overflow,
capacity pressure, unknown/blank IDs, malformed state/envelopes, nonqualifying
emoji after validation, retained-author conflict after last removal, two contexts
with coincident IDs, no-op/increased/decreased thresholds and policy mismatch.
Generated sequences compare state with an independent membership/count model
and expected watchlist transitions at every step, not copied implementation.
Run the real pure pipeline so rejected/duplicate delivery cannot partially mutate
reaction state or emit watchlist data. Valid-shaped malicious/extra-field
envelopes and producer/consumer disagreement must fail. A deliberately failing
async/subprocess fixture must yield nonzero official-runner status.

Current commands are `pnpm run lint`, `pnpm test`, `pnpm build` and export
verification `node scripts/verify-bd-export.mjs`. `pnpm test` already chains lint,
Shadow test compile/autorun and full build/export; retain meaningful lifecycle and
CommonJS meta-factory smoke. Shadow `:source-paths [src test]`/`-test$` controls
discovery; prove new CLJS tests actually run/count and deliberate failure is
nonzero. Current repo has no JVM test alias or coverage command: review an
isolated actual JVM fixture runner and coverage tool/output selection before
claiming parity/coverage, not unsupported assumed `clojure -M:test`.
Any fixture additions/tooling workflow changes are later implementation scope,
not silently installed here. Zero-warning/full gates and missing tools remain
visible; changed-only lint does not waive existing required full package checks.

Hosted CI currently contains only the pinned eta-mu review caller, not a new
independent pure-law test pipeline. Future hosted CLJS execution and coverage
proof must be implemented/reviewed without secrets or provider contacts. Current
caller reacts to opened/synchronize/reopened/ready_for_review, gated !draft and
same repository, pin `2b918cdab2ebd30e745bb8fa86d077d7a3af0030`. No create,
retarget/edited, eager-merge or deployment caller exists in the accepted tree.
That event inventory is source evidence, not protection or trusted-gate activation.

## Review, sizing and remaining holds

Whole issue is intentionally larger than the existing reaction (3 points). Proposed epic (13 points)
aggregates reaction (3 points) + dedup (5 points) + watchlist/policy/coercion/schemas (5 points), all individually
bounded at five or less. Review scope, library choice, thresholds/retention ABI,
error/ordering/coercion contracts, integration and point fairness; further lawful
breakdown must retain every original concept/invariant/proof. No estimate/status
change to the established reaction story and no source-only done/accepted claim.

Parent PR 1 and new planning/design/current-head checks/Rheos Ready remain holds.
Current CodeRabbit eligible completion is bound to the old finite plan; current
0 rounds and no new whole-plan review remain distinct. Actual native parsing
under a default-path/explicit owned fixture is visibility, not an accepted repo
configuration/WIP/admission. Eta Mu issue 239 distribution, Foresight issue 134 publisher visibility
and current quotas are existing owner concerns only; no new failure is inferred
without an actual job. No remote publish, approval settlement, request, real
Discord/Socket/OpenPlanner/backend/provider, message, credentials, settings or
shared-service action is performed or authorized by this local proposal.
