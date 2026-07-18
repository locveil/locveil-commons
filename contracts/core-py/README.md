# core-py — owned contract surface (cross-reference)

The vendored-runtime-code contract for the shared entry-point-group discovery engine
(PROD-8). The artifact keeps its importable home — **`../../packages/core-py/
entry_point_loader.py`** — per `../../process/contracts.md` §2 (owned surfaces that
legitimately live elsewhere keep it; this folder holds the STAMP + this pointer, the
registry indexes it).

- **Pinned set** (STAMP `artifacts`, complete by the pins-always-COMPLETE ruling):
  exactly `entry_point_loader.py`. The package's tests, `pyproject.toml`, and README are
  owner-side tooling and never travel.
- **Consumption** (binding, design §3): each consumer holds `contracts/pins/core-py/`
  (artifact copy + this STAMP verbatim + `PIN.json` with sha256) AND an importable copy
  in its own tree with a hermetic byte-identity test against the pin. Never edit a
  vendored copy — changes happen in `packages/core-py/`, re-tag `core-py-vN`, re-pin.
- **Version authority**: `STAMP.json` + tag `core-py-v1.1` (v1's tree predates this
  STAMP — v1.1 is the packaging correction, artifact bytes unchanged). Semantics/behavior
  questions: the design doc `../../../locveil-voice/docs/design/core_py_loader_extraction.md`
  and the behavior suite `../../packages/core-py/tests/`.

Consumers: locveil-voice (ARCH-58 `[release]`), locveil-bridge (CORE-7, §5 adoption
contract).
