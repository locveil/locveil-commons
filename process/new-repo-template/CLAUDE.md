# {{REPO_NAME}} — agent notes

{{ONE_PARAGRAPH: what this repo is, its role in Locveil, its siblings.}}

## Invariants (repo-local LAW — owned here, never inside shared blocks)

- {{REPO_LOCAL_INVARIANTS: e.g. the satellite's consumer-direction WS-protocol pin —
  this repo PINS ../locveil-voice/docs/guides/websocket-api.md by version; the doc wins.}}
- {{HW-GATED marker convention if hardware-dependent.}}

## Ledger & journal

Active ledger `docs/LEDGER.md` · DONE `docs/LEDGER_DONE.md` · journal `docs/JOURNAL.md`
(newest on top). Prefixes: {{PREFIXES}}. Everything else — the triad, rotation,
watermarks — is the shared discipline below; mechanics live in
`../locveil-commons/process/ledger-discipline.md`.

## Shared blocks (pinned — `process/claude-md.md`; edit in commons, then re-pin)

<!-- locveil:begin shared-invariants scope-v3 -->
{{PASTE process/claude-blocks/shared-invariants.md VERBATIM, then hash into .scope-guard.toml}}
<!-- locveil:end shared-invariants -->

<!-- locveil:begin cross-repo-board scope-v3 -->
{{PASTE process/claude-blocks/cross-repo-board.md VERBATIM, then hash into .scope-guard.toml}}
<!-- locveil:end cross-repo-board -->
