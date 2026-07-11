# Board journal — newest on top

## 2026-07-11 — PROD-5 voice delegation consumed (BUILD-23) — voice on scope-v3

The voice session pulled the PROD-5 delegation and executed it as **BUILD-23** (the
pre-assigned ID), narrowed at intake exactly as the delegation specified (drift-guard-script
wording dead; scope-guard's `claudemd` rule is the guard). Voice CLAUDE.md now carries both
pinned blocks at `scope-v3` (byte-identical, tamper-tested red/green), net-shrank 165→160
lines (the six long-form shared invariants out, voice dialect condensed to one
`ledger-dialect` bullet), re-pinned the tool to 1.1.0, rewrote the retired pre-board intake
bullet, renamed `config-master-canonical`→`config-master-file` (legend row added), added
`CLAUDE.md` to the CI `ledger` filter, and recorded the BUILD-22 template dependency.
Pushed; the voice `ledger-guard` CI validates the blocks remotely. PROD-5 now waits only on
bridge OPS-16 to confirm.

## 2026-07-11 — HK-2 decided: CLAUDE.md harmonization (executes PROD-5)

Second council session, bare seed, one keeper round + one owner round. Topic: where shared
rules live, how product Claudes access them, how they learn the board process, how new
repos get seeded. Keepers' unanimous finding: **the topic IS the parked PROD-5 — execute
it, don't re-design it.** Root cause of the owner's "sessions search for the board
process" complaint found and named: neither product CLAUDE.md mentions the board AT ALL,
and both still teach the retired pre-board uncommitted-intake mechanism inside
`cross-repo-source-of-truth`; bridge's preamble also still claims invariant sovereignty
that `ledger-discipline.md` took over at HK-1. Both keepers independently converged on the
same mechanism: **pinned digest blocks between markers + pointers** (bare pointer fails
offline enforcement — hooks/CI/cloud-triage run without siblings; full prose fails the
token budget), enforced by a `claudemd` hash rule in scope-guard (one tool, one hook, one
pin — `scope-v3`), with the hard criterion that adoption must NOT grow a product CLAUDE.md
(each currently duplicates 20–55 lines of ledger mechanics that come out). Owner accepted
all recommendations: single scope-vX pin; `config-master-canonical` renames apart both
sides (`config-master-file` / `config-master-tree`); commons authors
`process/new-repo-template/` and voice BUILD-22 instantiates it; immediate execution.
Deferred by owner: the session-start **inbox story** — "much bigger, the next HK
exercise". Landed: `process/claude-md.md` (normative), PROD-5 → `[>]` with delegations
(voice BUILD-23 narrowed, bridge OPS-16 redefined — its text referenced the deleted
`check_scope.py`), HK-2 filed to `BOARD_DONE.md`, this entry. Executed same session
(`1786f91`, tag `scope-v3`): `process/claude-blocks/` (both digest sources),
`process/new-repo-template/` (CLAUDE.md skeleton + starter config + hook + CI template +
ledger/journal shapes), scope-guard 1.1.0 with the `[claude]` hash rule +
`--hash-blocks`, commons' own adoption (blocks + config + CI filters + the overdue
`process/README.md` fix), CI convention in `ledger-discipline.md` §4. Verified: green on
commons; tampered block and missing markers both fail correctly. PROD-5 stays `[>]` until
BUILD-23/OPS-16 confirm consumption.

## 2026-07-11 — PROD-13 CLOSED: the discipline is live in all three repos

Both delegations executed same-day and wrote back (voice **BUILD-30**, bridge **OPS-22**);
commons-side deliverable was already done, so the entry moves to `BOARD_DONE.md` — the
first close performed *under* the discipline it created, gated by its own pre-commit hook.
Full arc: decided as HK-1 in the first live council, executed commons-side (scope-guard +
BOARD split + CI/hooks, `scope-v1`), consumed by both products — whose first real rotation
caught a v1 `--rotate journal` bug (archives written character-per-line; scratch tests
missed it), fixed commons-side as **scope-v2** with both consumers re-pinning. Regime 2
worked exactly as designed under a concurrent two-session collision: one fix in commons,
consumed by re-pin, no forked copies. All three repos now run the union checker green with
committed hooks + `ledger-guard` CI; both product journals rotated under their watermarks;
voice's DONE ledger rotated with all archived IDs resolvable.

## 2026-07-11 — PROD-13 voice delegation consumed (BUILD-30) — both delegations now written back

The voice session pulled the PROD-13 delegation, verified it per its
`task-start-reconciliation` (both advertised pre-existing findings confirmed real: the
unsorted DONE I18N section and the DONE ledger over the 4000-line ceiling), filed it as
**BUILD-30**, and executed the full cutover (vendored tool + `.scope-guard.toml`,
`check_scope.py` retired, `ledger-guard` CI re-pointed, committed pre-commit hook live,
invariant text + gate wording updated, DONE-ledger rotation adopted, journal 1510→708 and
DONE 4273→1930 rotated losslessly). Voice's first rotation attempt hit the same v1
`--rotate journal` bug **concurrently** with the bridge (its corrupted first-pass commits
were rebuilt; nothing had been pushed) — the sessions collided mid-fix on this repo, and
the bridge's scope-v2 landed first; voice re-pinned to it. Regime 2 held: one fix,
commons-side, consumed by re-pin on both sides. With both local IDs written back,
PROD-13's remaining board action is closing the entry (commons-side deliverable already
done) — left to the commons session that owns the entry, since it was active in this
working copy at the time.

## 2026-07-11 — PROD-13 bridge delegation consumed (OPS-22); scope-v2 tagged (rotation bugfix)

The bridge session pulled the PROD-13 delegation, verified it per its
`task-start-reconciliation`, filed it as **OPS-22**, and executed the cutover (vendored
tool + `.scope-guard.toml`, `check_scope.py` retired, `ledger-guard` CI re-pointed,
committed pre-commit hook live, invariant text updated). The first real `--rotate journal`
run then caught a v1 defect: **archives were written character-per-line** (in
`rotate_journal`, the section body was double-indexed after unpacking — `s[1]` on the
already-unpacked day-lines list — so `"\n".join` iterated a string; the kept-sections
rewrite had the same bug, silently truncating the journal). No history lost — the journal
is git-tracked and was restored. Fixed here (2-line fix), validated against a copy of the
bridge tree with a line-by-line Counter diff (1625 → 989 kept + 635 archived + pointer,
zero lines missing), tagged **scope-v2** (1.0.1). Also made the docs honest: v1's
README/spec said hooks run `--check` but no such flag existed (the bare invocation was the
check) — v2 adds the explicit `--check` flag (mutually exclusive with `--rotate`). Both
PROD-13 delegations re-pointed at scope-v2; **voice must pin scope-v2, not v1** — its
overdue journal rotation (1510 lines) would have hit the same bug. Bridge ID written back;
voice ID still pending.

## 2026-07-11 — HK-1 decided: ledger/journal discipline harmonized (files PROD-13)

First live council session (PROD-12's shakedown) — bare seed, topic typed into the round-0
dossier, decided in one keeper round + one owner round. Topic: harmonize ledger/journal
discipline across the repos and migrate `check_scope.py` to commons. Keeper reconciliation
corrected the brief: **neither script is a superset** (bridge adds DUPLICATE/MISPLACED/
ALIAS/tombstones; voice has UNINDEXED-review + evidence-index `[x]` semantics — and the
triad itself originated in voice, DOC-12), voice CI-gates its checker just like bridge,
pre-commit hooks exist nowhere, bridge's DONE doesn't rotate, and **both journals sit over
their own ~1500-line high-water today** (voice 1510, bridge 1625) — manual rotation
demonstrably drifts. Both keepers: support-with-conditions; conditions unanimous (union
rule set, per-repo config, pinned consumption, check-vs-rotate split, archived-ID
resolution). Owner accepted all recommendations; amendments: PROD-13 executes immediately;
required-task-tags in v1 but to be revisited in a future release-numbering/sprints
housekeeping round; **HK-N becomes a tracked board prefix** — council topics are
born-decided and file directly into `BOARD_DONE.md`. Rename question (brief point 5):
dropped — naming is config. Landed: `process/ledger-discipline.md` (normative), PROD-13
on the board with voice+bridge delegations, this entry. Executed same session:
`packages/scope-guard/` (union tool, `locveil-scope-guard`, tag `scope-v1`), the
BOARD/BOARD_DONE split (PROD-1/2/3/12 + HK-1 moved), commons `.scope-guard.toml` +
`ledger-guard` CI + committed pre-commit hook (`hooks/`). Verification: commons green;
bridge green (+ true overdue-journal warning); voice run surfaced **two true pre-existing
findings its own checker could not see** — the DONE I18N section is unsorted (the old
`[A-Z]+` ordering regex never matches `I18N`) and RELEASE_PLAN_DONE.md exceeds the
4000-line hard ceiling — both folded into the voice delegation. Rotation verified on
scratch copies: bridge journal 1625→698 lines (whole days, pointer updated), voice DONE
4273→1930 with all 125 archived IDs still resolvable (zero false orphans).

## 2026-07-11 — PROD-12: the council built (skill + keepers + dossier + convention)

Owner-designed over three analysis rounds, filed and built same day. Deliverables:
`.claude/skills/council/SKILL.md` (the procedure: seed → parallel keeper round →
synthesis → dossier publish → paste-back delta → iterate → land on the board),
`.claude/skills/council/dossier-template.html` (theme-aware page with the decision form,
dirty-field delta serializer, localStorage drafts, clipboard Copy with fallback),
`.claude/agents/{voice,bridge}-keeper.md` (read-only partisan lenses that load their repo's
CLAUDE.md/ledger/journal and reconcile seeded claims before arguing), and
`process/council.md` (the normative convention: terminal-equivalence of decisions,
paste-is-the-channel, one-channel-per-round, PROD-only seeding v1, `council-reply` format
v1). CLAUDE.md and process/README gained pointers. Not yet exercised live — the first real
topic shakes it down; the satellite keeper joins when BUILD-22 creates that repo.

## 2026-07-11 — Controller cutover CONFIRMED: the deployment is fully Locveil

Owner made the 9 new GHCR packages public (org policy initially blocked Public — fixed via
org Settings → Packages → allow public package creation) and ran both
`ops/migrate-to-locveil.sh` scripts on the WB7 successfully. The controller now runs
`locveil-voice`, `locveil-bridge`, `locveil-bridge-ui` from `/mnt/data/locveil-*-config`
under `locveil-{voice,bridge}.service` — zero `wb-mqtt` naming left anywhere in the product
estate (repos, images, containers, units, runtime trees, package names). The re-pointing arc
(PROD-2 + its BUILD-29/OPS-21 residue) is fully closed. Next natural board item: the
single-compose-with-startup-order design (voice BUILD-28's cross-repo intent).

## 2026-07-11 — Deployment-identity rename executed repo-side (voice BUILD-29 + bridge OPS-21)

Owner decision: complete the re-pointing down to the metal — the controller must run new
images with zero `wb-mqtt` leftovers, including the `/mnt/data/mqtt-*-config` runtime trees →
`locveil-*-config`. Both repos executed the coordinated rename in one session
(`locveil-voice@0aca2f7`, `locveil-bridge@bba68c9`): images (`locveil-voice-*`,
`locveil-voice-ui`, `locveil-bridge`, `locveil-bridge-ui` — UI name = owner pick), containers,
systemd units (`locveil-{voice,bridge}.service`), runtime trees, clone paths, INSTALL flows;
bridge also renamed its Python distribution (`locveil-bridge`, import package kept); voice
regenerated its API contract chain (description strings; config-ui gates green). Each repo
ships a one-time `ops/migrate-to-locveil.sh` for the controller cutover (runtime tree moves
with state/models/.env intact). Sequencing: CI publishes dispatched (runs watched); owner then
flips the new GHCR packages PUBLIC and runs the two migration scripts on the WB7. Voice also
surfaced a pre-existing order-dependent test flake → voice BUG-42.

## 2026-07-11 — PROD-2 CLOSED: bridge re-point executed (`locveil-bridge@bd256d8`, OPS-20)

The first board-as-outbox round-trip completed exactly as D-5 designed it: the bridge session
pulled the PROD-2 delegation, verified it per its `task-start-reconciliation` (the `.venv`
shebang warning proved out verbatim), filed it as **OPS-20**, executed (eval re-point green —
cli 4/4, backend suite 698 post venv-rebuild; sweep; container user; GHCR refs), and wrote
the ID back. PROD-2 is `[x]`; the uncommitted-sibling-filing mechanism is now fully retired.
Standing residue: the coordinated deployment-identity rename (voice BUILD-29 + bridge OPS-21,
owner-gated, likely one joint session with the BUILD-28 single-compose design), and each repo
needs one CI publish before its next controller `update.sh`.

## 2026-07-11 — PROD-2: voice re-point delegation EXECUTED (`locveil-voice@d0c0755`)

The voice BUILD-21 tail landed: eval refs re-pointed to `../../locveil-commons/eval` (gates
green from the new paths — cli 5/5, device tier-1 48/48), operative name sweep, `domovoy` →
`locveil` container user, GHCR pull refs → `ghcr.io/locveil/*`, productization pointer swap;
BUILD-21 closed in the voice ledger, residual deployment-identity rename filed there as
BUILD-29. Two operational notes: (a) the owner must run one voice CI publish before the next
controller `update.sh` (compose now pulls `ghcr.io/locveil/*`, which doesn't exist until the
first org-side publish); (b) the local dir rename bricks a repo's `.venv` (absolute
console-script shebangs) — the voice venv was rebuilt with `uv sync --all-extras`; the bridge
delegation now carries the same warning for `backend/.venv`. PROD-2 remains `[>]` until the
bridge writes its local ID back.

## 2026-07-11 — BUILD-21 commons bootstrap (PROD-2 restructure + PROD-3 board)

Owner had completed the rename chain (GitHub org `locveil`, repos `locveil-commons` /
`locveil-voice` / `locveil-bridge`, local dirs + remotes) and, earlier the same day, the
PROD-1 name lock (Locveil; .com/.ru registered, org claimed, .io dropped, .eu pending ID
verification). This session executed the commons side of voice BUILD-21:

- **D-2 restructure**: eval framework moved to `eval/` via `git mv` (package `eval_commons`,
  `shared/`, `examples/`, `tests/`, pyproject, uv.lock, ARCHITECTURE.md, its README);
  `board/`, `process/`, `packages/`, `site/` created. `contracts/` and `docs/design/` stay
  at root. Distribution renamed `eval-commons` → `locveil-eval` (import name unchanged);
  uv.lock regenerated; test `contracts/` anchors repointed (`parents[2]`). Suite green from
  the new home: 40 passed (`cd eval && uv run --all-extras --with pytest --with jsonschema
  pytest tests/ -q`).
- **Name sweep** of repo-owned files (code comments, examples, shared YAML, docs,
  contracts/README). NOT swept, by design: the pinned artifacts + `PIN.json` +
  `crossover_fixtures.json` (new names arrive with the next re-pin / fixture re-author) and
  the dated records (`productization_roadmap.md`, body of the migrated decision record).
- **PROD-3 board bootstrap**: `BOARD.md` (conventions + §3 seed backlog as PROD-1..11),
  this journal, new commons CLAUDE.md (session discipline, ownership regimes, tag scheme),
  root README rewritten as the umbrella; old README/ARCHITECTURE live on under `eval/`.
- **Decision record migrated**: `docs/design/productization.md` copied verbatim from
  `locveil-voice@92d1abd` with a migration + name-lock header; the voice-side pointer swap
  is delegated in PROD-2.

Open tails: PROD-2 delegations to voice (BUILD-21 tail: eval-ref re-point + pointer swap)
and bridge (first board-as-outbox delegation, ID pending write-back); `locveil.eu` owner
action in PROD-1.
