# scope — owned contract surface (cross-reference)

The vendored-tool contract for scope-guard, the ledger/journal discipline checker
(HK-1/PROD-13; convention: `../../process/ledger-discipline.md`). The artifact stays
runnable at **`../../packages/scope-guard/scope_guard.py`** (stays-in-home rule, §2).

- **Pinned set**: exactly `scope_guard.py`. Each consumer's `.scope-guard.toml` is
  repo-owned config and never travels.
- **Blocks ride the same tag** (HK-2 single-pin): the pinned CLAUDE.md block sources in
  `../../process/claude-blocks/` version with scope tags — a block-only release moves the
  tag while the script bytes stay identical.
- **Consumption**: vendor at a `scope-vX.Y.Z` tag (`repin.py tool scope-guard`); the
  repo's `.repin.toml` `[[tool]]` manifest records tag, path and sha256 (HK-12/HK-13).
  Re-pin blocks by copying the block text between the markers and updating its sha256
  in `.scope-guard.toml` (`scope_guard.py --hash-blocks`).
- **Version authority**: `STAMP.json` + tag (first stamped at v7; v1–v6 predate the stamp
  and are frozen history; three-part tags from v7.3.0 on — HK-13).
