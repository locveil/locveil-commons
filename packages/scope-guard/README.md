# locveil-scope-guard

The Locveil ledger/journal discipline guard — ONE config-driven, stdlib-only tool
superseding the per-repo `check_scope.py` scripts. Normative convention:
`process/ledger-discipline.md` (HK-1 / PROD-13). Tags: `scope-vX`.

## Consumption (regime 2 — pinned, vendored)

Consumers do **not** track this directory live. Vendor `scope_guard.py` at a tagged
version (the version stamp is in the file) next to your own `.scope-guard.toml`:

```
git -C ../locveil-commons show scope-v2:packages/scope-guard/scope_guard.py > scripts/scope_guard.py
```

Behavior changes happen here, never in a consumer's copy; consumers move by re-pinning.
Starter configs verified green against each repo's tree on 2026-07-11: `examples/`.
Current tag: **scope-v2** (1.0.1) — fixes v1's `--rotate journal` writing archives
character-per-line (caught by the first real rotation, bridge OPS-22; do not pin scope-v1
if you will rotate) and adds the explicit `--check` flag.

## Run

```
python3 scripts/scope_guard.py --config .scope-guard.toml            # check (read-only)
python3 scripts/scope_guard.py --config .scope-guard.toml --rotate   # journal + DONE rotation
```

`--check` is the only mode hooks and CI may run (warnings exit 0, errors exit 1; over
hard ceiling is an error). `--rotate` executes the rotation rule deterministically —
run it as its own commit. Rotated ledger archives stay in the known-ID set (the
`ledger.archive_dir` scan) — old IDs never become orphans.

## Rules

Union of the historical voice + bridge checkers, config-toggled: DUPLICATE id ·
MISPLACED status (two-directional) · ORPHAN finding · DEAD evidence link (path-scan
and/or the voice-style `[x]`-marker index) · ALIAS phantom · MISFILED task ·
OUT-OF-ORDER id · UNINDEXED review · tombstones — plus HK-1 additions: journal/DONE
watermarks · archive-pointer integrity · completion-journal cross-check ·
required-task-tags · board rule pack (delegation write-back).
