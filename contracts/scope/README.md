# scope — owned contract surface (cross-reference)

The vendored-tool contract for scope-guard, the ledger/journal discipline checker
(HK-1/PROD-13; convention: `../../process/ledger-discipline.md`). The artifact stays
runnable at **`../../packages/scope-guard/scope_guard.py`** (stays-in-home rule, §2).

- **Pinned set**: exactly `scope_guard.py`. Each consumer's `.scope-guard.toml` is
  repo-owned config and never travels.
- **Consumption**: vendor at a `scope-vN` tag; record the tag in the repo's
  `.repin.toml` `[[tool]]` manifest (HK-12) so staleness is machine-checked.
- **Version authority**: `STAMP.json` + tag (first stamped at `scope-v7`; v1–v6 predate
  the stamp and are frozen history).
