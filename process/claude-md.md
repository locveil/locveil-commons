# CLAUDE.md harmonization — normative convention (HK-2 / PROD-5)

Decided by the second council session (HK-2, 2026-07-11). Applies to every Locveil repo.
Where a repo's CLAUDE.md disagrees with this file or with the blocks it pins, this
convention wins.

## 1. Ownership boundary

- **Commons `process/` is the single normative source for shared process rules** (D-12).
  The shared set today: the ledger triad (owned by `ledger-discipline.md`),
  `every-task-in-the-ledger`, `task-start-reconciliation`, `design-then-implement`,
  `review-then-remediate`, the board/council mechanics, and enforcement wiring.
- **Repo-local LAW stays repo-owned and outside any shared block** — commons never
  rewrites it. Examples: voice's `ws-protocol-doc-canonical` (voice OWNS the WS protocol
  doc; everyone else consumes by pointer), `config-ui-stays-functional`,
  `hexagonal-architecture`, `no-type-checking`, `durable-actions`, per-repo
  `problem-report-inbox` lenses, and each repo's `config-master-*` rule.
- Dialect (priority tags, work-on-main granularity wording, file names) is legitimate and
  **lives in per-repo prose outside the markers**. Shared blocks are dialect-free.

## 2. The mechanism: pinned digest blocks

- Commons owns the block sources in **`process/claude-blocks/<name>.md`**. v1 blocks:
  `shared-invariants` and `cross-repo-board`.
- Each repo carries every applicable block **verbatim** in its CLAUDE.md between markers:

  ```
  <!-- locveil:begin <name> scope-vN -->
  …block text, byte-identical to process/claude-blocks/<name>.md at that tag…
  <!-- locveil:end <name> -->
  ```

- Blocks are **digests**: invariant names, one-line meanings, pointers to the normative
  files, ≤ ~15 lines each. The long-form contract never gets vendored into CLAUDE.md.
  Hard acceptance criterion from HK-2: **adopting the blocks must not grow a product
  repo's CLAUDE.md** — the duplicated long-form mechanics they replace come out.
- Blocks version with the **`scope-vX` tags** (HK-2 q2: single pin — one re-pin moves the
  tool and the block text together).

## 3. Enforcement: the scope-guard `claudemd` rule

- `.scope-guard.toml` gains a `[claude]` section listing each block and its pinned
  content hash:

  ```toml
  [claude]
  file = "CLAUDE.md"
  [[claude.blocks]]
  name = "shared-invariants"
  sha256 = "<hex>"
  ```

- The guard (from `scope-v3`) fails on: missing/broken markers, or block content whose
  hash differs from the pin. The check is **fully local** — no sibling checkout needed in
  hooks or CI (the HK-1 offline constraint).
- **Never edit a block in place.** The flow is: edit the source in commons
  `process/claude-blocks/` → commit (new `scope-vX` tag when the change should ship) →
  each consumer re-pins (copy new block text between its markers, update the hash —
  `scope_guard.py --hash-blocks` prints current hashes). Same-day cheap, by design.

## 4. Slug rename map (HK-2 q3: both sides rename apart)

| old (collides) | voice | bridge |
|---|---|---|
| `config-master-canonical` | `config-master-file` | `config-master-tree` |

No repo keeps the bare slug. Voice records the rename in its historical-number legend;
frozen archives keep the old slug untouched (history is history).

## 5. New-repo seeding

`process/new-repo-template/` is the canonical starting point (HK-2 q4: commons authors,
the bootstrapping task — satellite: voice BUILD-22 — instantiates, never freehands). It
ships day one with: a CLAUDE.md skeleton carrying both shared blocks + placeholders for
repo-local LAW, a starter `.scope-guard.toml`, the committed pre-commit hook, a
path-gated `ledger-guard` CI job, and empty ledger/DONE/journal files in the correct
shape. Discipline is seeded, never retrofitted.

## 6. Standing-text hygiene (one-time, rides the adoption delegations)

- Both product repos still carry the **retired pre-board intake text** ("cross-repo
  filings arrive uncommitted") inside `cross-repo-source-of-truth` — rewrite to
  distinguish board-as-outbox (PROD delegations) from direct operational filings.
- Bridge's preamble claims its invariants have no source of truth outside its CLAUDE.md —
  false since HK-1; rewrite to acknowledge the commons-normative layer.
