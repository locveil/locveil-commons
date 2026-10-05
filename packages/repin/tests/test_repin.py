"""Behavior suite for repin (HK-12/PROD-26; v2 HK-13/PROD-28; severity: contracts.md §5).

Real throwaway git repos pin the semantics: re-pin writes + PIN.json shape, the
severity ladder (--fail-on none/major/any), remote-first tag lookup with the
stale-clone fallback, untagged-family drift, the commons-only dest rule, check_only
families, and the vendored-tools manifest. v2 adds: the pin set derived from the owner
STAMP's `artifacts` (config `files` as fallback), reserved names, stale-file cleanup,
conformance pointers that resolve, the absent cross-repo dest skip, three-level
classification with --fail-on minor, touch-the-family, and tool path+sha256 + re-vendor.
"""

import json
import subprocess
from pathlib import Path

import pytest

import repin as repin_mod
from repin import load_config, main


def git(repo: Path, *args: str) -> None:
    subprocess.run(["git", "-C", str(repo), *args], check=True, capture_output=True)


def make_owner(tmp: Path, name: str = "owner", tag: str | None = "cat-v1.0") -> Path:
    o = tmp / name
    (o / "contracts/cat").mkdir(parents=True)
    (o / "contracts/cat/artifact.json").write_text('{"payload": 1}\n')
    (o / "contracts/cat/STAMP.json").write_text(
        '{"contract": "cat", "version": "1.0", "extra": "mirrored-value"}\n')
    git(o, "init", "-q", "-b", "main")
    git(o, "config", "user.email", "t@t")
    git(o, "config", "user.name", "t")
    git(o, "add", "-A")
    git(o, "commit", "-q", "-m", "init")
    if tag:
        git(o, "tag", tag)
    return o


def bump_owner(o: Path, tag: str) -> None:
    (o / "contracts/cat/artifact.json").write_text(f'{{"payload": "{tag}"}}\n')
    git(o, "add", "-A")
    git(o, "commit", "-q", "-m", tag)
    git(o, "tag", tag)


CONFIG = """\
[repin]
pinned_by = "test-suite"
default_fail_on = "any"

[[family]]
name = "cat"
owner_repo = "owner"
owner_dir = "../owner"
{owner_url}
files = ["contracts/cat/artifact.json", "contracts/cat/STAMP.json"]
mirror = ["extra"]
{check_only}
[[family.dest]]
path = "contracts/pins/cat"
conformance = "tests/test_cat.py"
"""


def make_consumer(tmp: Path, owner_url: str = "", check_only: bool = False) -> Path:
    c = tmp / "consumer"
    c.mkdir(exist_ok=True)
    cfg = CONFIG.format(owner_url=f'owner_url = "{owner_url}"' if owner_url else "",
                        check_only="check_only = true" if check_only else "")
    (c / ".repin.toml").write_text(cfg)
    (c / "tests").mkdir(exist_ok=True)
    (c / "tests/test_cat.py").write_text("def test_cat():\n    pass\n")
    return c


def run(consumer: Path, *args: str) -> int:
    return main([*args, "--config", str(consumer / ".repin.toml")])


# --- re-pin mechanics ---


def test_repin_writes_pin_and_stamps(tmp_path):
    owner = make_owner(tmp_path)
    consumer = make_consumer(tmp_path)
    assert run(consumer, "cat") == 0
    dest = consumer / "contracts/pins/cat"
    assert (dest / "artifact.json").read_bytes() == (owner / "contracts/cat/artifact.json").read_bytes()
    pin = json.loads((dest / "PIN.json").read_text())
    assert pin["contract"] == "cat" and pin["tag"] == "cat-v1.0" and pin["version"] == "1.0"
    assert pin["extra"] == "mirrored-value"          # mirrored owner-STAMP key
    assert pin["pinned_by"] == "test-suite"
    assert pin["conformance"] == "tests/test_cat.py"
    assert set(pin["files"]) == {"artifact.json", "STAMP.json"}


def test_repin_at_explicit_tag(tmp_path):
    owner = make_owner(tmp_path)
    bump_owner(owner, "cat-v1.1")
    consumer = make_consumer(tmp_path)
    assert run(consumer, "cat", "--tag", "cat-v1.0") == 0
    pin = json.loads((consumer / "contracts/pins/cat/PIN.json").read_text())
    assert pin["tag"] == "cat-v1.0"


def test_check_only_family_refuses_repin(tmp_path):
    make_owner(tmp_path)
    consumer = make_consumer(tmp_path, check_only=True)
    assert run(consumer, "cat") == 2


def test_unknown_family_is_an_error(tmp_path):
    make_owner(tmp_path)
    consumer = make_consumer(tmp_path)
    assert run(consumer, "dog") == 2


# --- the severity ladder ---


def test_check_ok_when_current(tmp_path):
    make_owner(tmp_path)
    consumer = make_consumer(tmp_path)
    run(consumer, "cat")
    assert run(consumer, "--check") == 0


def test_minor_gap_fails_any_but_not_major(tmp_path):
    owner = make_owner(tmp_path)
    consumer = make_consumer(tmp_path)
    run(consumer, "cat")
    bump_owner(owner, "cat-v1.1")
    assert run(consumer, "--check", "--fail-on", "any") == 1
    assert run(consumer, "--check", "--fail-on", "major") == 0
    assert run(consumer, "--check", "--fail-on", "none") == 0


def test_major_gap_fails_major(tmp_path):
    owner = make_owner(tmp_path)
    consumer = make_consumer(tmp_path)
    run(consumer, "cat")
    bump_owner(owner, "cat-v2.0")
    assert run(consumer, "--check", "--fail-on", "major") == 1
    assert run(consumer, "--check", "--fail-on", "none") == 0


def test_never_pinned_counts_as_major(tmp_path):
    make_owner(tmp_path)
    consumer = make_consumer(tmp_path)
    assert run(consumer, "--check", "--fail-on", "major") == 1


def test_default_fail_on_comes_from_config(tmp_path):
    owner = make_owner(tmp_path)
    consumer = make_consumer(tmp_path)
    run(consumer, "cat")
    bump_owner(owner, "cat-v1.1")
    assert run(consumer, "--check") == 1  # config says default_fail_on = "any"


# --- tag lookup: remote-first, fallback, offline ---


def test_remote_first_via_file_url(tmp_path):
    owner = make_owner(tmp_path)
    consumer = make_consumer(tmp_path, owner_url=owner.as_uri())
    run(consumer, "cat")
    assert run(consumer, "--check") == 0


def test_unreachable_remote_falls_back_to_disk_with_warn(tmp_path, capsys):
    owner = make_owner(tmp_path)
    consumer = make_consumer(tmp_path, owner_url="file:///definitely/not/here")
    run(consumer, "cat")
    assert run(consumer, "--check") == 0
    assert "remote unreachable" in capsys.readouterr().out
    bump_owner(owner, "cat-v1.1")
    assert run(consumer, "--check", "--fail-on", "any") == 1


def test_no_source_at_all_is_warn_not_crash(tmp_path, capsys):
    make_owner(tmp_path)
    consumer = make_consumer(tmp_path)
    run(consumer, "cat")
    subprocess.run(["mv", str(tmp_path / "owner"), str(tmp_path / "gone")], check=True)
    assert run(consumer, "--check", "--fail-on", "none") == 0   # pre-commit: never blocks
    assert "no tag source" in capsys.readouterr().out
    assert run(consumer, "--check", "--fail-on", "any") == 1    # release: must see


# --- untagged families ---


def test_untagged_pin_at_main_and_drift(tmp_path):
    owner = make_owner(tmp_path, tag=None)
    consumer = make_consumer(tmp_path)
    assert run(consumer, "cat") == 0
    pin = json.loads((consumer / "contracts/pins/cat/PIN.json").read_text())
    assert pin["tag"] is None and pin["version"] is None
    assert run(consumer, "--check") == 0
    (owner / "contracts/cat/artifact.json").write_text('{"payload": 2}\n')
    git(owner, "add", "-A")
    git(owner, "commit", "-q", "-m", "drift")
    assert run(consumer, "--check", "--fail-on", "any") == 1
    assert run(consumer, "--check", "--fail-on", "major") == 0  # drift is not a major gap


# --- config rules ---


def test_cross_repo_dest_only_into_commons(tmp_path):
    make_owner(tmp_path)
    consumer = make_consumer(tmp_path)
    (tmp_path / "locveil-commons/contracts/pins").mkdir(parents=True)
    cfg = (consumer / ".repin.toml").read_text().replace(
        'path = "contracts/pins/cat"',
        'path = "../locveil-commons/contracts/pins/cat"')
    (consumer / ".repin.toml").write_text(cfg)
    load_config(consumer / ".repin.toml")  # commons dest: legal
    (consumer / ".repin.toml").write_text(cfg.replace("locveil-commons", "owner"))
    with pytest.raises(SystemExit, match="ONLY into"):
        load_config(consumer / ".repin.toml")


# --- vendored-tools manifest ---


TOOL = """
[[tool]]
name = "some-guard"
family = "cat"
owner_repo = "owner"
owner_dir = "../owner"
pinned_tag = "cat-v1.0"
"""


def test_tool_manifest_current_then_stale(tmp_path):
    owner = make_owner(tmp_path)
    consumer = make_consumer(tmp_path)
    run(consumer, "cat")
    (consumer / ".repin.toml").write_text((consumer / ".repin.toml").read_text() + TOOL)
    assert run(consumer, "--check") == 0
    bump_owner(owner, "cat-v2.0")
    run(consumer, "cat")  # family itself re-pinned current
    # HK-13 q6: a vendored-tool version gap warns at every level but `any`
    assert run(consumer, "--check", "--fail-on", "major") == 0
    assert run(consumer, "--check", "--fail-on", "minor") == 0
    assert run(consumer, "--check", "--fail-on", "any") == 1
    assert run(consumer, "--check", "--fail-on", "none") == 0


# --- v2 (HK-13): the owner's STAMP is the single source of the pin set ---


def make_enumerating_owner(tmp: Path, artifacts: list[str], tag: str = "cat-v1.0.0",
                           extra_files: dict[str, str] | None = None) -> Path:
    o = tmp / "owner"
    (o / "contracts/cat").mkdir(parents=True)
    for rel, body in (extra_files or {}).items():
        (o / rel).parent.mkdir(parents=True, exist_ok=True)
        (o / rel).write_text(body)
    (o / "contracts/cat/STAMP.json").write_text(json.dumps(
        {"contract": "cat", "version": tag.split("-v")[1], "tag": tag,
         "artifacts": artifacts, "extra": "mirrored-value"}) + "\n")
    git(o, "init", "-q", "-b", "main")
    git(o, "config", "user.email", "t@t")
    git(o, "config", "user.name", "t")
    git(o, "add", "-A")
    git(o, "commit", "-q", "-m", "init")
    git(o, "tag", tag)
    return o


def recut(o: Path, tag: str, artifacts: list[str], files: dict[str, str]) -> None:
    for rel, body in files.items():
        (o / rel).parent.mkdir(parents=True, exist_ok=True)
        (o / rel).write_text(body)
    (o / "contracts/cat/STAMP.json").write_text(json.dumps(
        {"contract": "cat", "version": tag.split("-v")[1], "tag": tag,
         "artifacts": artifacts}) + "\n")
    git(o, "add", "-A")
    git(o, "commit", "-q", "-m", tag)
    git(o, "tag", tag)


def no_files(consumer: Path) -> None:
    cfg = consumer / ".repin.toml"
    cfg.write_text(cfg.read_text().replace(
        'files = ["contracts/cat/artifact.json", "contracts/cat/STAMP.json"]\n', ""))


def test_pin_set_comes_from_owner_stamp_not_config(tmp_path):
    make_enumerating_owner(tmp_path, ["contracts/cat/a.json", "docs/guide.md"],
                           extra_files={"contracts/cat/a.json": "{}", "docs/guide.md": "g",
                                        "contracts/cat/artifact.json": "ignored"})
    consumer = make_consumer(tmp_path)  # config still lists the old `files`: ignored
    assert run(consumer, "cat") == 0
    pin = json.loads((consumer / "contracts/pins/cat/PIN.json").read_text())
    assert set(pin["files"]) == {"a.json", "guide.md", "STAMP.json"}
    assert pin["version"] == "1.0.0" and pin["extra"] == "mirrored-value"
    no_files(consumer)  # and the config needs no `files` at all
    assert run(consumer, "cat") == 0 and run(consumer, "--check") == 0


def test_empty_artifacts_pins_the_stamp_alone(tmp_path):
    make_enumerating_owner(tmp_path, [])
    consumer = make_consumer(tmp_path)
    no_files(consumer)
    assert run(consumer, "cat") == 0
    pin = json.loads((consumer / "contracts/pins/cat/PIN.json").read_text())
    assert set(pin["files"]) == {"STAMP.json"}


def test_no_artifacts_and_no_fallback_is_an_error(tmp_path):
    make_owner(tmp_path)  # legacy STAMP: enumerates nothing
    consumer = make_consumer(tmp_path)
    no_files(consumer)
    with pytest.raises(SystemExit, match="nothing defines the pin set"):
        run(consumer, "cat")


def test_reserved_and_duplicate_names_refuse_to_pin(tmp_path):
    make_enumerating_owner(tmp_path, ["contracts/cat/README.md"],
                           extra_files={"contracts/cat/README.md": "normative"})
    consumer = make_consumer(tmp_path)
    assert run(consumer, "cat") == 2
    assert not (consumer / "contracts/pins/cat/PIN.json").exists()


def test_repin_removes_files_the_owner_dropped_and_keeps_the_readme(tmp_path):
    owner = make_enumerating_owner(tmp_path, ["contracts/cat/a.json", "contracts/cat/b.json"],
                                   extra_files={"contracts/cat/a.json": "a",
                                                "contracts/cat/b.json": "b"})
    consumer = make_consumer(tmp_path)
    assert run(consumer, "cat") == 0
    dest = consumer / "contracts/pins/cat"
    (dest / "README.md").write_text("why we pin cat\n")
    recut(owner, "cat-v1.1.0", ["contracts/cat/a.json", "contracts/cat/guide.md"],
          {"contracts/cat/guide.md": "g"})
    assert run(consumer, "cat") == 0
    assert sorted(p.name for p in dest.iterdir()) == [
        "PIN.json", "README.md", "STAMP.json", "a.json", "guide.md"]


def test_conformance_pointer_must_resolve(tmp_path):
    make_enumerating_owner(tmp_path, ["contracts/cat/a.json"],
                           extra_files={"contracts/cat/a.json": "a"})
    consumer = make_consumer(tmp_path)
    (consumer / "tests/test_cat.py").unlink()
    assert run(consumer, "cat") == 2


def test_absent_cross_repo_dest_is_skipped_not_never_pinned(tmp_path):
    make_enumerating_owner(tmp_path, ["contracts/cat/a.json"],
                           extra_files={"contracts/cat/a.json": "a"})
    consumer = make_consumer(tmp_path)
    run(consumer, "cat")
    cfg = consumer / ".repin.toml"
    cfg.write_text(cfg.read_text() + '''[[family.dest]]
path = "../locveil-commons/contracts/pins/cat"
''')
    assert run(consumer, "--check", "--fail-on", "major") == 0  # sibling absent: skipped
    (tmp_path / "locveil-commons").mkdir()
    assert run(consumer, "--check", "--fail-on", "major") == 1  # present + unpinned


def test_three_levels_and_fail_on_minor(tmp_path):
    owner = make_enumerating_owner(tmp_path, ["contracts/cat/a.json"],
                                   extra_files={"contracts/cat/a.json": "a"})
    consumer = make_consumer(tmp_path)
    run(consumer, "cat")
    recut(owner, "cat-v1.0.1", ["contracts/cat/a.json"], {"contracts/cat/a.json": "a2"})
    assert run(consumer, "--check", "--fail-on", "minor") == 0   # patch gap: warn
    assert run(consumer, "--check", "--fail-on", "any") == 1
    recut(owner, "cat-v1.1.0", ["contracts/cat/a.json"], {"contracts/cat/a.json": "a3"})
    assert run(consumer, "--check", "--fail-on", "major") == 0   # minor gap
    assert run(consumer, "--check", "--fail-on", "minor") == 1   # release gate
    assert repin_mod._classify("cat", "cat-v1", "cat-v1.0.1") == "stale-patch"
    assert repin_mod._classify("cat", "cat-v1.9", "cat-v1.10.0") == "stale-minor"
    assert repin_mod._classify("cat", "cat-v1", "cat-v1.0.0") == "ok"


def test_touch_the_family_fails_regardless_of_severity(tmp_path):
    owner = make_enumerating_owner(tmp_path, ["contracts/cat/a.json"],
                                   extra_files={"contracts/cat/a.json": "a"})
    consumer = make_consumer(tmp_path)
    run(consumer, "cat")
    git(consumer, "init", "-q", "-b", "main")
    git(consumer, "config", "user.email", "t@t")
    git(consumer, "config", "user.name", "t")
    git(consumer, "add", "-A")
    git(consumer, "commit", "-q", "-m", "pin")
    recut(owner, "cat-v1.0.1", ["contracts/cat/a.json"], {"contracts/cat/a.json": "a2"})
    (consumer / "unrelated.txt").write_text("x")
    git(consumer, "add", "-A")
    git(consumer, "commit", "-q", "-m", "unrelated")
    assert run(consumer, "--check", "--fail-on", "major", "--touched", "HEAD~1") == 0
    (consumer / "tests/test_cat.py").write_text("def test_cat():\n    assert True\n")
    git(consumer, "add", "-A")
    git(consumer, "commit", "-q", "-m", "touch the conformance test")
    assert run(consumer, "--check", "--fail-on", "major", "--touched", "HEAD~1") == 1
    assert run(consumer, "--check", "--fail-on", "major", "--touched", "no-such-ref") == 0


TOOL_V2 = """
[[tool]]
name = "some-guard"
family = "cat"
owner_repo = "owner"
owner_dir = "../owner"
pinned_tag = "cat-v0.0.0"
path = "scripts/tool.py"
"""


def test_tool_revendor_records_tag_and_hash_then_detects_local_edits(tmp_path):
    owner = make_enumerating_owner(tmp_path, ["packages/tool.py"],
                                   extra_files={"packages/tool.py": "print(1)\n"})
    consumer = make_consumer(tmp_path)
    run(consumer, "cat")  # (the family pin itself; the tool shares the family here)
    (consumer / "scripts").mkdir()
    cfg = consumer / ".repin.toml"
    cfg.write_text(cfg.read_text() + TOOL_V2)
    assert run(consumer, "tool", "some-guard") == 0
    assert (consumer / "scripts/tool.py").read_text() == "print(1)\n"
    text = cfg.read_text()
    assert 'pinned_tag = "cat-v1.0.0"' in text and "sha256 = " in text
    assert text.count("[[family]]") == 1  # nothing else rewritten
    assert run(consumer, "--check", "--fail-on", "any") == 0
    (consumer / "scripts/tool.py").write_text("print(2)  # local edit\n")
    assert run(consumer, "--check", "--fail-on", "major") == 1   # tool-drift
    assert run(consumer, "--check", "--fail-on", "none") == 0
    recut(owner, "cat-v1.1.0", ["packages/tool.py"], {"packages/tool.py": "print(3)\n"})
    assert run(consumer, "tool", "some-guard") == 0               # re-vendor again
    assert 'pinned_tag = "cat-v1.1.0"' in cfg.read_text()
    assert cfg.read_text().count("sha256 = ") == 1
