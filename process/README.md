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

Pending, until the owning PROD tasks land (see `../board/BOARD.md`):

- **Normative ops spec** + per-repo conformance checklist — PROD-4 (delegates voice
  BUILD-18-narrowed, bridge OPS-15).
- **Problem-report policy spec** (envelope, redaction, rate limits, retention, labels) —
  PROD-6; consumed by both collectors and the private `wb-user-reports`. Owner note: the
  wider "inbox story" is earmarked as the next HK council topic.
