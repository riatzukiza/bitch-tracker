---
uuid: "3ec6477d-331f-47bc-8c1e-e9fa4ed2396f"
title: "BT4.03 — Enforce full-tree privacy, artifact drift and provenance in CI"
status: "incoming"
type: "story"
priority: "P1"
points: "2"
labels: "planning, artifacts, privacy, reproducibility"
category: "stories"
epic: "ef1097f4-cb92-4318-b7c9-a60d49624272"
parent: "ef1097f4-cb92-4318-b7c9-a60d49624272"
dependency: ["6fe3cf31-866d-4d6b-9c90-0645993cf27c", "522a0b65-0fcb-43d7-a338-614af8cf3856"]
---

# BT4.03 — Enforce full-tree privacy, artifact drift and provenance in CI

## Context

Issue: https://github.com/octave-commons/bitch-tracker/issues/4

Current personal/origin main: `4f1015bae457e6b4890f80a5d312f4259fce3ddb`. The existing source-only scaffold,
bundler and export smoke are current authority; closed-unmerged PR1
`693f1388e61bd268814f85d1a40ef15a4485e6a3` and PR2
`c48c8e45366e592b30cdbbcf54f016d585b0e646` are provenance only. Their historical
772,060-byte configuration / 460 queued-event counts are reported issue evidence,
not newly inspected content. No old runtime snapshot, message or identifier is
retrieved or imported by this planning candidate.

Current main has only the pinned eta-mu native-review caller, with a diff-stat
evidence gate. It has no hosted product build, full-tree sanitation or artifact
reproducibility gate. Review availability is separate from deterministic proof.

## Outcome

Current-head hosted checks run all eight issue4 obligations against the complete
committed tree and selected release tree, producing sanitized, reachable evidence
without signing or deployment authority.

## Scope

- Integrate admitted BT4.01 contracts/probes and BT4.02 two-root build/smoke in a
  dedicated least-privilege product-artifact job; pin action/native inputs and
  include source/tests/scripts/config/fixtures/policy paths in triggers.
- Scan every tracked file, including hidden paths, plus the complete selected
  artifact tree. Do not follow repository symlinks outside the checkout or scan
  Git history/operator caches/profiles as a purported full-tree substitute.
- Execute seeded fictional negative probes in both trees; no payload is echoed
  into diagnostic/evidence artifacts. Missing tools, unreadable files, scanner
  failures and rejected fixtures must fail closed.
- Rebuild and compare or keep generated output excluded and attach qualified
  version-bound artifacts through the reviewed distribution policy. CI artifact
  retention is evidence; repository-release publication remains a separate
  authorized promotion, with no automatic release/controller activation here.
- Persist immutable source SHA, raw tool versions/commands/exits, artifact and
  evidence hashes, scope, scan counts, fixture outcomes, smoke and drift result in
  an owned Receipt River handoff. Never rewrite past receipts/provenance.

## Non-goals

Optional reviewer identity/approval fabrication, suppressing current required
checks, credentials/protection/settings changes, App or deployment token exposure
to candidate product code, paid reviews, live services or Discord messages.

## Acceptance criteria

- Hosted exact-head evidence proves all eight issue4 criteria, including the
  fictional schema-bound example and licensed/provenanced artifact classification.
- Full-tree scan fails on seeded hidden/release-only leaks and on tool/I/O errors;
  no broad exclusions turn findings into a pass.
- Clean build pair, isolated smoke and deliberate failure propagation execute,
  with machine-readable outcomes and exact hashes; source-only existence is not proof.
- Generated-file drift and the selected release-artifact policy are enforced,
  with no stale/partial artifact accepted.
- Jobs executing candidate code have read-only tokens and no signing/deployment
  secrets; privileged publication is separately admitted by trusted machinery.
- Receipts/evidence are reachable at the tested head, respect original byte
  prefixes and make unavailable actions explicit. No issue closure or card done
  claim precedes accepted proof for its full scope.

## Verification

Depend on admitted BT4.01 and BT4.02. Add a failing gate/probe/failure-propagation
case before wiring green; then exercise hosted jobs at the exact candidate head
and preserve IDs/check states. Local preparation cannot replace hosted admission.
See the [eight-criterion proof map](../notes/artifact-boundary-plan.md).

## Risks

Path-filter gaps, diffs mistaken for full-tree scans, unsanitized scanner output,
mutable tool inputs and privileged candidate hooks can invalidate otherwise green
checks. If the existing caller prerequisite is unavailable, retain its real state
and use the existing owner issue rather than bypassing it or duplicating intake.
