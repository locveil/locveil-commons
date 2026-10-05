# contract-guard — owned contract surface (cross-reference)

The vendored-tool contract for contract-guard, the layer-1 contract-coherence checker
(HK-5/PROD-16; convention: `../../process/contracts.md` §4). The artifact stays runnable
at **`../../packages/contract-guard/contract_guard.py`** (stays-in-home rule, §2).

- **Pinned set**: exactly `contract_guard.py`. The optional `.contract-guard.toml`
  (vendorable_roots / non_contract / contract_names) is repo-owned and never travels.
- **Consumption**: vendor at a `contract-guard-vX.Y.Z` tag (`repin.py tool contract-guard`);
  the repo's `.repin.toml` `[[tool]]` manifest records tag, path and sha256 (HK-12/HK-13).
  Hooks pass `--relax-tags`; CI runs strict, on every push.
- **Version authority**: `STAMP.json` + tag (first stamped at v3; v1/v2 predate the stamp
  and are frozen history; three-part tags from v4.0.0 on — HK-13).
- **Owner guard**: `packages/contract-guard/tests/` (behavior suite over throwaway repos).
