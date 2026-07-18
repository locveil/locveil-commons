# locveil-core-py — shared Python core

The co-owned Python core (PROD-8, D-8; regime 2). First and so far only module:
**`entry_point_loader.py`** — the entry-point-group discovery engine extracted from
locveil-voice per the agreed design
`../../../locveil-voice/docs/design/core_py_loader_extraction.md` (§2 is the binding
surface; the PROD-8 council decisions bound its scope).

## Surface

One class, **`DynamicLoader`** — no module-level singleton; each consumer owns its
instance (the shared artifact is state-free). Python 3.11+, `importlib.metadata` only.

| Method | Semantics |
|---|---|
| `discover_providers(namespace, enabled=None, base_class=None)` | Load a group, cached by `(namespace, enabled, base_class)`; `base_class` rejects non-subclasses into the failure ledger |
| `get_provider_class(namespace, name, base_class=None)` | One class; group-cache hit or a **single-EP load** — siblings stay unimported |
| `list_available_providers(namespace)` | Names by loading (historical semantics) |
| `list_registered(namespace)` | Names **without importing** (startup validation, `dump_catalog`) |
| `get_discovery_failures(namespace)` | The per-namespace failure ledger (BUG-36): name → reason; success clears the entry |
| `clear_cache()` | Drops the class cache; the failure ledger persists until a success clears it |

## Consumption — vendored at a tag, strictly pinned

Versioned by prefixed tags **`core-py-vN`** (current: `core-py-v1` = 1.0.0). This is the
estate's first vendored **runtime** code, so convention-only discipline is not enough
(owner ruling, design §3): each consumer holds

- `contracts/pins/core-py/` — the pinned `entry_point_loader.py` + `PIN.json` (sha256) +
  README, registered in its `contracts/README.md` (contract-guard hash + TAG rules apply);
- an importable copy in its own tree, with a hermetic test asserting it is
  **byte-identical** to the pin. Never edit a vendored copy — changes happen here,
  re-tag, and consumers re-pin.

Consumers: voice (**ARCH-58** `[release]`), bridge (**CORE-7**, contract in design §5).

## What deliberately does NOT live here

Voice's `EntryPointMetadata` quartet + values, its `utils/namespaces.py` group registry
and aux helpers; bridge's by-name config resolver (`utils/class_loader.py`). Each
auxiliary graduates only on its own second consumer (rule of two). The logging-scheme
extraction (ARCH-43 → OPS-14) is PARKED by the council — loader first.

## Tests

```
cd packages/core-py && uv run --with pytest pytest tests/ -q
```

The behavior suite fakes the entry-point mechanism (duck-typed `.name`/`.load()`) to pin
the cache, ledger, and the three agreed deltas without throwaway distributions.
