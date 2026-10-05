# New-repo template (HK-2 / PROD-5 — `process/claude-md.md` §5)

The canonical starting point for a new Locveil repo's process scaffolding. The
bootstrapping task (satellite: voice BUILD-22) INSTANTIATES this — never freehands.
Discipline is seeded, not retrofitted.

## Instantiation checklist

1. Copy `CLAUDE.md` to the repo root; fill every `{{PLACEHOLDER}}`; write the repo-local
   LAW sections (never inside the marker blocks).
2. Copy `docs/` skeletons (`LEDGER.md`, `LEDGER_DONE.md`, `JOURNAL.md`) — rename freely
   (naming is config), keep the shapes.
3. Copy the configs + hook, then vendor the three tools with repin (never by hand):
   ```
   cp scope-guard.toml ../<new-repo>/.scope-guard.toml     # then edit paths/prefixes
   cp repin.toml       ../<new-repo>/.repin.toml           # fill the placeholders
   cp hooks/pre-commit ../<new-repo>/hooks/pre-commit && chmod +x
   cp -r contracts     ../<new-repo>/contracts             # the registry skeleton
   cd ../<new-repo> && mkdir -p scripts
   python3 ../locveil-commons/packages/repin/repin.py tool repin --config .repin.toml
   python3 scripts/repin.py tool scope-guard && python3 scripts/repin.py tool contract-guard
   git config core.hooksPath hooks
   ```
   `repin.py tool <name>` writes the file and records `pinned_tag` + `sha256` in
   `.repin.toml`; the first call is bootstrapped from the commons copy.
4. Paste the three block texts between their markers (set each marker's `scope-vX.Y.Z`
   label to the tag you vendored) and set the block hashes:
   `python3 scripts/scope_guard.py --hash-blocks` → paste into `.scope-guard.toml` `[claude]`.
5. Docs manifest: write `docs/manifest.json`, pin the schema
   (`python3 scripts/repin.py docs-manifest-schema`) and wire a coherence test that
   validates the manifest against the PINNED schema; put its path in `.repin.toml`. The
   manifest is instance data — it carries no STAMP.
6. Copy `ledger-guard.yml` and `contract-guard.yml` into `.github/workflows/`; adjust the
   ledger path filters to the chosen file names (`ledger-discipline.md` §4). The
   contract-guard job has NO path gate — keep it that way (`contracts.md` §4).
7. First commit must pass the hook. If it doesn't, the instantiation is wrong — fix it,
   don't bypass. The first surface another repo consumes gets its `contracts/<name>/`
   STAMP (three-part version, `artifacts` declared) + tag + registry row in the same
   change that creates it.

Python components follow `process/python-layout.md` from birth:
`<component>/src/<locveil_pkg>/` + `<component>/tests/`, config tree `config/` at
repo root, Dockerfiles in root `docker/` with root build context.
