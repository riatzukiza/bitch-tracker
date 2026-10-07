# Resolved artifact containment repair

Native review 5442714787, P2 inline 4207234458, thread
`PRRT_kwDOU4Vc586p6oGF`, item `cr-comment:v1:7dbcf00263c2b4d7b508a6e0`
correctly identifies a symlink escape in the transport-reference checker.
Canonical status succeeded before the full review read. Full review has one
inline and no separate body/nitpick/outside obligation beyond its repeated prompt.
Safe native views with withheld query values retain original rawhash/private provenance.

At published 9c3, a harmless external-file link and intermediate-directory link
both passed when their fictional sentinel bytes matched a manifest. The before
probe preserves both exit 0 results; all fixtures and the external sentinel are
inside this lane’s private directory, with no real host secret or board access.
The sentinel bytes remain unchanged. This confirms containment failure only,
not an observed real-host leak or concurrent race.

The minimal suggested correction resolves the evidence root and artifact,
checks relative containment, and reads the validated resolved artifact. Lexical
absolute/`..` rejection remains. Existing 22 valid references and four hostile
controls remain; new external-file and intermediate-directory escapes fail.
In-root file/directory symlinks and root aliases succeed; explicit `..` still
fails. The after matrix has 11 cases and all expected exit/result checks pass.
Python compilation passes. No speculative TOCTOU or schema/board overhaul occurs.

All historical captures, manifests, failures, cards/notes, original seven
concepts/eight invariants/seven proofs/seven reaction criteria and proposed 13-point
sizing/Incoming metadata remain exact. One correcting Receipt River row and
canonical portable reflection append only; no history rewrite or live event.
No Rheos operation, application implementation/test suite, provider request,
service, native write, push or settlement occurs. Root owns publication after
a distinct frozen peer; native review/cooldown/convergence remain separate.


## Accountable local result

Actual current Receipt River 154440 validates declared rows 3, 4 and corrective
row 5 at the working tip; both inherited flat rows remain refused and unchanged.
Canonical portable reflection reader recognizes the appended standard entry.
All eight command entries distinguish exact local streams from separately
labelled safe native review views. Final immutable source/API/object/prefix proof
is outside this candidate; no self-review is native approval or Ready evidence.
