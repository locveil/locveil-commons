# locveil-repin — consumed-contract re-pin + staleness check

The org-wide promotion of locveil-voice's BUILD-24 `scripts/repin.py` engine (decided
HK-12, executed PROD-26). One stdlib file, `repin.py`; per-repo behavior lives entirely
in a repo-local **`.repin.toml`** — the tool carries no topology.

## What it does

- **`repin.py <family> [--tag TAG]`** — re-pin a consumed family: fetch the owner's
  committed artifacts at a `<family>-vN` tag (default: newest), copy verbatim into the
  configured dest(s), stamp a strict `PIN.json` (core fields + `files` sha256 map +
  conformance pointer + mirrored owner-STAMP keys). Multi-dest families update every
  copy in one run at the same tag so they can never diverge. Writing requires the owner
  sibling on disk; cross-repo dest writes are legal ONLY into `../locveil-commons`
  (co-owned ground — HK-12 ruling). `check_only` families (a pin stamped by another
  repo's re-pin flow, e.g. commons' catalog copy stamped by voice) refuse re-pinning.
- **`repin.py --check [--fail-on none|major|any] [--family NAME]`** — staleness report
  per the §5 severity ladder (`process/contracts.md`):
  - `none` — pre-commit warn stage: always exit 0;
  - `major` — ordinary CI: fail only on a MAJOR-version gap or a never-pinned family;
  - `any` — release gates / touch-the-family workflows: fail on any staleness.
  `default_fail_on` in the config applies when the flag is omitted.
- **Tag lookup is remote-first**: tokenless `git ls-remote --tags <owner_url>` (the org
  repos are public — recorded HK-12 assumption); on network failure it falls back to the
  on-disk sibling's tags with a WARN carrying fetch age (a stale clone under-reports).
  Never network-required-to-commit. Untagged families: re-pin pins at owner `main`
  (tag/version null); `--check` byte-drift-checks against the sibling, else warn-skips.
- **`[[tool]]` entries** are the vendored-tools manifest: the recorded `pinned_tag` of a
  vendored script (scope-guard, contract-guard, repin itself) is checked against the
  owner's newest family tag on the same ladder — the tag↔vendored-copy relationship
  stops living in prose.

The fix for staleness is always a **deliberate re-pin under a ledger task** — never an
auto-fetch, never `--no-verify`.

## Config shape

```toml
[repin]
pinned_by = "<repo> scripts/repin.py (<task>)"
default_fail_on = "major"

[[family]]
name = "catalog"                       # tag family: catalog-vN
owner_repo = "locveil-bridge"
owner_dir = "../locveil-bridge"        # sibling checkout (re-pin + offline fallback)
owner_url = "https://github.com/locveil/locveil-bridge.git"   # remote-first --check
files = ["contracts/catalog/catalog.golden.json", "contracts/catalog/STAMP.json"]
mirror = ["bridge_commit"]             # owner-STAMP keys copied into PIN.json
# check_only = true                    # pin stamped by another repo's re-pin flow
[[family.dest]]
path = "contracts/pins/catalog"
conformance = "eval/tests/test_contracts_pin.py"

[[tool]]
name = "scope-guard"
family = "scope"                       # tag family: scope-vN
owner_repo = "locveil-commons"
owner_dir = "../locveil-commons"
owner_url = "https://github.com/locveil/locveil-commons.git"
pinned_tag = "scope-v6"                # bump in the re-vendor ledger task
```

## Consumption

Versioned by tags **`repin-vN`** (owned surface: `contracts/repin/STAMP.json`).
Consumers vendor `repin.py` at a pinned tag (the scope-guard model — their `[[tool]]`
entry then watches its own staleness) and write their own `.repin.toml`. The config is
repo-owned and NOT part of the pinned artifact set. Wire-up per repo: a warn-only
pre-commit stage (`--check --fail-on none || true`), the ordinary-CI severity of the
repo's choice, and `--fail-on any` in release flows.

## Tests

```
cd packages/repin && uv run --with pytest pytest tests/ -q
```

Real throwaway git repos pin re-pin mechanics, the severity ladder, remote-first +
fallback + offline behavior, untagged drift, the commons-only dest rule, and the tools
manifest.
