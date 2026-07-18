"""Behavior suite for repin (HK-12/PROD-26; severity: process/contracts.md §5).

Real throwaway git repos pin the semantics: re-pin writes + PIN.json shape, the
severity ladder (--fail-on none/major/any), remote-first tag lookup with the
stale-clone fallback, untagged-family drift, the commons-only dest rule, check_only
families, and the vendored-tools manifest.
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
    assert run(consumer, "--check", "--fail-on", "major") == 1  # the tool is major-stale
    assert run(consumer, "--check", "--fail-on", "none") == 0
