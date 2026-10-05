"""Behavior suite for contract-guard v4 (HK-13/PROD-28, IMPL-10).

Real throwaway git repos pin the v4 rule set: declared artifacts (legacy WARN vs
dated FAIL, empty-needs-guard), three-part version form, reserved/duplicate names,
STAMP-DRIFT, pin completeness, UNLISTED-FILE as a failure, pointer resolution and the
registry-version rule. The v3 rules they build on (TAG-MISSING, CONTENT-DRIFT) get one
regression each.
"""

import hashlib
import json
import subprocess
from pathlib import Path

from contract_guard import run_check

NEW = "2026-10-05"   # HK-13 landing date: rules FAIL from here
OLD = "2026-07-18"   # legacy: the new rules only WARN


def git(repo: Path, *args: str) -> None:
    subprocess.run(["git", "-C", str(repo), *args], check=True, capture_output=True)


def stamp(name: str, version: str, date: str = NEW, **extra) -> dict:
    return {"contract": name, "version": version, "tag": f"{name}-v{version}",
            "date": date, "owner_repo": "r", **extra}


def make_repo(tmp: Path, owned: dict[str, dict], files: dict[str, str] | None = None,
              registry: str | None = None, tag: bool = True) -> Path:
    """owned: name -> STAMP dict; files: extra repo-root-relative files."""
    r = tmp / "r"
    (r / "contracts").mkdir(parents=True)
    for rel, body in (files or {}).items():
        (r / rel).parent.mkdir(parents=True, exist_ok=True)
        (r / rel).write_text(body)
    for name, st in owned.items():
        d = r / "contracts" / name
        d.mkdir(parents=True, exist_ok=True)
        (d / "README.md").write_text(f"# {name}\n")
        (d / "STAMP.json").write_text(json.dumps(st, indent=2) + "\n")
    (r / "contracts/README.md").write_text(
        registry if registry is not None else "registry: " + " ".join(owned) + "\n")
    git(r, "init", "-q", "-b", "main")
    git(r, "config", "user.email", "t@t")
    git(r, "config", "user.name", "t")
    git(r, "add", "-A")
    git(r, "commit", "-q", "-m", "init")
    if tag:
        for st in owned.values():
            git(r, "tag", st["tag"])
    return r


def codes(rep, kind: str = "failures") -> list[str]:
    return [m.split(":", 1)[0] for m in getattr(rep, kind)]


def add_pin(r: Path, name: str, files: dict[str, str], pin_extra: dict | None = None,
            owner_stamp: dict | None = None, pin_date: str = NEW) -> Path:
    d = r / "contracts/pins" / name
    d.mkdir(parents=True)
    listed = {}
    if owner_stamp is not None:
        files = {**files, "STAMP.json": json.dumps(owner_stamp)}
    for fname, body in files.items():
        (d / fname).write_text(body)
        listed[fname] = hashlib.sha256(body.encode()).hexdigest()
    pin = {"contract": name, "version": "1.0.0", "tag": f"{name}-v1.0.0",
           "owner_repo": "o", "owner_commit": "abc", "pinned_by": "t",
           "pin_date": pin_date, "files": listed, "conformance": "tests/test_pin.py",
           **(pin_extra or {})}
    (d / "PIN.json").write_text(json.dumps(pin))
    reg = r / "contracts/README.md"
    reg.write_text(reg.read_text() + f" {name}\n")
    return d


# ---------------------------------------------------------------- owned: declaration


def test_clean_three_part_stamp_passes(tmp_path):
    r = make_repo(tmp_path, {"cat": stamp("cat", "1.0.0", artifacts=["src/a.json"])},
                  files={"src/a.json": "{}\n"})
    rep = run_check(r)
    assert rep.failures == [] and rep.warnings == []


def test_missing_artifacts_warns_for_legacy_and_fails_when_dated(tmp_path):
    r = make_repo(tmp_path / "old", {"cat": stamp("cat", "1.0", date=OLD)})
    rep = run_check(r)
    assert rep.failures == [] and "ARTIFACTS-UNDECLARED" in codes(rep, "warnings")
    r = make_repo(tmp_path / "new", {"cat": stamp("cat", "1.0.0")})
    assert "ARTIFACTS-UNDECLARED" in codes(run_check(r))


def test_empty_artifacts_needs_a_resolving_guard(tmp_path):
    r = make_repo(tmp_path / "a", {"cat": stamp("cat", "1.0.0", artifacts=[])})
    assert "ARTIFACTS-EMPTY-NO-GUARD" in codes(run_check(r))
    r = make_repo(tmp_path / "b",
                  {"cat": stamp("cat", "1.0.0", artifacts=[], guard="tests/t.py::test_x")},
                  files={"tests/t.py": "pass\n"})
    assert run_check(r).failures == []
    r = make_repo(tmp_path / "c",
                  {"cat": stamp("cat", "1.0.0", artifacts=[], guard="tests/gone.py")})
    assert {"ARTIFACTS-EMPTY-NO-GUARD", "POINTER-UNRESOLVED"} <= set(codes(run_check(r)))


def test_version_form_is_three_part_from_hk13(tmp_path):
    r = make_repo(tmp_path / "new", {"cat": stamp("cat", "1.1", artifacts=["a.txt"])},
                  files={"a.txt": "x"})
    # "a.txt" is a bare name too (ARTIFACTS-PATH) — VERSION-FORM is what we pin here
    assert "VERSION-FORM" in codes(run_check(r))
    r = make_repo(tmp_path / "old",
                  {"cat": stamp("cat", "1.1", date=OLD, artifacts=["src/a.txt"])},
                  files={"src/a.txt": "x"})
    assert run_check(r).failures == []


def test_reserved_and_duplicate_names_fail_at_the_owner(tmp_path):
    r = make_repo(tmp_path, {"cat": stamp("cat", "1.0.0", artifacts=[
        "contracts/cat/README.md", "a/guide.md", "b/guide.md"])},
        files={"a/guide.md": "a", "b/guide.md": "b"})
    got = codes(run_check(r))
    assert "RESERVED-NAME" in got and "DUPLICATE-NAME" in got


def test_code_constant_pointer_must_resolve(tmp_path):
    r = make_repo(tmp_path, {"cat": stamp("cat", "1.0.0", artifacts=["src/a.json"],
                                          code_constant="src/gone.py::VERSION")},
                  files={"src/a.json": "{}"})
    assert codes(run_check(r)) == ["POINTER-UNRESOLVED"]


# ---------------------------------------------------------------- owned: drift


def test_stamp_drift_fails_and_pre_stamp_tag_warns(tmp_path):
    r = make_repo(tmp_path / "drift", {"cat": stamp("cat", "1.0.0", artifacts=["src/a.json"])},
                  files={"src/a.json": "{}"})
    sp = r / "contracts/cat/STAMP.json"
    st = json.loads(sp.read_text())
    st["note"] = "edited after the tag"
    sp.write_text(json.dumps(st))
    assert "STAMP-DRIFT" in codes(run_check(r))

    r = make_repo(tmp_path / "pre", {}, files={"src/a.json": "{}"})
    git(r, "tag", "cat-v1.0.0")  # the tag predates the STAMP
    d = r / "contracts/cat"
    d.mkdir()
    (d / "README.md").write_text("# cat\n")
    (d / "STAMP.json").write_text(json.dumps(stamp("cat", "1.0.0", artifacts=["src/a.json"])))
    (r / "contracts/README.md").write_text("cat\n")
    rep = run_check(r)
    assert rep.failures == [] and "STAMP-NOT-IN-TAG" in codes(rep, "warnings")


def test_content_drift_and_tag_missing_still_hold(tmp_path):
    r = make_repo(tmp_path / "cd", {"cat": stamp("cat", "1.0.0", artifacts=["src/a.json"])},
                  files={"src/a.json": "{}"})
    (r / "src/a.json").write_text('{"moved": true}')
    assert "CONTENT-DRIFT" in codes(run_check(r))
    r = make_repo(tmp_path / "tm", {"cat": stamp("cat", "1.0.0", artifacts=["src/a.json"])},
                  files={"src/a.json": "{}"}, tag=False)
    assert "TAG-MISSING" in codes(run_check(r))
    relaxed = run_check(r, relax=True)
    assert relaxed.failures == [] and "TAG-MISSING" in codes(relaxed, "warnings")


# ---------------------------------------------------------------- pins


def test_complete_pin_passes(tmp_path):
    r = make_repo(tmp_path, {}, files={"tests/test_pin.py": "pass\n"})
    add_pin(r, "dog", {"a.json": "{}"},
            owner_stamp=stamp("dog", "1.0.0", artifacts=["contracts/dog/a.json"]))
    rep = run_check(r)
    assert rep.failures == [] and rep.warnings == []


def test_incomplete_pin_fails_new_and_warns_legacy(tmp_path):
    owner = stamp("dog", "1.0.0", artifacts=["contracts/dog/a.json", "contracts/dog/guide.md"])
    r = make_repo(tmp_path / "new", {}, files={"tests/test_pin.py": "pass\n"})
    add_pin(r, "dog", {"a.json": "{}"}, owner_stamp=owner)
    assert codes(run_check(r)) == ["PIN-INCOMPLETE"]
    r = make_repo(tmp_path / "old", {}, files={"tests/test_pin.py": "pass\n"})
    add_pin(r, "dog", {"a.json": "{}"}, owner_stamp=owner, pin_date=OLD)
    rep = run_check(r)
    assert rep.failures == [] and "PIN-INCOMPLETE" in codes(rep, "warnings")


def test_owner_stamp_without_artifacts_is_unverifiable_not_failed(tmp_path):
    r = make_repo(tmp_path, {}, files={"tests/test_pin.py": "pass\n"})
    add_pin(r, "dog", {"a.json": "{}"}, owner_stamp=stamp("dog", "1.0.0", date=OLD))
    rep = run_check(r)
    assert rep.failures == [] and "PIN-COMPLETENESS-UNVERIFIABLE" in codes(rep, "warnings")


def test_unlisted_file_fails_but_consumer_readme_is_reserved(tmp_path):
    r = make_repo(tmp_path, {}, files={"tests/test_pin.py": "pass\n"})
    d = add_pin(r, "dog", {"a.json": "{}"},
                owner_stamp=stamp("dog", "1.0.0", artifacts=["contracts/dog/a.json"]))
    (d / "README.md").write_text("why we pin dog\n")
    assert run_check(r).failures == []
    (d / "stray.txt").write_text("x")
    assert codes(run_check(r)) == ["UNLISTED-FILE"]


def test_pin_conformance_pointer(tmp_path):
    owner = stamp("dog", "1.0.0", artifacts=["contracts/dog/a.json"])
    r = make_repo(tmp_path / "bad", {})
    add_pin(r, "dog", {"a.json": "{}"}, owner_stamp=owner)  # tests/test_pin.py absent
    assert codes(run_check(r)) == ["POINTER-UNRESOLVED"]
    r = make_repo(tmp_path / "none", {})
    add_pin(r, "dog", {"a.json": "{}"}, owner_stamp=owner, pin_extra={"conformance": None})
    rep = run_check(r)
    assert rep.failures == [] and "PIN-NO-CONFORMANCE" in codes(rep, "warnings")
    r = make_repo(tmp_path / "legacy", {})
    add_pin(r, "dog", {"a.json": "{}"}, owner_stamp=owner, pin_date=OLD,
            pin_extra={"conformance": "prose about a future test"})
    rep = run_check(r)
    assert rep.failures == [] and "POINTER-UNRESOLVED" in codes(rep, "warnings")


# ---------------------------------------------------------------- registry + .repin.toml


def test_registry_version_strings_must_be_current(tmp_path):
    st = stamp("cat", "1.2.0", artifacts=["src/a.json"])
    ok = "cat at `cat-v1.2.0`; unrelated tomcat-v9 and cat-vN.M stay out of it\n"
    r = make_repo(tmp_path / "ok", {"cat": st}, files={"src/a.json": "{}"}, registry=ok)
    assert run_check(r).failures == []
    r = make_repo(tmp_path / "bad", {"cat": st}, files={"src/a.json": "{}"},
                  registry="cat (first: `cat-v1.0`), now cat-v1.2.0\n")
    assert codes(run_check(r)) == ["REGISTRY-VERSION"]


def test_repin_config_pointers_and_tool_registry(tmp_path):
    cfg = """\
[[family]]
name = "dog"
owner_repo = "o"
[[family.dest]]
path = "contracts/pins/dog"
conformance = "tests/gone.py"
[[family.dest]]
path = "../other/contracts/pins/dog"
conformance = "tests/elsewhere.py"

[[tool]]
name = "guard"
family = "contract-guard"
pinned_tag = "contract-guard-v4.0.0"
path = "scripts/contract_guard.py"
"""
    r = make_repo(tmp_path, {}, files={".repin.toml": cfg},
                  registry="vendored guard at contract-guard-v3\n")
    got = codes(run_check(r))
    assert got.count("POINTER-UNRESOLVED") == 2  # in-repo conformance + tool path
    assert "REGISTRY-VERSION" in got
