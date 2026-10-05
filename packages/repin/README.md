# locveil-repin — consumed-contract re-pin + staleness check

The org-wide promotion of locveil-voice's BUILD-24 `scripts/repin.py` engine (decided
HK-12, executed PROD-26). One stdlib file, `repin.py`; per-repo behavior lives entirely
in a repo-local **`.repin.toml`** — the tool carries no topology.

## What it does

- **`repin.py <family> [--tag TAG]`** — re-pin a consumed family at the owner's
  `<family>-vX.Y.Z` tag (default: newest). **The pin file set is the owner's (v2,
  HK-13):** the `artifacts` the owner's `contracts/<family>/STAMP.json` enumerates AT THE
  TAG, plus the STAMP itself, copied flat (file names, not paths) into the configured
  dest(s) with a strict `PIN.json` (core fields + `files` sha256 map + conformance
  pointer + mirrored owner-STAMP keys). A config `files` list is only the FALLBACK for
  owner tags cut before the owner enumerated. Reserved names (`README.md`, `PIN.json` —
  the consumer's own files in a pin folder) and duplicate file names refuse to pin;
  files the owner dropped are removed from the pin; a `conformance` pointer must resolve
  to a file in the repo that holds the pin (omit it when no test exists yet).
  Multi-dest families update every copy in one run at the same tag. Writing requires the
  owner sibling on disk; cross-repo dest writes are legal ONLY into `../locveil-commons`
  (co-owned ground — HK-12 ruling). `check_only` families refuse re-pinning.
- **`repin.py tool <name> [--tag TAG]`** — re-vendor a shared tool: fetch the single
  artifact the owner's STAMP enumerates at the tag, write it to the tool's `path`, and
  record `pinned_tag` + `sha256` in that `[[tool]]` block (nothing else in the config is
  rewritten).
- **`repin.py --check [--fail-on none|major|minor|any] [--touched BASE] [--family NAME]`**
  — staleness report per the §5 severity ladder (`process/contracts.md`):
  - `none` — pre-commit warn stage: always exit 0;
  - `major` — ordinary CI: a MAJOR family gap or a never-pinned family;
  - `minor` — release / image-dispatch gates: a minor-or-major family gap (HK-13 q6);
  - `any` — everything, including patch gaps and vendored-tool gaps.
  Vendored-tool version gaps fail only under `any` (a commons tool tag never blocks a
  hotfix image); a locally EDITED vendored tool (sha256 mismatch) fails at every level
  but `none`. `--touched BASE` is touch-the-family, implemented once here: a family
  whose pin folder or conformance test changed since BASE fails on ANY staleness. A
  cross-repo dest whose sibling repo is not on disk (CI) is skipped, never counted
  never-pinned. `default_fail_on` in the config applies when the flag is omitted.
- **Tag lookup is remote-first**: tokenless `git ls-remote --tags <owner_url>` (the org
  repos are public — recorded HK-12 assumption); on network failure it falls back to the
  on-disk sibling's tags with a WARN carrying fetch age (a stale clone under-reports).
  Never network-required-to-commit. Untagged families: re-pin pins at owner `main`
  (tag/version null); `--check` byte-drift-checks against the sibling, else warn-skips.

The fix for staleness is always a **deliberate re-pin under a ledger task** — never an
auto-fetch, never `--no-verify`.

## Config shape

```toml
[repin]
pinned_by = "<repo> scripts/repin.py (<task>)"
default_fail_on = "major"

[[family]]
name = "catalog"                       # tag family: catalog-vX.Y.Z
owner_repo = "locveil-bridge"
owner_dir = "../locveil-bridge"        # sibling checkout (re-pin + offline fallback)
owner_url = "https://github.com/locveil/locveil-bridge.git"   # remote-first --check
# NO `files`: the owner's STAMP enumerates the set. (Fallback only, for an owner tag
# that predates enumeration: files = ["contracts/x/a.json", "contracts/x/STAMP.json"])
# stamp = "contracts/catalog/STAMP.json"   # default: contracts/<family>/STAMP.json
mirror = ["bridge_commit"]             # owner-STAMP keys copied into PIN.json
# check_only = true                    # pin stamped by another repo's re-pin flow
[[family.dest]]
path = "contracts/pins/catalog"
conformance = "backend/tests/test_catalog_pin.py"   # resolves in the dest's repo

[[tool]]
name = "scope-guard"
family = "scope"                       # tag family: scope-vX.Y.Z
owner_repo = "locveil-commons"
owner_dir = "../locveil-commons"
owner_url = "https://github.com/locveil/locveil-commons.git"
path = "scripts/scope_guard.py"        # where the vendored copy lives
pinned_tag = "scope-v7.3.0"            # both lines written by `repin.py tool scope-guard`
sha256 = "<hex>"
```

## Consumption

Versioned by tags **`repin-vX.Y.Z`** (owned surface: `contracts/repin/STAMP.json`).
Consumers vendor `repin.py` at a pinned tag (`repin.py tool repin` — their `[[tool]]`
entry then watches its own staleness and bytes) and write their own `.repin.toml`. The
config is repo-owned and NOT part of the pinned artifact set. Wire-up per repo: a
warn-only pre-commit stage (`--check --fail-on none || true`); ordinary CI on every push
at `--fail-on major --touched <push base>`; `--fail-on minor` in release / image-dispatch
flows.

## Tests

```
cd packages/repin && uv run --with pytest pytest tests/ -q
```

Real throwaway git repos pin re-pin mechanics, the severity ladder, remote-first +
fallback + offline behavior, untagged drift, the commons-only dest rule, the tools
manifest, and the v2 behaviors (STAMP-derived pin set, reserved names, stale-file cleanup,
absent-dest skip, three levels, touch-the-family, tool re-vendor + hash).
