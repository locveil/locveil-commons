# process/ — normative process & product specs (ownership regime 3: commons owns)

Here now:

- **[`council.md`](council.md)** — the cross-repo council convention (PROD-12): moderated
  discussions with per-repo keeper subagents on a dossier artifact; ground rules + the
  `council-reply` paste-block format. Executable half: `.claude/skills/council/`.
- **[`ledger-discipline.md`](ledger-discipline.md)** — ledger & journal discipline
  (HK-1/PROD-13): the triad, rotation watermarks, the ID-resolution guarantee, scope-guard
  enforcement, the board rule pack, CI convention. Tool: `../packages/scope-guard/`.
- **[`claude-md.md`](claude-md.md)** — CLAUDE.md harmonization (HK-2/PROD-5): pinned digest
  blocks between `locveil:begin/end` markers, the `claudemd` guard rule, ownership
  boundary, slug rename map, new-repo seeding. Block sources: [`claude-blocks/`](claude-blocks/);
  template: [`new-repo-template/`](new-repo-template/).
- **[`problem-reports.md`](problem-reports.md)** — the inbox story (HK-3/PROD-6/PROD-14):
  choreography semantics, leak fence, retention/privacy policy, consumption rules, lens
  co-ownership. Machine core: [`../contracts/report-protocol/`](../contracts/report-protocol/README.md)
  (tags `report-protocol-vN`; pinned + test-validated by voice, bridge, and locveil-reports).
- **[`contracts.md`](contracts.md)** — the general contract convention (HK-5/PROD-16):
  contract classes, the uniform `contracts/` layout (owned + `pins/` + registry README),
  STAMP/PIN cores, family tags, two-layer enforcement (contract-guard + conformance
  tests), staleness rules. Tool: `../packages/contract-guard/`.

Pending, until the owning PROD tasks land (see `../board/BOARD.md`):

- **Normative ops spec** + per-repo conformance checklist — PROD-4 (delegates voice
  BUILD-18-narrowed, bridge OPS-15).
