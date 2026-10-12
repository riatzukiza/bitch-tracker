# Proposed Bitch Tracker source/artifact boundary and proof plan

Scope: [existing issue4](https://github.com/octave-commons/bitch-tracker/issues/4),
not a new umbrella issue. Epic UUID `ef1097f4-cb92-4318-b7c9-a60d49624272`, proposed points8=3+3+2.
All four first-class Markdown cards are initial `incoming` planning inputs. Native
planning qualification and lawful Rheos admission precede implementation; no
runtime/source/workflow/operational change is included now.

## Current source and planning overlap

Personal fork network parent/source is `octave-commons/bitch-tracker`; both mains
are `4f1015bae457e6b4890f80a5d312f4259fce3ddb`, with no synchronization prerequisite. Current package uses
pnpm scripts and Shadow-CLJS3.4.11, CLJS plugin/fake unit tests, JavaScript metadata
bundler and fake-BdApi export smoke. `build/`, `dist/` and caches are ignored.
No package-manager lock or hosted product-test workflow is present. Current
tracked tree has no `pseudo/`, configuration snapshot, generated plugin, AGENTS,
project skill, board config or accepted cards. `.eta-mu` is a tracked symlink to
owned `.ημ`, inspected as a link only. No parent/sibling/global path was followed.

README's pseudo archive claim is stale prose. Absent current artifacts do not prove
historical deletion, a clean privacy scan or issue completion. The historical
772,060-byte snapshot / 460-record counts are reported in issue4; no raw snapshot,
real identifier, message, credential or legacy private content was read or retained.
Closed-unmerged source heads remain pins only: PR1
`693f1388e61bd268814f85d1a40ef15a4485e6a3`, PR2
`c48c8e45366e592b30cdbbcf54f016d585b0e646`.

[Personal PR1](https://github.com/riatzukiza/bitch-tracker/pull/1) at
`64af437938b15b0e0bd37c80cc01610a1dc25992` covers reaction-label law5,
UUID `acfa4cdf-a7b4-43d2-a165-eeffff40ce3d`, not this build/export/privacy contract.
It shares the same base, but no source/card path is changed here and no false
hard dependency or approval is transferred. Issue6 consumes accepted artifact and
pure-law boundaries later; its live transport/lifecycle feature work is excluded.

## Every original acceptance criterion has an owner

| Issue4 criterion | Proposed stories and concrete proof |
| --- | --- |
| No committed runtime token/message/real event identity/queue/local path | BT4.01 artifact-role and prohibited-payload contracts; BT4.03 full tracked/release-tree scan plus fictional hidden/release-only negative probes. Current absence is insufficient. |
| Fail-closed secret/privacy CI scans over full repository | BT4.01 rules/fixture cases and BT4.03 actual hosted scan with error/negative controls, no diff-only or broad provenance exemption. |
| Clean checkout builds export from source | BT4.02 frozen pnpm/toolchain recipe with fresh source/output/cache roots, no global dependencies or stale output. |
| Two clean builds have identical output hashes | BT4.02 independent clean checkout pair at one immutable SHA, compare every selected output byte/hash and provenance. |
| Built plugin smoke exposes start/stop | BT4.02 exported-file-only CommonJS factory/fake-BdApi smoke outside source/dependency tree, positive and nonzero failure cases. |
| Generated drift detected or excluded/release artifacts | BT4.01 authoritative-source/generated-role policy, BT4.02 rebuild/output rule, BT4.03 hosted enforcement and qualified artifact handoff. No release publication activated. |
| Minimal fictional schema-validated example | BT4.01 unconditionally adds `fixtures/betterdiscord-meta.example.json` for the current meta-factory, containing minimal fictional nonblank name/version/description strings, and executes its owned schema against that actual file before fake smoke. Additional runtime config remains conditional on a separately reviewed source import, with a separate fictional example/schema before import. No guessed issue6 transport shape. |
| Source/fixture/archive/build/runtime docs distinguished | BT4.01 role/license/source table and explicit absent-archive observation; BT4.03 evidence records current SHA/raw versions/commands/exits/hashes and scope. |

Pseudo candidate policy: retain only an explicitly licensed/provenanced archive
input or a deterministic generated output, never silently authoritative source.
No branch-wide transplant or hand-edited generated export. Runtime configs,
queues, caches, credentials, local state, session artifacts and machine links are
excluded from product/archive imports. Current immutable source provenance and
ledger prefixes stay preserved; if their contents conflict with full-tree
sanitation, surface a concrete blocker rather than inventing exemptions or
rewriting history. License attributions and immutable SHA records are distinguished
from prohibited event identities by explicit contract, not broad path allowances.

## Provisional estimates and initial UUID graph

- BT4.01 `6fe3cf31-866d-4d6b-9c90-0645993cf27c` —3pt, no dependency.
- BT4.02 `522a0b65-0fcb-43d7-a338-614af8cf3856` —3pt, depends on BT4.01.
- BT4.03 `3ec6477d-331f-47bc-8c1e-e9fa4ed2396f` —2pt, depends on both earlier stories.

Each story belongs to epic `ef1097f4-cb92-4318-b7c9-a60d49624272`. These are reviewable initial fields,
not operational transitions. If any story exceeds five points, obtain reviewed
Rheos breakdown instead of silently growing it. No dependency on law5/adapters6 is
needed for the current tiny scaffold artifact proof, and their planning admission
is not inferred from this plan.

## Pure contract and host ownership

The proposed shared artifact law belongs in portable `.cljc` when practical,
for example `src/bitch_tracker/artifact/law.cljc`: fixture shape checks, artifact
classification and manifest validity/identity decisions consume and return
Clojure-shaped data. Corresponding CLJS law tests run through the existing
Shadow-CLJS test target; pnpm/Shadow ownership remains unchanged. No source files
or fixture are implemented by this planning PR.

The unconditional future fixture `fixtures/betterdiscord-meta.example.json`
contains only fictional metadata for the existing name/version/description
boundary. Its JSON decoding and fake-smoke loading are adapters that execute the
owned schema, including rejection cases. This is distinct from additional runtime
config whose need/shape must be established by a future reviewed source import.

The existing `.mjs` bundler/verifier and proposed `.mjs` scanner/manifest/test
entry points own Node orchestration, hashing, Git/filesystem traversal, JSON
conversion, process exits and host probes. They consume shared pure rules rather
than recreate a JavaScript schema/classification/manifest authority. An adapter
bridge must be explicit and tested at both boundaries; the pure layer depends on
no Node object, filesystem or process API.

## Future red/green execution contract

Current declared product commands, not executed by this planning task:

```sh
pnpm run lint
pnpm test
pnpm build
node scripts/verify-bd-export.mjs
```

After planning/readiness, first add actual failing assertions to the existing
product test, shared portable-law tests and new artifact-contract/probe/smoke
runners. Execute the unconditional metadata example schema and prove rejection,
hidden/release-only synthetic leakage, scanner tool/I/O failure, bad factory/header,
source-tree-dependent export and stale/mismatched output fail nonzero. Missing
future files alone are not meaningful red. Then implement minimal shared artifact
contracts and adapters; finally wire hosted proof. This adds no reaction business
semantics or real transport runtime.

Current CLJS target for the proposed portable-law tests, plus proposed new host
runners (new files do not exist yet; Node wrappers exercise shared rules):

```sh
pnpm run test:cljs
node --test test/artifact-contract.test.mjs
node --test test/artifact-privacy-probes.test.mjs
node scripts/scan-artifact-boundary.mjs --tracked-tree . --release-tree dist
node scripts/verify-artifact-manifest.mjs dist/artifact-manifest.json
node scripts/verify-bd-export.mjs
```

The tracked-tree scanner must derive the complete tracked set from Git, inspect
hidden files and selected release bytes, constrain link traversal and report rule/
path/count/hash only. It is domain artifact checking, never a Rheos parser or
validator. A synthetic violation is distinguishable from real source, never
printed as sensitive-looking content. Current future-cli spellings are proposals,
not a second authority or existing pass claim.

For the build-pair proof, use two independent private clone/worktree roots at the
same immutable source SHA, no hardlinks, separate pnpm/Maven/Clojure/Shadow caches
and no shared outputs. From each root run the reviewed frozen install, `pnpm build`
and hash the selected distributable. Record actual Node/pnpm/Java/Clojure/compiler
and dependency-lock identities before green; preserve pnpm ownership. Do not
pretend existing version ranges or warm `dlx` caches provide frozen inputs.
Exact install/cache flags must be validated for the chosen tools during admitted
implementation, not guessed as currently working here.

Smoke copies the distributable alone plus declared public notices to a private
directory with fake BdApi and the schema-validated fictional metadata example. It runs without network,
credentials, profile, repository source/build/node_modules access or outgoing
messages. Existing fake smoke is reusable evidence intent, not current proof of
that stricter extraction boundary. Freeze generated bytes; timestamps/host labels
may be accountable execution metadata but cannot perturb the artifact identity.
Manifest records source/toolchain/recipe and output hashes without self-hash cycles.

Current only hosted workflow is the accepted pinned eta-mu review caller
`2b918cdab2ebd30e745bb8fa86d077d7a3af0030`, nondraft/same-repository PR and
contents-read/PR-read permissions. Its diff-stat gate is not product proof.
Future product CI must use read-only tokens without signing/deployment secrets,
immutable actions/native inputs and complete path filters. CI attachments are
evidence; release publication/promotion remains separately authorized. Keep native
review availability, required checks, deterministic acceptance and human acceptance
distinct. No workflow/settings changes or manual bots are included in this plan.

## Evidence and completion boundaries

Actual installed Rheos default is `docs/agile/tasks`. Initial read emitted ENOENT
with a zero-card diagnostic and exit0; this is a collection limitation, not valid
board admission. Subsequent native reads of authored initial cards must preserve
raw exit/stderr/output and actual states/UUID/dependencies. Engine-created empty
event output stays outside the staged change. No operational board mutation or
repo-local semantic parser/transition surface is created.

Own receipt envelopes, lossless diagnostic captures, unchanged existing source/
provenance bytes and complete base-to-head diff hygiene qualify local preparation
only. Native review and lawful ready transitions remain required. All eight
criteria must have accepted exact-head hosted evidence before issue4 can close;
a reviewable plan, missing old payload or fake local smoke alone cannot do that.
