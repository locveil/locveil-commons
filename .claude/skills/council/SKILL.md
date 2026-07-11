---
name: council
description: Run a cross-repo housekeeping/design topic as a moderated council — commons Claude coordinates, per-repo keeper subagents argue their repo's interests on a dossier artifact, the owner decides via an on-page form whose Copy button produces a paste-back delta. Seed with a PROD-N id, free text, or nothing. Use for topics with cross-repo stakes; single-repo work belongs in an ordinary session in that repo.
---

# The Locveil council (PROD-12)

Convention of record: `process/council.md` — read it if in doubt; this file is the
executable procedure. **Everything decided here is treated exactly as if decided in the
terminal**: outcomes land on `board/BOARD.md` (PROD entries + board-as-outbox delegations)
or in `process/`, `board/JOURNAL.md` summarizes, commits are pushed. The dossier artifact is
an ephemeral view — never a record, never cited as authority.

## 1. Seed

Parse the argument:
- **`PROD-N`** → read that entry from `board/BOARD.md`; it is the topic brief verbatim. If
  the id is not on the board, say so and stop (product-repo ids are NOT resolved — v1 limit;
  suggest pasting the entry text as free text, or promoting the topic to a PROD entry first).
- **Free text** → the brief as given.
- **Bare** → publish the dossier at round 0 with ONLY the header + the BARE-SEED topic
  input block from the template, tell the owner to type the topic there → Copy → paste, and
  END THE TURN. The pasted `topic-input` becomes the brief; continue at step 2.

Assign a topic id: the PROD id when seeded from one, else `HK-<n>` — the next free `HK-`
number from the **board ledgers** (the authoritative set scope-guard enforces):
`grep -ohE '\*\*HK-[0-9]+' board/BOARD.md board/BOARD_DONE.md`. Never derive it from
journal headings (they are dated, not HK-prefixed) or from dossier files. On landing, the
HK entry files directly into `BOARD_DONE.md` (born-decided; deferred topics park in
`BOARD.md`) — `process/ledger-discipline.md` §5.

## 2. Keeper round

Spawn the keeper agents **in parallel** (Agent tool; `subagent_type: voice-keeper` and
`bridge-keeper`; add `satellite-keeper` when that repo exists). Each gets: the topic id, the
brief verbatim, the seed provenance (which PROD entry, if any), and any owner comments so
far. Keepers are read-only lenses; they return the structured POSITION block their agent
definition mandates. If the brief was seeded from a PROD entry, keepers reconcile it against
their repo's reality first — surface any "this claim is stale" findings prominently.

For later rounds, **continue the same keeper agents via SendMessage** (context intact) with
only the new material: the owner's delta + the other keeper's points they must answer.

## 3. Synthesize and publish the dossier

Write your own position as a third voice ("commons" keeper card: the umbrella/process
perspective), then a synthesis: where keepers agree, each open **conflict** (use the
conflict block), and a concrete **proposal**. Build the page from
`dossier-template.html` (same directory):

- Copy the template content, fill every `{{PLACEHOLDER}}`, replicate KEEPER/QUESTION/
  CONFLICT blocks as needed, delete unused template blocks and comments.
- **One decision form per round**: question blocks `q1..qN` mirror what you would have put
  in AskUserQuestion — single-select as radios (a recommended option pre-`checked`),
  multi-select as checkboxes, each with an optional `qN-comment` textarea. Always keep the
  `general-comment` field. Every field: `class="cf"` + unique `name` (the serializer depends
  on both). Bump `{{ROUND}}` every redeploy — the round is baked into the delta header and
  the localStorage draft key.
- Write the file to the scratchpad as `council-<topic-id>.html` and publish with the
  Artifact tool — **same file path every round** (same URL), favicon `🏛️`, stable title.
- **Do not publish sensitive material** the owner has flagged; the dossier is private by
  default but publishing is still distribution.

Then **end the turn**: tell the owner the round is open on the page — answer there, press
*Copy my changes*, paste here. **One channel per round**: no terminal AskUserQuestion for
questions that are on the page (quick out-of-band clarifications are fine).

## 4. Parse the reply

The paste is a `council-reply` block (grammar in `process/council.md`):

```
council-reply <topic-id> round-<n>
<field>: <value>            # only fields the owner changed; JSON-quoted when multiline
(no-changes)                # possible: owner accepted everything as pre-selected
```

Mismatched topic id or round → ask before proceeding (a stale page is the likely cause —
remind the owner to reload). `(no-changes)` means every pre-selected (recommended) option
stands. Radio values arrive as the option value; checkbox groups as a comma-joined list.

## 5. Iterate or land

- `back-to-keepers` or substantive comments → step 2 (SendMessage rounds), then a fresh
  round on the dossier (round+1).
- `defer` → journal one line, mark the dossier chip "deferred", stop.
- **Accept** (with or without amendments) → land it exactly as a terminal session would:
  1. Board: new PROD entry or update to the seeded one — decision text + delegation text
     committed in the entry (receiving repos pull, file local ids, write them back; the
     board never asserts their status).
  2. `process/` spec if the decision is a normative convention.
  3. `board/JOURNAL.md` entry (newest on top) summarizing topic, positions, decision.
  4. Commit + push (owner has standing approval for this repo).
  5. Redeploy the dossier once more with the chip set to "decided" and the decision text in
     the synthesis card; then it goes stale by design.

## Cost discipline

Two keepers × N rounds is meaningfully heavier than a solo session. Use the council for
topics with genuine cross-repo stakes; route single-repo topics to an ordinary session in
that repo and say so instead of convening.
