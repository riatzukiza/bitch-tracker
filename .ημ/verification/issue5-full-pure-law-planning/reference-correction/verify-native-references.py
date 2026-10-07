#!/usr/bin/env python3
"""Check captured transport references; never interpret board semantics."""
import argparse, base64, hashlib, json
from pathlib import Path

def references(value):
    """Yield native transport record objects recursively, without board interpretation."""
    if isinstance(value, dict):
        path = value.get("path")
        if isinstance(path, str) and path.startswith("native/"):
            yield value
        for child in value.values():
            yield from references(child)
    elif isinstance(value, list):
        for child in value:
            yield from references(child)

EXPECTED_REFERENCES = {
    'native-inventory-manifest.json': (
        'native/octave-commons-Truth.stdout.b64',
        'native/octave-commons-Truth.stderr.b64',
        'native/riatzukiza-Truth.stdout.b64',
        'native/riatzukiza-Truth.stderr.b64',
        'native/octave-commons-epiphany.stdout.b64',
        'native/octave-commons-epiphany.stderr.b64',
        'native/riatzukiza-epiphany.stdout.b64',
        'native/riatzukiza-epiphany.stderr.b64',
        'native/octave-commons-bitch-tracker.stdout.b64',
        'native/octave-commons-bitch-tracker.stderr.b64',
        'native/riatzukiza-bitch-tracker.stdout.b64',
        'native/riatzukiza-bitch-tracker.stderr.b64',
        'native/open-hax-opencode.stdout.b64',
        'native/open-hax-opencode.stderr.b64',
        'native/riatzukiza-opencode.stdout.b64',
        'native/riatzukiza-opencode.stderr.b64',
    ),
    'bitch1-full-scope-manifest.json': (
        'native/bitch1-full.stdout.b64',
        'native/bitch1-full.stderr.b64',
        'native/bitch1-files.stdout.b64',
        'native/bitch1-files.stderr.b64',
    ),
    'bitch1-canonical-first.json': (
        'native/bitch1-canonical-first.stdout.b64',
        'native/bitch1-canonical-first.stderr.b64',
    ),
}

def verify(root):
    """Validate the complete expected transport identities, metadata and containment."""
    failures = []
    count = 0
    paths = set()
    identities = []
    for required in EXPECTED_REFERENCES:
        if not (root / required).is_file():
            failures.append({"manifest": required, "error": "required native manifest missing"})
    for manifest in sorted(root.glob("*.json")):
        try:
            value = json.loads(manifest.read_text())
        except (OSError, ValueError) as error:
            failures.append({"manifest": manifest.name, "error": str(error)})
            continue
        for entry in references(value):
            count += 1
            identities.append((manifest.name, entry["path"]))
            relative = Path(entry["path"])
            paths.add(str(relative))
            artifact = root / relative
            try:
                if not isinstance(entry.get("bytes"), int) or isinstance(entry.get("bytes"), bool) or entry["bytes"] < 0:
                    raise ValueError("invalid decoded byte count")
                digest = entry.get("sha256")
                if not isinstance(digest, str) or len(digest) != 64 or any(c not in "0123456789abcdef" for c in digest):
                    raise ValueError("invalid SHA256 metadata")
                if relative.is_absolute() or ".." in relative.parts:
                    raise ValueError("reference leaves evidence root")
                resolved_root = root.resolve()
                resolved_artifact = artifact.resolve()
                try:
                    resolved_artifact.relative_to(resolved_root)
                except ValueError:
                    raise ValueError("reference resolves outside evidence root")
                encoded = resolved_artifact.read_bytes()
                if not encoded.endswith(b"\n") or encoded.endswith(b"\n\n"):
                    raise ValueError("expected exactly one terminal LF")
                raw = base64.b64decode(encoded[:-1], validate=True)
                if base64.b64encode(raw) + b"\n" != encoded:
                    raise ValueError("noncanonical base64")
                if len(raw) != entry["bytes"] or hashlib.sha256(raw).hexdigest() != entry["sha256"]:
                    raise ValueError("decoded size/SHA mismatch")
            except (OSError, ValueError) as error:
                failures.append({"manifest": manifest.name, "path": str(relative), "error": str(error)})
    expected = {(manifest, path) for manifest, paths_ in EXPECTED_REFERENCES.items() for path in paths_}
    observed = set(identities)
    for manifest, path in sorted(expected - observed):
        failures.append({"manifest": manifest, "path": path, "error": "expected native reference missing"})
    for manifest, path in sorted(observed - expected):
        failures.append({"manifest": manifest, "path": path, "error": "unexpected native reference identity"})
    if len(identities) != len(observed):
        failures.append({"error": "duplicate native reference identity"})
    if count != len(expected):
        failures.append({"error": "native reference count differs from required complete set"})
    return {"references": count, "unique_paths": len(paths), "failures": failures, "ok": not failures}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True, type=Path)
    args = parser.parse_args()
    result = verify(args.root)
    print(json.dumps(result, sort_keys=True))
    raise SystemExit(0 if result["ok"] else 1)
