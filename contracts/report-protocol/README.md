# report-protocol — the shared inbox truth (owned, machine core)

The machine half of the problem-reports contract (HK-3/PROD-6): labels + colors, lenses,
ticket **types** (first-class — a future type is a vN bump, not a redesign), the typed
state machine (`ping_pong_max`), title prefixes, bundle path, handover schema, slug
registry. The prose half — choreography, leak fence, retention, lens co-ownership — is
[`process/problem-reports.md`](../../process/problem-reports.md); on shared vocabulary the
machine core defines, the prose points here.

- **Artifact:** [`report-protocol.json`](report-protocol.json)
- **Version:** `STAMP.json` + tag (current: see the STAMP; `v1.0.1` is the bytes-only cut
  where the STAMP began to enumerate the artifact — HK-13) — the stamp defines, changelogs
  narrate (`process/contracts.md` §3). The in-artifact `version` field arrives at v2.
- **Consumers (pin + conformance test each):** locveil-voice (`/report` collector),
  locveil-bridge (filing constants), locveil-reports (labels/bootstrap + protocol-check
  CI). All three were pin-validated at v1 (2026-07-11); since HK-13 all three hold a
  repin-stamped strict pin at `contracts/pins/report-protocol/` (locveil-reports joined
  the uniform layout at IMPL-21 — its hand-made root copy is gone).
- **Bump rules:** any consumer-visible change = new tag + STAMP bump; consumers re-pin,
  never patch their copies. Three levels (`process/contracts.md` §3): additive (new
  type/label) = minor; semantic change = major; bytes moved with no surface change = patch.
