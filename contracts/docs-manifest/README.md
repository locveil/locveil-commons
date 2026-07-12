# docs-manifest — the user-facing docs tree, machine-readable (internal)

Repo-internal contract (HK-6/PROD-17; convention: `../../process/user-docs.md` §4).
The artifact is [`docs/manifest.json`](../../docs/manifest.json) — it lives with the docs
it describes; this folder carries the STAMP and this pointer. Schema of record:
[`process/user-docs/manifest.schema.json`](../../process/user-docs/manifest.schema.json)
(the org-wide vocabulary — commons owns it, every repo's manifest validates against it).

Guards: schema validation + manifest↔tree coherence in
`eval/tests/test_docs_manifest.py` (normal suite); the docs-verdict presence rule in
scope-guard (`scope-v5`, `docs_verdict_since` in `.scope-guard.toml`). Node policy:
additions ride the causing task, removals by tombstone or filed supersession —
`process/user-docs.md` §4.
