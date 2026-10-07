#!/usr/bin/env python3
"""Exercise complete captured transport identities using private filesystem fixtures."""
import argparse, base64, hashlib, json, os, shutil, subprocess, sys
from pathlib import Path

MANIFESTS = {'native-inventory-manifest.json': ['native/octave-commons-Truth.stdout.b64', 'native/octave-commons-Truth.stderr.b64', 'native/riatzukiza-Truth.stdout.b64', 'native/riatzukiza-Truth.stderr.b64', 'native/octave-commons-epiphany.stdout.b64', 'native/octave-commons-epiphany.stderr.b64', 'native/riatzukiza-epiphany.stdout.b64', 'native/riatzukiza-epiphany.stderr.b64', 'native/octave-commons-bitch-tracker.stdout.b64', 'native/octave-commons-bitch-tracker.stderr.b64', 'native/riatzukiza-bitch-tracker.stdout.b64', 'native/riatzukiza-bitch-tracker.stderr.b64', 'native/open-hax-opencode.stdout.b64', 'native/open-hax-opencode.stderr.b64', 'native/riatzukiza-opencode.stdout.b64', 'native/riatzukiza-opencode.stderr.b64'], 'bitch1-full-scope-manifest.json': ['native/bitch1-full.stdout.b64', 'native/bitch1-full.stderr.b64', 'native/bitch1-files.stdout.b64', 'native/bitch1-files.stderr.b64'], 'bitch1-canonical-first.json': ['native/bitch1-canonical-first.stdout.b64', 'native/bitch1-canonical-first.stderr.b64']}

def records(value):
    """Yield native record objects from the authored transport JSON structure."""
    if isinstance(value, dict):
        if isinstance(value.get("path"), str) and value["path"].startswith("native/"):
            yield value
        for child in value.values(): yield from records(child)
    elif isinstance(value, list):
        for child in value: yield from records(child)

def main(args):
    """Exercise actual checker verdicts on complete private positive and hostile inputs."""
    args.fixtures.mkdir(parents=True, exist_ok=False)
    cases=[]
    def copy(name):
        """Create a complete independently owned fixture without changing evidence."""
        root=args.fixtures/name
        root.mkdir()
        for source in args.evidence.glob("*.json"): shutil.copyfile(source,root/source.name)
        shutil.copytree(args.evidence/"native",root/"native")
        return root
    def edit(root, name, fn):
        """Apply one named manifest mutation in a private fixture."""
        path=root/name; value=json.loads(path.read_text()); fn(value)
        path.write_text(json.dumps(value))
    def run(name,root,expected,reason=None):
        """Assert subprocess exit, JSON verdict and optional specific refusal cause."""
        p=subprocess.run([sys.executable,str(args.checker),"--root",str(root)],capture_output=True,text=True,timeout=20)
        v=json.loads(p.stdout)
        assert p.returncode==expected and v["ok"]==(expected==0), (name,p.returncode,v)
        if reason: assert any(reason in str(f.get("error","")) for f in v["failures"]),(name,v)
        cases.append({"case":name,"exit":p.returncode,"expected":expected,"result":v,"stderr":p.stderr})
    def entries(root,name):
        """Read transport records from one private fixture manifest."""
        return list(records(json.loads((root/name).read_text())))
    def omit(value):
        """Remove only the designated expected reference for the omission control."""
        if isinstance(value,dict):
            for k,v in list(value.items()):
                if isinstance(v,dict) and v.get("path")=="native/bitch1-full.stdout.b64": del value[k];return True
                if omit(v):return True
        elif isinstance(value,list):
            for i,v in enumerate(value):
                if isinstance(v,dict) and v.get("path")=="native/bitch1-full.stdout.b64":del value[i];return True
                if omit(v):return True
        return False
    n=copy("missing-manifest");(n/"native-inventory-manifest.json").unlink()
    for path in MANIFESTS["native-inventory-manifest.json"]:(n/path).unlink()
    run("missing-manifest-with-six-valid-refs",n,0 if args.phase=="before" else 1)
    n=copy("omitted-entry");edit(n,"bitch1-full-scope-manifest.json",omit)
    run("omitted-reference",n,0 if args.phase=="before" else 1)
    n=copy("equal-cardinality-replacement");r=entries(n,"bitch1-full-scope-manifest.json")[0]
    old=r["path"];new="native/fictional-replacement.b64";shutil.copyfile(n/old,n/new)
    edit(n,"bitch1-full-scope-manifest.json",lambda v: records(v).__next__().__setitem__("path",new))
    run("equal-cardinality-replacement",n,0 if args.phase=="before" else 1)
    n=copy("duplicate-reference")
    edit(n,"bitch1-full-scope-manifest.json",lambda v: list(records(v))[0].update(list(records(v))[1]))
    run("duplicate-with-22-records",n,0 if args.phase=="before" else 1)
    if args.phase=="after":
        run("actual-22-reference-positive",args.evidence,0)
        for name in MANIFESTS:
            n=copy("absent-"+name);(n/name).unlink();run("required-manifest-"+name,n,1)
        for mutation in ["bytes","missing-sha","invalid-size","invalid-sha","wrapper","missing-artifact","malformed-json","unexpected-reference","empty"]:
            n=copy(mutation);target=n/"native/bitch1-full.stdout.b64"
            if mutation=="bytes": target.write_bytes(base64.b64encode(b"wrong fictional bytes")+b"\n")
            elif mutation=="missing-sha":edit(n,"bitch1-full-scope-manifest.json",lambda v:list(records(v))[0].pop("sha256"))
            elif mutation=="invalid-size":edit(n,"bitch1-full-scope-manifest.json",lambda v:list(records(v))[0].__setitem__("bytes","1"))
            elif mutation=="invalid-sha":edit(n,"bitch1-full-scope-manifest.json",lambda v:list(records(v))[0].__setitem__("sha256","x"*64))
            elif mutation=="wrapper":target.write_bytes(target.read_bytes()+b"\n")
            elif mutation=="missing-artifact":target.unlink()
            elif mutation=="malformed-json":(n/"bitch1-canonical-first.json").write_text("{")
            elif mutation=="unexpected-reference":(n/"extra.json").write_text(json.dumps(entries(n,"bitch1-full-scope-manifest.json")[0]))
            else:
                for m in n.glob("*.json"):m.write_text("{}")
            run(mutation,n,1)
        external=args.fixtures/"fictional-external-owner";external.mkdir()
        sentinel=external/"sentinel.b64";sentinel.write_bytes((args.evidence/"native/bitch1-full.stdout.b64").read_bytes())
        identity=hashlib.sha256(sentinel.read_bytes()).hexdigest()
        n=copy("external-file");t=n/"native/bitch1-full.stdout.b64";t.unlink();t.symlink_to(sentinel)
        run("external-file-symlink",n,1,"resolves outside")
        shutil.copytree(args.evidence/"native",external/"native")
        n=copy("external-directory");shutil.rmtree(n/"native");(n/"native").symlink_to(external/"native",target_is_directory=True)
        run("external-directory-symlink",n,1,"resolves outside")
        n=copy("internal-file");t=n/"native/bitch1-full.stdout.b64";shutil.copyfile(t,n/"owned.b64");t.unlink();t.symlink_to(n/"owned.b64")
        run("internal-file-symlink-positive",n,0)
        n=copy("internal-directory");(n/"native").rename(n/"owned-native");(n/"native").symlink_to(n/"owned-native",target_is_directory=True)
        run("internal-directory-symlink-positive",n,0)
        alias=args.fixtures/"root-alias";alias.symlink_to(n,target_is_directory=True);run("root-alias-positive",alias,0)
        n=copy("lexical-dotdot");edit(n,"bitch1-full-scope-manifest.json",lambda v: list(records(v))[0].__setitem__("path","native/../owned.b64"))
        shutil.copyfile(args.evidence/"native/bitch1-full.stdout.b64",n/"owned.b64")
        run("lexical-dotdot-negative",n,1,"leaves evidence root")
        assert hashlib.sha256(sentinel.read_bytes()).hexdigest()==identity
    print(json.dumps({"phase":args.phase,"cases":cases,"cases_count":len(cases),"scope":"harmless independently owned complete transport fixtures; no board interpretation or TOCTOU claim"},sort_keys=True))

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--checker",required=True,type=Path);p.add_argument("--evidence",required=True,type=Path)
    p.add_argument("--fixtures",required=True,type=Path);p.add_argument("--phase",required=True,choices=["before","after"])
    main(p.parse_args())
