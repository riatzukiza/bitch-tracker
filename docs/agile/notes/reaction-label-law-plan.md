# Proposed reaction-label law and test contract

Story UUID: `acfa4cdf-a7b4-43d2-a165-eeffff40ce3d`; points: 3; tier: **proposed**.
This is a contract proposal for issue5, not implementation or an accepted shape
lift. The card remains incoming until reviewed and admitted through Rheos.

The boundary accepts plain Clojure data: explicit state, fixed qualifying-emoji
policy and one normalized event. It returns either a successful transition or
typed error data carrying the original state. Precise namespace/function names
and validation library are chosen during admitted implementation; this PR adds
no runtime adapter or validation engine.

| Value | Proposed constraint |
| --- | --- |
| Operation | Finite add/remove vocabulary |
| Message key | `[server-id channel-id message-id]`, nonblank strings |
| Author binding | One nonblank author ID per retained message identity |
| Membership | `[reactor-id emoji-id]`, nonblank stable strings |
| Policy | Explicit nonempty set of nonblank qualifying emoji IDs, fixed for a state instance |
| State | Pure Clojure maps/sets; retain author binding after labels become empty |
| Count | Per author, number of message keys with at least one qualifying membership; absent count means zero |
| Rejection | Typed malformed-input/conflicting-identity/state-policy error; original state unchanged |

Retained author binding makes later conflicting author IDs fail consistently
after the last label is removed. Forgetting identities is a separate retention
contract excluded here. This finite law does not promise unbounded runtime
retention; runtime owners need reviewed lifecycle policy before activation.
Malformed external state is untrusted and must be validated before use.

An unqualified emoji event is a no-op only after shape and existing author
binding validation. Unknown-message removal creates no retained binding.
Disjoint memberships commute; opposing add/remove for the same membership obey
input order. Set idempotence supplies neither exactly-once delivery nor
historical-event replay protection.

| Fictional fixture | Expected law |
| --- | --- |
| Same reactor, two emoji IDs | One count; surviving label keeps it counted |
| Two reactors, same emoji | Remove one without decrement; last decrements once |
| Duplicate add/remove and absent remove | Idempotence, nonnegative counts |
| One author, two messages | Two active-message contributions |
| Same message ID, other channel/server | Independent composite keys |
| Two authors | No count leakage |
| Bad IDs or invalid operation | Typed rejection and unchanged state |
| Author conflict, also after last removal | Typed rejection and retained binding |
| Nonqualifying emoji | Validated no-op |
| Generated operation sequences | Count equals membership projection at every step |
| Disjoint operation permutations | Equivalent final state/count; no claim for opposing same-membership order |

After review/readiness, write meaningful red fixtures/properties before green
code, using injected data only. Run hosted CLJS and, for `.cljc`, the same
JVM/CLJS fixtures. Preserve lifecycle tests and existing export smoke. Clocks,
dedup, watchlist and effectful consumers remain separately admitted stories;
no global helper, dependency hook or service runs in this planning PR.


## Proposed whole-issue design relationship

The original finite reaction contract and fixtures remain unchanged above.
[Issue 5 full pure-law planning](issue5-full-pure-laws-plan.md) now describes
the complete proposed issue decomposition and interface/validation integration.
Its dedup/watchlist effects-free siblings do not authorize clocks, TTL storage,
watchlist side effects or notifications inside this reaction function. No prior
review is transferred to the new full planning head; all shared schema and
integration decisions still require review and lawful Ready admission.
