---
uuid: "ef1097f4-cb92-4318-b7c9-a60d49624272"
title: "BT4 — Sanitize and prove deterministic source-only plugin artifacts"
status: "incoming"
type: "epic"
priority: "P1"
points: "8"
labels: "planning, artifacts, privacy, reproducibility"
category: "epics"
---

# BT4 — Sanitize and prove deterministic source-only plugin artifacts

## Context

Issue: https://github.com/octave-commons/bitch-tracker/issues/4

Current personal/origin main: `4f1015bae457e6b4890f80a5d312f4259fce3ddb`. The existing source-only scaffold,
bundler and export smoke are current authority; closed-unmerged PR1
`693f1388e61bd268814f85d1a40ef15a4485e6a3` and PR2
`c48c8e45366e592b30cdbbcf54f016d585b0e646` are provenance only. Their historical
772,060-byte configuration / 460 queued-event counts are reported issue evidence,
not newly inspected content. No old runtime snapshot, message or identifier is
retrieved or imported by this planning candidate.

Current main tracks no `pseudo/` archive/config snapshot and no generated build
or dist artifact. README still calls `pseudo/` the archive; reconcile that stale
prose through the future source-classification contract. Absence today is not a
historical purge, a full privacy-scan pass, or issue closure.

## Outcome

All eight issue4 acceptance criteria have explicit implementation owners and
revision-bound proof: a sanitized source/fixture/archive/output boundary, two
clean reproducible builds and a hermetic BetterDiscord export, enforced by
fail-closed hosted full-tree/privacy/artifact gates.

## Proposed breakdown and scope

| Story | UUID | Points | Initial proposed dependencies |
| --- | --- | --- | --- |
| BT4.01 Source/fixture/privacy contract | `6fe3cf31-866d-4d6b-9c90-0645993cf27c` | 3 | None |
| BT4.02 Reproducible source-only export | `522a0b65-0fcb-43d7-a338-614af8cf3856` | 3 | BT4.01 |
| BT4.03 Hosted full-tree/provenance/drift proof | `3ec6477d-331f-47bc-8c1e-e9fa4ed2396f` | 2 | BT4.01 and BT4.02 |

The 8-point epic is the sum 3+3+2, not an 8-point implementation story. Estimates
and the initial dependency graph are proposals requiring native planning review.
Use Rheos for any later operational status/frontmatter/comment/transition change.

## Non-goals

Reaction/dedup/watchlist semantics belong to issue5 and [personal planning PR1](https://github.com/riatzukiza/bitch-tracker/pull/1),
reaction story UUID `acfa4cdf-a7b4-43d2-a165-eeffff40ce3d`. Discord/Socket.IO/
OpenPlanner runtime integration belongs to issue6. Those are body references,
not false hard dependencies on unavailable foreign cards. No live client/profile,
credentials, private snapshot, service, provider, external messages, historical
rewrite, process activation, release publication or deployment is authorized.

## Acceptance criteria

- Every issue4 criterion resolves to the [proof map](../notes/artifact-boundary-plan.md).
- Each story stays bounded at no more than five points, with real contracts and
  failing assertions before green implementation, then adapters/hosted proof.
- Source CLJS remains authoritative. Each retained pseudo plugin candidate is a
  licensed/provenanced archive input or a deterministic output; never both or
  silently authoritative source.
- Full committed/release-tree scans fail closed on forbidden runtime payloads,
  credentials, real event identities, queues and machine-specific paths. Synthetic
  probes produce no sensitive log/capture output. Current corpus absence does
  not waive scanning.
- The current meta-factory has a minimal fictional
  `fixtures/betterdiscord-meta.example.json` with an executed owned schema,
  unconditionally; it does not inherit real records or wait for a future import.
  Pure schema/classification/manifest decisions stay portable `.cljc` when
  practical; JSON/Node/I/O/build runners are outer adapters with Clojure-shaped
  semantic boundaries. A future import needing runtime config is blocked until an explicit fictional
  example/schema exists; no invented transport schema is smuggled into this epic.
- Two independent clean builds, isolated exported-file smoke and generated-drift/
  release-artifact policy have current-head hosted evidence and owned receipts.

## Verification

Planning preparation uses actual native Rheos readback of these four initial
Markdown inputs, receipt-envelope checks, exact unchanged source/provenance
prefixes and full base-to-head diff hygiene. No implementation or build pass is
claimed in this PR. Native planning qualification and lawful ready transitions
are prerequisites before work starts on the implementation stories.

## Risks

Transitive dependency drift, checkout path leakage, source-dependent Node exports,
privacy false negatives and conflicting immutable evidence policies can defeat
superficially green builds. Preserve original hashes/history; surface any conflict
with sanitation rather than broadly exempting provenance or rewriting receipts.
