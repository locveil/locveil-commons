# Locveil board — the cross-repo initiative ledger (PROD-N)

The D-4/D-5 board (`docs/design/productization.md`). One entry per cross-repo initiative,
stable ID `PROD-N`, referenced in commit messages (`PROD-3: …`).

## Conventions

- **A cross-repo idea = a PROD task; the deliverable is a design doc.** Placement rule: a
  design defining a concept/contract both products consume lives in this repo's
  `docs/design/`; a design whose primary artifact is one repo's code lives in that repo's
  `docs/design/`, even when the session ran here.
- **Board-as-outbox (D-5):** on completion a PROD task *delegates* — the delegation text is
  committed in the entry below (this repo is co-owned ground; both product repos may write
  here). The receiving repo's session pulls the delegation, verifies it per its own
  `task-start-reconciliation`, files it under a local ID, and **writes that ID back into the
  entry**. Nothing lives uncommitted in a sibling working tree.
- **The board never asserts a delegated task's status** — per-repo ledgers own status. An
  entry lists delegated IDs; it closes when its own commons-side deliverable is done and all
  delegations have local IDs written back.
- Statuses: `[ ]` open · `[>]` in progress · `[x]` done. Session notes go to
  `JOURNAL.md` (newest on top), not here.
- **Ledger discipline (HK-1 / PROD-13, normative: `process/ledger-discipline.md`):** this
  board is the active ledger; completed entries MOVE to `BOARD_DONE.md` in the same change
  as their journal entry. Council topics carry the `HK-N` prefix; being born-decided they
  file directly into `BOARD_DONE.md` (a deferred council parks its HK entry here). Guarded
  by scope-guard (`packages/scope-guard/`, config `.scope-guard.toml`).

## Ledger

Completed entries live in `BOARD_DONE.md` (moved on close; `process/ledger-discipline.md`).

## PROD — cross-repo initiatives

- [ ] **PROD-4 — Normative ops spec** (D-12) in `process/`: the converged pattern (sdcard
      clone update-time-only, `/mnt/data/<name>-config`, repo-owns-config rsync, `.env`
      secrets, systemd oneshot `RequiresMountsFor=/mnt/data` ONLY, GHCR pull-not-build, log
      rotation, 127.0.0.1 healthchecks, start-period > fleet boot) + a conformance checklist.
      Shared *scripts* only at the third consumer (rule of three). Delegates on completion:
      voice BUILD-18 (narrowed) + bridge OPS-15.
- [ ] **PROD-8 — core-py bootstrap + first two extractions** (D-8): `packages/core-py`
      skeleton (own pyproject, `core-py-vX` tags), then the two designs — dynamic code
      loader (voice ARCH-42; voice consumer #1, bridge #2 via CORE-7) and logging scheme
      (voice ARCH-43; retires the BUG-30/OPS-12 hand-copy → bridge OPS-14).
- [ ] **PROD-9 — Landing page + first suite manifest** (D-11/D-12): `site/` on GitHub Pages
      at `locveil.com` — joint story, per-product blurbs, honest quickstart, routing only
      (never duplicates per-repo reference docs); the calver suite manifest ("Locveil
      2026.xx = voice vX + bridge vY + contract vZ + images …", gated on the cross-suites
      passing against exactly those pins) is its "current release" section. Unblocked by
      PROD-1.
- [ ] **PROD-10 — ui-kit package + stylebook** (D-8/D-9, next release): `packages/ui-kit`
      npm package consumed by both config UIs (`../locveil-voice/config-ui`,
      `../locveil-bridge/ui`); component boundaries keep one-shell-with-plugins reachable —
      no plugin framework before two real plugins exist.
- [ ] **PROD-11 — FUTURE design: Home Assistant in parallel to Wirenboard** (D-4's stress
      test): if the canonical DeviceCommand contract survives HA unchanged, voice gets zero
      tasks; if voice needs changes, the contract leaked WB-specifics. Waits until wanted.
