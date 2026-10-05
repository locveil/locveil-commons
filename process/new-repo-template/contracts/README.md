# {{REPO_NAME}} — contract registry

The direction-labeled index required by `../locveil-commons/process/contracts.md` §2.
Every contract this repo OWNS and every pin it CONSUMES, one line each; details live in
the per-contract READMEs. Layout is the uniform org shape: `contracts/<name>/` owned
(README + STAMP.json; every STAMP declares `artifacts`), `contracts/pins/<name>/`
consumed (the owner's enumerated files, flat + owner STAMP + `PIN.json`; an optional
`README.md` is this repo's own note). Version strings in this file are CURRENT tags only
— history belongs in the per-contract READMEs (the guard checks it).

## Owned

| Contract | Where | Version authority |
|---|---|---|
| _none yet — a surface another repo consumes is cut here in the same change that creates it_ | | |

## Consumed (pins)

| Pin | Owner | Conformance |
|---|---|---|
| [`docs-manifest-schema`](pins/docs-manifest-schema/) | locveil-commons | {{the manifest coherence test}} |

Guards: layer 1 is the vendored `scripts/contract_guard.py` (hook with `--relax-tags`,
CI strict on every push); layer 2 is the tests named above; staleness is the vendored
`scripts/repin.py` (`.repin.toml`, which also pins the vendored tools by tag + sha256).
