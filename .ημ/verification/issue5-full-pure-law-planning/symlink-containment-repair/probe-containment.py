#!/usr/bin/env python3
"""Exercise transport containment with complete private fixtures, never board semantics."""
import argparse, base64, hashlib, json, shutil, subprocess, sys
from pathlib import Path


def main(checker, evidence, fixtures, phase):
    """Assert the historical symlink outcomes against complete 22-reference inputs."""
    fixtures.mkdir(parents=True, exist_ok=False)
    target = Path("native/bitch1-full.stdout.b64")
    external = fixtures / "external-owner"
    external.mkdir()
    sentinel = external / "sentinel.b64"
    sentinel.write_bytes((evidence / target).read_bytes())
    identity = hashlib.sha256(sentinel.read_bytes()).hexdigest()
    results = []

    def fixture(name):
        """Copy all three required manifests and the unchanged native artifacts."""
        root = fixtures / name
        root.mkdir()
        for source in evidence.glob("*.json"):
            shutil.copyfile(source, root / source.name)
        shutil.copytree(evidence / "native", root / "native")
        return root

    def run(name, root, expected, reason=None):
        """Check actual subprocess verdict, exit and specific refusal when supplied."""
        command = [sys.executable, str(checker), "--root", str(root)]
        result = subprocess.run(command, capture_output=True, text=True, timeout=20)
        value = json.loads(result.stdout)
        if result.returncode != expected or value["ok"] != (expected == 0):
            raise AssertionError({"name": name, "exit": result.returncode, "expected": expected, "value": value})
        if reason and not any(reason in str(f.get("error", "")) for f in value["failures"]):
            raise AssertionError({"name": name, "missing_refusal_reason": reason, "value": value})
        results.append({"name": name, "argv": command, "exit": result.returncode, "expected": expected, "result": value, "stderr": result.stderr})

    file_root = fixture("external-file")
    (file_root / target).unlink()
    (file_root / target).symlink_to(sentinel)
    directory_root = fixture("external-directory")
    (directory_root / "native").rename(directory_root / "owned-native")
    external_native = external / "native"
    external_native.mkdir()
    # Only the designated expected artifact resolves outside this fixture.
    # Its siblings resolve back to the original in-root files via the directory.
    for source in (directory_root / "owned-native").iterdir():
        if source.name == target.name:
            shutil.copyfile(sentinel, external_native / source.name)
        else:
            (external_native / source.name).symlink_to(source)
    (directory_root / "native").symlink_to(external_native, target_is_directory=True)
    expected = 0 if phase == "before" else 1
    reason = None if phase == "before" else "resolves outside"
    run("external-file-symlink", file_root, expected, reason)
    run("external-directory-symlink", directory_root, expected, reason)
    if phase == "after":
        run("actual22-reference-positive", evidence, 0)
        for name in ["missing", "bytes", "wrapper", "empty"]:
            root = fixture("old-control-" + name)
            artifact = root / target
            if name == "missing":
                artifact.unlink()
            elif name == "bytes":
                artifact.write_bytes(base64.b64encode(b"wrong bytes") + b"\n")
            elif name == "wrapper":
                artifact.write_bytes(artifact.read_bytes() + b"\n")
            else:
                for source in root.glob("*.json"):
                    source.write_text("{}\n")
            reasons = {"bytes": "decoded size/SHA mismatch", "wrapper": "expected exactly one terminal LF", "empty": "expected native reference missing"}
            run("old-negative-" + name, root, 1, reasons.get(name))
        internal = fixture("internal-file")
        shutil.copyfile(internal / target, internal / "owned.b64")
        (internal / target).unlink()
        (internal / target).symlink_to(internal / "owned.b64")
        run("internal-file-symlink-positive", internal, 0)
        internal_directory = fixture("internal-directory")
        (internal_directory / "native").rename(internal_directory / "owned-native")
        (internal_directory / "native").symlink_to(internal_directory / "owned-native", target_is_directory=True)
        run("internal-directory-symlink-positive", internal_directory, 0)
        alias = fixtures / "root-alias"
        alias.symlink_to(internal, target_is_directory=True)
        run("root-alias-positive", alias, 0)
        lexical = fixture("lexical-dotdot")
        shutil.copyfile(lexical / target, lexical / "owned.b64")
        manifest = lexical / "bitch1-full-scope-manifest.json"
        value = json.loads(manifest.read_text())

        def replace_path(value):
            """Change exactly one known native path, leaving its byte/hash metadata intact."""
            if isinstance(value, dict):
                if value.get("path") == str(target):
                    value["path"] = "native/../owned.b64"
                    return 1
                return sum(replace_path(child) for child in value.values())
            if isinstance(value, list):
                return sum(replace_path(child) for child in value)
            return 0

        if replace_path(value) != 1:
            raise AssertionError("expected exactly one designated native reference")
        manifest.write_text(json.dumps(value))
        run("lexical-dotdot-negative", lexical, 1, "leaves evidence root")
    if hashlib.sha256(sentinel.read_bytes()).hexdigest() != identity:
        raise AssertionError("fictional other-owner sentinel changed")
    print(json.dumps({"phase": phase, "cases": results, "sentinel_sha256": identity, "sentinel_unchanged": True, "limits": "single-process harmless complete private fixtures; no live host evidence or TOCTOU guarantee"}, sort_keys=True))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--checker", required=True, type=Path)
    parser.add_argument("--evidence", required=True, type=Path)
    parser.add_argument("--fixtures", required=True, type=Path)
    parser.add_argument("--phase", required=True, choices=["before", "after"])
    args = parser.parse_args()
    main(args.checker, args.evidence, args.fixtures, args.phase)
