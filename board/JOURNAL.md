# Board journal — newest on top

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
