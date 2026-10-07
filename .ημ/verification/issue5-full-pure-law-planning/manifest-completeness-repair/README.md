# Exact native reference completeness correction

Native CodeRabbit review **5443573568**, root **4207929993**, thread
**PRRT_kwDOU4Vc586p8WWL**, item **cr-comment:v1:b766ae10a69495b6e2adb4d9**
identified an actual P1 false success in the transport-reference checker on
published **5bb822ebd871797ef789b68c42620a861e1da8cf**. The full review covers
all 138 changed paths and reports one actionable inline. This packet is a local
correction, with no provider request, native settlement, approval or round credit.

The baseline accepts four hostile complete-fixture variants: deleting the inventory
manifest and its 16 artifacts leaves six valid references; omitting one reference
leaves 21; substituting a valid fictional path preserves a count of 22; duplicating
another path also leaves 22 records. All four return `ok: true` / exit 0 before
this correction. The helper now requires all three named manifests and the exact
22 `(manifest name, relative path)` identities, rejects duplicates and incorrect
counts, and refuses malformed byte/hash metadata and manifest JSON. Counts alone
cannot authorize success. This fixed evidence packet is the authority for those
transport identities; the helper does not interpret board semantics.

The existing root/artifact resolution, `relative_to` containment and validated
resolved-path read remain unchanged. The final 23-case run preserves all eleven
prior semantic outcomes using **full 22-reference fixtures**, rather than allowing
new completeness refusal to mask symlink testing. External file and intermediate
directory symlinks produce an explicit containment error. In-root file/directory
symlinks and a root alias still succeed; lexical `..`, missing artifacts, wrong
bytes, noncanonical wrappers and empty inputs fail. Three missing-manifest controls,
omitted/replaced/duplicated identities, missing/malformed metadata, malformed JSON
and an unexpected duplicate identity fail. Fictional other-owner sentinel bytes
remain unchanged. These single-process fixtures establish no live leakage or
TOCTOU guarantee.

Run the actual transport checker with Python 3; run `probe-completeness.py` with
`--checker`, `--evidence`, a fresh private `--fixtures` directory and `--phase after`.
It calls the checker as a subprocess and asserts actual JSON verdicts and exits.
The `before` phase needs the immutable baseline helper. Python AST compilation
also passes. Application/backend/Discord tests, build, providers, board state,
services and credentials are outside this transport-only repair.

`command-captures.json` aggregates exact decoded stdout/stderr with bytes/SHA256
and canonical base64 **strings without LF**, not separate one-LF files. Historical
captures retain their original grammars and bytes. `native-review-views.json`
contains complete structurally redacted native review/inline views and CLI thread
text, with raw SHA256/size and private original locations: those safe views are
**not raw-lossless native captures**. Canonical status succeeded before detailed
native reads. Native Essentials footer says zero included reviews remain and one
review/hour, without a reset deadline; no capacity or convergence is inferred.

The current immutable Receipt River owner 154440f3c997aa9208194bba59b5edbef3654f78
is byte-verified across all 15 copied source files. Its actual API validates new
row 6 and the declared owned rows 3–6; the two inherited flat-format refusals remain
visible. A canonical portable Session Mycology `- ts:` reflection is appended and
read back with the actual BB tools in the explicit owned worktree. No live event,
spore, promotion or global helper root walk runs. Setup mistakes and their scoped
corrections are retained in `owner-source-and-setup.json`.

All original seven concepts, eight invariants, seven proofs, seven reaction criteria,
Incoming metadata, proposed aggregate 13-point scope, all 22 restored streams,
previous manifests/captures, historical receipts/reflections and source/workflow/
configuration/event bytes remain unchanged except the checker and append-only
accountability/index additions. The full immutable proof and publication input
are sealed outside the source after an ordinary local successor commit. Root alone
may publish and settle following distinct independent verification.
