# User-facing documentation — the org convention (HK-6, normative)

Decided by council HK-6 (2026-07-12, two rounds, all three product keepers; arc in
`board/JOURNAL.md`). Applies to every Locveil repo. On disagreement with per-repo text,
this file wins. Companions: `contracts.md` (the manifest is a repo-internal contract),
`ledger-discipline.md` (the docs-verdict line lives in completion entries).

## 1. Scope: what is user-facing

A document is user-facing when it addresses a READER, not the codebase. Classes and
audiences (the `class` / `audience` enums of the manifest schema, §4):

| Class | Audience | Example |
|---|---|---|
| front-door | all | root `README.md` — status banner, what-it-does, doc index |
| quickstart | tester | first safe look; never points at a live house broker |
| operator | operator | install/update/rollback runbooks (`ops/INSTALL.md`) — IN scope (HK-6 q4) |
| howto | tester/integrator | task guides with a worked example |
| narrative | all | architecture for a curious reader (diagram-led) |
| end-user | end user | the report-a-problem class — each product with a report pipeline authors its own, in its own voice |
| canonical-reference | integrator/contributor | version-stamped, conformance-tested wire/API truth (`websocket-api.md`, contract READMEs) — **style carve-out**: technical language allowed, never "simplified" by decree; location is repo dialect, defined by its GUARDS (stamp + conformance test), always linked from CONTRIBUTING.md |
| contributor | contributor | `CONTRIBUTING.md` (required per repo) + contributor-addressed READMEs (eval framework, contracts registry) |
| diagram | all | `.dot` source + rendered image, same basename — one unit, updated in the same change |

NOT user-facing: `docs/design/`, `docs/review/`, `docs/planned/`, ledgers/journals/
archives, CLAUDE.md, pin folders' internals, eval YAML. **ADRs are abolished as a class**
(HK-6 q3): existing ones are reviewed, their live content redistributed into
design/review/user/contributor docs, the husks archived with supersession banners.

**Required-class floor — only where the capability exists** (HK-6 round-2 ruling): every
product repo staffs front-door, quickstart-or-equivalent, operator, and — where the
capability exists — end-user (report pipeline) and canonical-reference (a wire surface)
classes. A repo without the capability carries nothing for it; a capability whose doc
truth is gated (hardware, phase gates) carries a **pending-gate node** naming its gate —
declared, never fiction, never silently absent. Commons has no end-user classes; its
contributor/integrator docs are in scope.

## 2. Style (extracted from the exemplar corpora)

Reader-first, second person; each doc opens with who it's for (+ a diagram where one
helps). **No internal tracking language** anywhere a user can see — no task IDs, ledger/
journal refs, file:line; this **extends to schema/OpenAPI field descriptions** (they
surface in viewers and generated types). Russian product surface is quoted verbatim
(«сообщи о проблеме»), never translated away; docs are English for operator/tester/
integrator readers — a Russian end-user doc class is PARKED until a real non-owner user
exists ("no Russian docs today", HK-6). Diagrams are Graphviz: committed `.dot` source +
rendered image, same basename, render command in the header, regenerated in the same
change. Status banners state honestly what is built vs pending — and banners are
themselves audited (a stale banner is staleness). Durability rule: prefer wording that
names no repository or internal path (it survives renames). App-embedded text stays
micro-copy; on any overlap, docs win.

## 3. The hardened rule: documentation-is-part-of-done

For every task, before completion: does the change alter behavior any manifest node
describes? The answer is RECORDED — a **docs-verdict line in the completion (DONE-ledger)
entry**:

```
docs: <node-id>[, <node-id>…]            # updated, same change
docs: none — <one clause>                 # explicit dismissal
```

- **Caused vs discovered:** staleness you CAUSE is fixed in the same change, never filed;
  staleness you DISCOVER is filed as a DOC task tagged to the next release gate (it may
  not rot indefinitely).
- **Enforcement, lane-separated (HK-6 q3):** scope-guard (commons release, vendored,
  `scope-v5`+) checks the verdict line's presence/syntax on new completion entries —
  ledger lane only. The manifest conformance test (per-repo, drift-guard pattern, normal
  CI suite) owns everything manifest-aware: node↔tree bijection, floor, verdict node-ids
  exist, and the falsifiability check — a change touching a mapped surface glob while the
  verdict says `none` is flagged. Promotion of the test into shared tooling waits for
  rule-of-two. All checks stay `--check`/test-tier; no push gate writes docs for you.
- **Hardware dialect:** docs bind to the artifact's phase — DES story changes → narrative
  same change; provisioning changes → provisioning runbook same change; PCB → build doc
  at board-ordered and bench-verified; FW → flash/troubleshoot guides at FIRST LIGHT.
  A section whose truth needs the bench is `hw_gated` — the rule never forces fiction.
- **Review cadence, event-driven:** release cuts (software repos) and phase-gate
  crossings (satellite) are mandatory manifest reviews — the REL-4 audit format, made
  cheaper by the suspect-set (surfaces touched since last audit → candidate nodes).
  **A docs-review task may additionally be filed in any repo's ledger at any time; one
  filed in the COMMONS ledger fans out as a board-as-outbox delegation to every repo**
  (HK-6 round-2 ruling) — each repo files a local DOC task and writes it back.

## 4. The docs manifest (repo-internal contract)

Every repo carries a machine-readable manifest of its user-facing tree:

- **Artifact:** `docs/manifest.json` (hand-written, lives with what it describes).
  **Stamp:** `contracts/docs-manifest/` — STAMP.json (`docs-manifest-vN`, bumped only on
  schema reshape) + pointer README; registry row labeled INTERNAL. The established
  ui-openapi/ws-protocol pointer pattern.
- **Schema:** commons-owned, ONE vocabulary — `process/user-docs/manifest.schema.json`
  (testable; prose here). Node: `{path, class, audience, covers: [surface…],
  status: ok|banner|pending-gate, phase?, hw_gated?, gate?, derives_from?, diagram?,
  canonical?: {invariant, stamp, guard}}`. Header: the repo's user-facing roots + its
  surface→glob map. Repos OMIT inapplicable fields; they never invent dialect fields.
- **Surfaces stay small (≤10) and repo-owned** (`rest-api`, `catalog`, `drivers`,
  `deployment`, `mqtt`, `reports`, …). The glob map turns a diff into candidate nodes at
  COMPLETION time — a false positive costs one dismissal clause, not a red gate.
  `covers`/glob metadata is itself docs and may rot; the review cadence audits it too;
  trigger lists grow via the verdict feedback loop, never required-exhaustive at birth.
- **`derives_from`:** user docs DERIVE from engineering leaf truth (satellite
  `docs/devices/`), never duplicate it — the edge is declared and checkable.
- **Node policy (nobody asks anybody):** additions ride the causing task — the coherence
  test fails a doc committed without a node (registration IS the manifest edit);
  removing the last node of a floor class without a same-change replacement fails the
  guard; nodes leave only by tombstone (the MOVED pointer pattern) or a filed
  supersession/DOC task; cross-cutting reorgs get a filed task (review-then-remediate).
- **CONTRIBUTING.md is required per repo and lives IN the manifest**
  (`audience: contributor`) — contributor docs rot on the same triggers (proven: a
  CONTRIBUTING drifted stale in under 24 hours while outside the old rule's scope). It
  narrates and LINKS the normative sources (contracts registry, design entry points, dev
  setup, repo LAW); the sources themselves stay outside the manifest under their own
  disciplines. This resolves normative-doc placement: the class is defined by its
  guards, the location is repo dialect, the access path is CONTRIBUTING.md.

## 5. Arrival path

The digest line lives in the `shared-invariants` pinned block (from `scope-v5`); the
normative text is THIS file. `process/new-repo-template/` seeds the invariant, a skeleton
`docs/manifest.json`, and a CONTRIBUTING.md stub — repo N+1 is born compliant. The org
README rides PROD-9 (no separate artifact — HK-6 q7).
