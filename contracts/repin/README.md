# repin — owned contract surface (cross-reference)

The vendored-tool contract for the org's consumed-contract re-pin + staleness engine
(HK-12/PROD-26). The artifact keeps its runnable home — **`../../packages/repin/repin.py`**
— per `../../process/contracts.md` §2 (stays-in-home rule; this folder holds the STAMP +
this pointer, the registry indexes it).

- **Pinned set** (STAMP `artifacts`): exactly `repin.py`. Each consumer's `.repin.toml`
  is repo-owned config — it declares that repo's families/dests/tools and never travels.
- **Consumption**: vendor `repin.py` at a `repin-vX.Y.Z` tag (`repin.py tool repin`); the
  repo's `[[tool]]` entry records tag, path and sha256 (self-watching staleness + bytes).
  Wire the §5 ladder: pre-commit `--check --fail-on none || true`; CI on every push at
  `--fail-on major --touched <push base>`; `--fail-on minor` in release / dispatch flows.
- **Version authority**: `STAMP.json` + tag (three-part from v2.0.0 — HK-13). Semantics:
  the module docstring + behavior suite `../../packages/repin/tests/`; severity policy:
  `process/contracts.md` §5.

Consumers (PROD-26 delegations): locveil-voice (BUILD-43, before ARCH-58), locveil-bridge
and locveil-satellite (their sweep tasks; IDs on the board when written back).
