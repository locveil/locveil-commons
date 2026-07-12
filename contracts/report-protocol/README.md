# report-protocol — the shared inbox truth (owned, machine core)

The machine half of the problem-reports contract (HK-3/PROD-6): labels + colors, lenses,
ticket **types** (first-class — a future type is a vN bump, not a redesign), the typed
state machine (`ping_pong_max`), title prefixes, bundle path, handover schema, slug
registry. The prose half — choreography, leak fence, retention, lens co-ownership — is
[`process/problem-reports.md`](../../process/problem-reports.md); on shared vocabulary the
machine core defines, the prose points here.

- **Artifact:** [`report-protocol.json`](report-protocol.json)
- **Version:** `STAMP.json` + tag (`report-protocol-v1`) — the stamp defines, changelogs
  narrate (`process/contracts.md` §3). The in-artifact `version` field arrives at v2.
- **Consumers (pin + conformance test each):** locveil-voice (`/report` collector),
  locveil-bridge (filing constants), locveil-reports (labels/bootstrap + protocol-check
  CI). All three were pin-validated at `report-protocol-v1` (2026-07-11).
- **Bump rules:** any consumer-visible change = new tag + STAMP bump; consumers re-pin,
  never patch their copies. Additive (new type/label) = minor; semantic change = major.
