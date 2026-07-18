# contract-guard — owned contract surface (cross-reference)

The vendored-tool contract for contract-guard, the layer-1 contract-coherence checker
(HK-5/PROD-16; convention: `../../process/contracts.md` §4). The artifact stays runnable
at **`../../packages/contract-guard/contract_guard.py`** (stays-in-home rule, §2).

- **Pinned set**: exactly `contract_guard.py`. The optional `.contract-guard.toml`
  (vendorable_roots / non_contract / contract_names) is repo-owned and never travels.
- **Consumption**: vendor at a `contract-guard-vN` tag; record the tag in the repo's
  `.repin.toml` `[[tool]]` manifest (HK-12). Hooks pass `--relax-tags`; CI runs strict.
- **Version authority**: `STAMP.json` + tag (first stamped at `contract-guard-v3`;
  v1/v2 predate the stamp and are frozen history).
