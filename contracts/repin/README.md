# repin — owned contract surface (cross-reference)

The vendored-tool contract for the org's consumed-contract re-pin + staleness engine
(HK-12/PROD-26). The artifact keeps its runnable home — **`../../packages/repin/repin.py`**
— per `../../process/contracts.md` §2 (stays-in-home rule; this folder holds the STAMP +
this pointer, the registry indexes it).

- **Pinned set** (STAMP `artifacts`): exactly `repin.py`. Each consumer's `.repin.toml`
  is repo-owned config — it declares that repo's families/dests/tools and never travels.
- **Consumption**: vendor `repin.py` at a `repin-vN` tag (the scope-guard model), add a
  `[[tool]]` entry for it in the repo's own `.repin.toml` (self-watching staleness), wire
  the §5 severity ladder: pre-commit `--check --fail-on none || true`, ordinary CI at the
  repo's chosen severity, `--fail-on any` in release flows.
- **Version authority**: `STAMP.json` + tag `repin-v1`. Semantics: the module docstring +
  behavior suite `../../packages/repin/tests/`; severity policy: `process/contracts.md` §5.

Consumers (PROD-26 delegations): locveil-voice (BUILD-43, before ARCH-58), locveil-bridge
and locveil-satellite (their sweep tasks; IDs on the board when written back).
