# locveil-contract-guard

Layer-1 contract enforcement for every Locveil repo — the coherence half of
`process/contracts.md` §4. One stdlib-only file, `--check` only, never mutates the tree.

**What it checks (local only):** the uniform `contracts/` layout (`<name>/` owned,
`pins/<name>/` consumed, README registry mentions every folder), STAMP.json core fields
and `tag == "<contract>-v<version>"`, PIN.json core fields, and sha256 of local pinned
copies against the PIN's `files` map. Legacy pins (no `files` map / no PIN.json yet)
degrade to warnings until their next re-pin. Since v1.1 (`contract-guard-v2`, PROD-22 —
a bridge-caught false green): an owned STAMP naming a git tag that doesn't exist FAILS
(`TAG-MISSING`) — the tag is created in the same change as the STAMP bump; remote-push
verification stays out of scope.

**v4 (`contract-guard-v4.0.0`, HK-13/PROD-28)** — one declaration, checked from both ends:
every STAMP declares `artifacts` (what consumers pin AND what the drift rule locks; empty
only with a resolving `guard` pointer; STAMPs dated before 2026-10-05 warn as legacy);
cuts dated from 2026-10-05 are three-part (`X.Y.Z`); an owner never enumerates a reserved
file name (`README.md`, `PIN.json`, `STAMP.json`) or two files sharing a name — pins are
flat; the STAMP itself must equal its bytes at its tag (`STAMP-DRIFT`); a pin must cover
the `artifacts` of the owner STAMP it carries (`PIN-INCOMPLETE`; pins stamped before
2026-10-05 warn); an unlisted file in a strict pin fails; pointer fields resolve to files
(`guard`, `code_constant`, PIN / `.repin.toml` `conformance`, `[[tool]]` `path`); and any
`<family>-v<digits>` string in `contracts/README.md` must equal the family's current
STAMP / PIN / `[[tool]]` tag.

**What it never checks:** semantics (per-repo conformance tests, §4 layer 2) and
anything cross-repo (pin==tag bytes is the re-pin flow's job).

**Consumption:** vendor `contract_guard.py` at a pinned `contract-guard-vX.Y.Z` tag
(`repin.py tool contract-guard`), wire it into the pre-commit hook (`--relax-tags`) and a
CI job that runs on EVERY push — no path gate (HK-13: owned artifacts mostly live outside
`contracts/`). A rule change here never moves a consumer until it re-vendors.

Run: `python3 contract_guard.py --check [--root <repo>]` · tests: `python -m pytest tests -q`
