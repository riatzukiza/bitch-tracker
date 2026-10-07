#!/usr/bin/env python3
"""Exercise transport containment with fictional files; no board semantics."""
import argparse, base64, hashlib, json, shutil, subprocess
from pathlib import Path

def main(checker, evidence, fixtures, phase):
    fixtures.mkdir(parents=True, exist_ok=False)
    encoded = base64.b64encode(b"fictional independently owned sentinel") + b"\n"
    raw = base64.b64decode(encoded[:-1], validate=True)
    external = fixtures / "external-owner"
    external.mkdir()
    sentinel = external / "sentinel.b64"
    sentinel.write_bytes(encoded)
    identity = hashlib.sha256(sentinel.read_bytes()).hexdigest()
    record = {"path": "native/sentinel.b64", "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()}
    results = []
    def fixture(name):
        root = fixtures / name
        root.mkdir()
        (root / "manifest.json").write_text(json.dumps({"stdout": record}))
        return root
    def run(name, root, expected):
        command = ["python", str(checker), "--root", str(root)]
        result = subprocess.run(command, capture_output=True, text=True, timeout=20)
        value = json.loads(result.stdout)
        if result.returncode != expected or value["ok"] != (expected == 0):
            raise AssertionError({"name": name, "exit": result.returncode, "expected": expected, "value": value})
        results.append({"name": name, "argv": command, "exit": result.returncode, "expected": expected, "result": value, "stderr": result.stderr})
    file_root = fixture("external-file")
    (file_root / "native").mkdir()
    (file_root / "native/sentinel.b64").symlink_to(sentinel)
    directory_root = fixture("external-directory")
    (directory_root / "native").symlink_to(external, target_is_directory=True)
    run("external-file-symlink", file_root, 0 if phase == "before" else 1)
    run("external-directory-symlink", directory_root, 0 if phase == "before" else 1)
    if phase == "after":
        run("actual22-reference-positive", evidence, 0)
        for name in ["missing", "bytes", "wrapper", "empty"]:
            root = fixtures / ("old-control-" + name)
            root.mkdir()
            for source in evidence.glob("*.json"):
                shutil.copyfile(source, root / source.name)
            shutil.copytree(evidence / "native", root / "native")
            target = root / "native/bitch1-full.stdout.b64"
            if name == "missing": target.unlink()
            elif name == "bytes": target.write_bytes(base64.b64encode(b"wrong bytes") + b"\n")
            elif name == "wrapper": target.write_bytes(target.read_bytes() + b"\n")
            else:
                for source in root.glob("*.json"): source.write_text("{}\n")
            run("old-negative-" + name, root, 1)
        internal = fixture("internal-file")
        (internal / "native").mkdir()
        (internal / "owned.b64").write_bytes(encoded)
        (internal / "native/sentinel.b64").symlink_to(internal / "owned.b64")
        run("internal-file-symlink-positive", internal, 0)
        internal_directory = fixture("internal-directory")
        (internal_directory / "owned").mkdir()
        (internal_directory / "owned/sentinel.b64").write_bytes(encoded)
        (internal_directory / "native").symlink_to(internal_directory / "owned", target_is_directory=True)
        run("internal-directory-symlink-positive", internal_directory, 0)
        alias = fixtures / "root-alias"
        alias.symlink_to(internal, target_is_directory=True)
        run("root-alias-positive", alias, 0)
        lexical = fixture("lexical-dotdot")
        (lexical / "manifest.json").write_text(json.dumps({"stdout": {**record, "path": "native/../owned.b64"}}))
        (lexical / "owned.b64").write_bytes(encoded)
        run("lexical-dotdot-negative", lexical, 1)
    if hashlib.sha256(sentinel.read_bytes()).hexdigest() != identity:
        raise AssertionError("fictional other-owner sentinel changed")
    print(json.dumps({"phase": phase, "cases": results, "sentinel_sha256": identity, "sentinel_unchanged": True, "limits": "single-process harmless owned fixtures; no live host evidence or TOCTOU guarantee"}, sort_keys=True))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--checker", required=True, type=Path)
    parser.add_argument("--evidence", required=True, type=Path)
    parser.add_argument("--fixtures", required=True, type=Path)
    parser.add_argument("--phase", required=True, choices=["before", "after"])
    args = parser.parse_args()
    main(args.checker, args.evidence, args.fixtures, args.phase)
