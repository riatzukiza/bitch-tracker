---
uuid: "522a0b65-0fcb-43d7-a338-614af8cf3856"
title: "BT4.02 — Prove two clean source-only builds and isolated export smoke"
status: "incoming"
type: "story"
priority: "P1"
points: "3"
labels: "planning, artifacts, privacy, reproducibility"
category: "stories"
epic: "ef1097f4-cb92-4318-b7c9-a60d49624272"
parent: "ef1097f4-cb92-4318-b7c9-a60d49624272"
dependency: ["6fe3cf31-866d-4d6b-9c90-0645993cf27c"]
---

# BT4.02 — Prove two clean source-only builds and isolated export smoke

## Context

Issue: https://github.com/octave-commons/bitch-tracker/issues/4

Current personal/origin main: `4f1015bae457e6b4890f80a5d312f4259fce3ddb`. The existing source-only scaffold,
bundler and export smoke are current authority; closed-unmerged PR1
`693f1388e61bd268814f85d1a40ef15a4485e6a3` and PR2
`c48c8e45366e592b30cdbbcf54f016d585b0e646` are provenance only. Their historical
772,060-byte configuration / 460 queued-event counts are reported issue evidence,
not newly inspected content. No old runtime snapshot, message or identifier is
retrieved or imported by this planning candidate.

Current package commands use pnpm and pinned Shadow-CLJS3.4.11. Main has a CLJS
factory, metadata bundler and fake-BdApi verifier, but no package-manager lock or
revision-bound clean-build reproducibility proof. Existing smoke execution inside
the source tree does not establish a portable exported artifact.

## Outcome

An exact source/toolchain recipe builds byte-identical BetterDiscord exports in
two independent clean roots and loads the exported file outside its source/build/
dependency tree with only a fake local API surface.

## Scope

- Retain pnpm policy and compiler3.4.11; declare supported exact Node/pnpm/Java/
  Clojure/compiler/dependency identities and lock inputs before green. Add a
  reviewed frozen dependency recipe without changing package-manager ownership.
- Build the same immutable source revision in two separate private checkouts and
  cache/output roots. No hardlinks/shared writable dependencies or global installs.
- Emit a small deterministic artifact manifest with source SHA, recipe/toolchain
  identity, relative artifact path/size/hash and license record. Exclude wall-clock
  time, local absolute paths, host state and manifest self-hash cycles.
- Copy only the selected distributable artifact and declared public notices to a
  fresh smoke directory. Verify CommonJS `meta => plugin`, metadata and start/stop
  lifecycle using the current fictional fake-BdApi surface; no source-tree reads,
  hidden node_modules dependency, network, client profile or messages.

## Non-goals

Reaction/adapters or plugin feature changes, provider integration, binary runtime
packaging, external artifact/release publication, services, signing or deployment.

## Acceptance criteria

- Two fresh independent source builds have identical plugin bytes and SHA-256;
  same-root warm repeat alone is insufficient.
- Missing compiler/dependency/input, incompatible runtime and altered recipe
  fail truthfully; no stale generated bundle can substitute for compilation.
- The isolated final bundle exposes the expected factory/start/stop contract;
  fake-only lifecycle succeeds without the repository tree or live credentials.
- An intentional bad header/export/lifecycle failure exits nonzero. Assertion
  failures propagate through every wrapper used to build/smoke.
- Provenance matches the actual immutable source, selected toolchain and output
  bytes. Commit no runtime config, generated session state or local path.
- `.gitignore` and reviewed distribution policy keep generated outputs out of
  hand editing; no compiled drift is silently accepted as source authority.

## Verification

After admitted BT4.01, write failing recipe/manifest and isolated-smoke assertions,
then minimally adjust build/bundle/verification adapters and record both clean
runs' raw versions, commands, exits and hashes. Future CLI invocations are listed
in the [execution contract](../notes/artifact-boundary-plan.md), explicitly not
executed by this planning PR.

## Risks

Unfrozen Maven/npm edges, compile-time path/timestamp leakage and Node-script
runtime imports may prevent standalone reproducibility. Report those actual
failures; do not silently change compiler targets or claim BetterDiscord live
runtime acceptance from a fake smoke.
