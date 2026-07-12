# locveil-contract-guard

Layer-1 contract enforcement for every Locveil repo — the coherence half of
`process/contracts.md` §4. One stdlib-only file, `--check` only, never mutates the tree.

**What it checks (local only):** the uniform `contracts/` layout (`<name>/` owned,
`pins/<name>/` consumed, README registry mentions every folder), STAMP.json core fields
and `tag == "<contract>-v<version>"`, PIN.json core fields, and sha256 of local pinned
copies against the PIN's `files` map. Legacy pins (no `files` map / no PIN.json yet)
degrade to warnings until their next re-pin.

**What it never checks:** semantics (per-repo conformance tests, §4 layer 2) and
anything cross-repo (pin==tag bytes is the re-pin flow's job).

**Consumption:** vendor `contract_guard.py` at a pinned `contract-guard-vN` tag, wire it
into the pre-commit hook and a path-gated CI job — the scope-guard model, verbatim. A
rule change here never moves a consumer until it re-pins.

Run: `python3 contract_guard.py --check [--root <repo>]`
