---
uuid: "6fe3cf31-866d-4d6b-9c90-0645993cf27c"
title: "BT4.01 — Define source, fixture and artifact sanitation contracts"
status: "incoming"
type: "story"
priority: "P1"
points: "3"
labels: "planning, artifacts, privacy, reproducibility"
category: "stories"
epic: "ef1097f4-cb92-4318-b7c9-a60d49624272"
parent: "ef1097f4-cb92-4318-b7c9-a60d49624272"
---

# BT4.01 — Define source, fixture and artifact sanitation contracts

## Context

Issue: https://github.com/octave-commons/bitch-tracker/issues/4

Current personal/origin main: `4f1015bae457e6b4890f80a5d312f4259fce3ddb`. The existing source-only scaffold,
bundler and export smoke are current authority; closed-unmerged PR1
`693f1388e61bd268814f85d1a40ef15a4485e6a3` and PR2
`c48c8e45366e592b30cdbbcf54f016d585b0e646` are provenance only. Their historical
772,060-byte configuration / 460 queued-event counts are reported issue evidence,
not newly inspected content. No old runtime snapshot, message or identifier is
retrieved or imported by this planning candidate.

This story supplies the explicit artifact boundary required before a closed branch
is lifted. Current main's absent pseudo/config payload needs no speculative purge.
Existing `.ημ/Π_*` source provenance remains unchanged in planning.

## Outcome

A reviewable, enforceable contract classifies current inputs and any proposed
archive/output import, excludes runtime/session state, and defines fictional
examples plus the full-tree privacy scan's positive/negative cases.

## Scope

- Inventory tracked source, third-party lint imports, docs, provenance, symlinks,
  existing fake smoke/test fixtures and generated outputs without following links
  or traversing `.git`, external profiles, caches or sibling repositories.
- Classify `src/` as authoritative CLJS, `build/` and `dist/` as generated outputs,
  minimal examples as fictional schema-bound fixtures and `pseudo/*.plugin.js`
  candidates as either explicitly licensed/provenanced archives or build outputs.
- Record source SHA, license/notice, role, toolchain/recipe identity and expected
  hash for each retained generated artifact. Preserve attribution and immutable
  provenance; no copied unknown-license branch content is allowed.
- Define a fixture schema for the existing meta-factory smoke metadata. If a
  future source import requires additional config, author a minimal fictional
  `.example.json` with its owned schema before importing; do not port legacy
  config, queue, messages, identifiers or guessed issue6 transport semantics.
- Declare ignore/sanitization policy for runtime configs, queues, credentials,
  local state, sessions, caches and machine-specific links/absolute paths.
  Future source-tree hygiene changes are implementation, not this plan.

## Non-goals

Compiler/build changes, source runtime behavior, reaction law5, adapters6,
credential detection against the operator's machine, historical rewriting, live
Discord/profile/network actions, release publication and deployment.

## Acceptance criteria

- Current artifact-role table names all tracked input classes and the absent
  pseudo/config observation separately from historical reports.
- Each candidate pseudo plugin has one explicit role, license/source record and
  immutable provenance before retention; deterministic output is never hand-edited.
- Fictional fixture schema actually rejects missing/unknown/wrong-type values
  according to the reviewed input contract; no real record is reproduced.
- Negative fixtures cover credential fields, real-event-identity slots, nonblank
  runtime message content, queues, local state and absolute/symlink escapes using
  unmistakably fictional values. Scanner reports only rule/path/count/hash.
- Scope includes hidden tracked files and the complete selected release tree,
  not only the PR diff; no broad provenance/cache exception suppresses bad tracked
  data. Public license attribution and immutable hashes are explicitly distinct
  from prohibited runtime event identity, without arbitrary path allowlists.
- If immutable evidence and sanitation conflict, record a concrete blocker and
  preserve source/history; do not pretend a scan passed or remove its obligation.

## Verification

After native admission, add schema/classification and synthetic privacy-probe
assertions that fail for the correct reason, including seeded leakage at a hidden
tracked path and at a release-only path. Prove scanner I/O errors fail nonzero and
logs do not echo the fixture payload. Future commands and ownership are in the
[execution contract](../notes/artifact-boundary-plan.md). No scan pass is claimed
from file existence or a one-off grep.

## Risks

Overbroad exemptions, numeric-hash false positives, config shapes guessed from
stale sources and symlink traversal can invalidate the boundary. The story is
3 points provisionally; split further through reviewed Rheos if actual contract
implementation exceeds five points.
