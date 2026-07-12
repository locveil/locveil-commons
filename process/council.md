# The council — cross-repo discussion convention (PROD-12, normative)

**Status: ADOPTED 2026-07-11 (owner-designed over three analysis rounds in the commons
session; built same day). Executable half: `.claude/skills/council/` (SKILL.md + dossier
template); keeper lenses: `.claude/agents/{voice,bridge,satellite}-keeper.md` (satellite
keeper active since 2026-07-12, PROD-15; spawned when the topic touches its repo —
coordinator's call).**

A council is a moderated cross-repo discussion run FROM this repo (D-4): the commons session
coordinates, per-repo **keepers** (read-only subagents loaded with their repo's CLAUDE.md,
ledger and journal) argue their repo's interests, **the owner decides**. The discussion
renders on a **dossier** (a private artifact web page, one per topic, updated in place each
round); the owner answers through an on-page form.

## Ground rules (normative)

1. **Terminal-equivalence.** A council decision is recorded and enforced exactly as if it
   had been reached in a terminal session: accepted outcomes land as `board/BOARD.md` PROD
   entries (with board-as-outbox delegation text; receiving repos pull, file local ids,
   write them back) or as `process/` specs; `board/JOURNAL.md` summarizes. Nothing cites
   the dossier; it is an ephemeral view, never a record.
2. **The paste is the only return channel.** The dossier page cannot reach the session
   (artifact CSP blocks all network egress — by design, not by accident). The page's *Copy
   my changes* button serializes only the fields the owner changed this round into a
   `council-reply` block; the owner pastes it into the terminal. Un-copied page edits are
   protected by localStorage drafts across reloads of the same round, but the paste is the
   commit.
3. **One channel per round.** While a dossier round is open, its questions are answered on
   the page — the coordinator does not duplicate them as terminal forms.
4. **Seeding (v1): `PROD-N` on this board, free text, or bare** (topic typed into the
   dossier's seed form). Product-repo task ids are not resolved in v1 — promote the topic
   to a PROD entry, or paste its text. A seeded entry is reconciled against repo reality by
   the keepers before anyone argues from it.
   **Topic ids (HK-1 amendment):** a topic not seeded from a PROD entry gets the next free
   `HK-N`, determined from the **board ledgers** — the `**HK-N**` declarations across
   `board/BOARD.md` + `board/BOARD_DONE.md` (never from journal headings or dossier files;
   scope-guard enforces uniqueness over exactly this set). **Filing** follows
   `ledger-discipline.md` §5: HK topics are born-decided — the entry files directly into
   `BOARD_DONE.md` when the council lands; a deferred council parks it in the active board.
   A council that lands its outcome under an existing/new PROD entry still files its HK
   entry (pointing at that PROD id) — the HK ledger is the council's own record.
5. **Keepers are partisan, read-only lenses.** They write no files anywhere, they cite
   `file:line`, they argue their own repo's invariants and interests only. The coordinator
   contributes the commons/process lens and the synthesis; conflicts are surfaced, not
   smoothed over.
6. **Scope discipline.** Councils are for topics with genuine cross-repo stakes. A
   single-repo topic gets an ordinary session in that repo.

## The `council-reply` paste-block (format v1)

```
council-reply <topic-id> round-<n>
<field>: <value>
...
```

- Header: topic id (`PROD-N` or `HK-<n>`) + the round baked into the page.
- One line per **changed** field only. Values are plain; JSON-quoted (`"..."`) when they
  contain newlines, quotes, colons, or leading/trailing whitespace. Checkbox groups are
  comma-joined lists. An explicitly cleared field arrives as `""`.
- A reply of `(no-changes)` accepts every pre-selected (recommended) option as-is.
- Standard single-select vocabulary: `accept` · `amend` (+ `qN-comment`) ·
  `back-to-keepers` (+ comment) · `defer`.

Format changes bump the version here and in the template comment — the parser (the
coordinator) must keep accepting v1.
