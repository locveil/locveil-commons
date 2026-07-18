"""Behavior suite for the shared DynamicLoader (PROD-8; binding surface: voice design
`core_py_loader_extraction.md` §2).

The entry-point mechanism is faked with duck-typed objects — the loader only touches
``.name`` and ``.load()`` — so the semantics (cache, failure ledger, the three agreed
deltas) are pinned without building throwaway distributions.
"""

import pytest

import entry_point_loader
from entry_point_loader import DynamicLoader


class Base:
    pass


class Good(Base):
    pass


class AlsoGood(Base):
    pass


class NotASubclass:
    pass


class FakeEP:
    def __init__(self, name, obj=None, exc=None):
        self.name = name
        self._obj = obj
        self._exc = exc
        self.load_count = 0

    def load(self):
        self.load_count += 1
        if self._exc is not None:
            raise self._exc
        return self._obj


def install(monkeypatch, groups):
    """Point the module's entry_points at a fake registry; returns a call counter."""
    calls = {"n": 0}

    def fake_entry_points(*, group):
        calls["n"] += 1
        return list(groups.get(group, []))

    monkeypatch.setattr(entry_point_loader, "entry_points", fake_entry_points)
    return calls


def break_mechanism(monkeypatch):
    def broken_entry_points(*, group):
        raise RuntimeError("discovery mechanism down")

    monkeypatch.setattr(entry_point_loader, "entry_points", broken_entry_points)


# --- discover_providers: faithful semantics ---


def test_discover_loads_group(monkeypatch):
    install(monkeypatch, {"ns": [FakeEP("a", Good), FakeEP("b", AlsoGood)]})
    loader = DynamicLoader()
    assert loader.discover_providers("ns") == {"a": Good, "b": AlsoGood}


def test_enabled_filters_and_empty_list_means_no_filter(monkeypatch):
    install(monkeypatch, {"ns": [FakeEP("a", Good), FakeEP("b", AlsoGood)]})
    loader = DynamicLoader()
    assert loader.discover_providers("ns", enabled=["a"]) == {"a": Good}
    assert loader.discover_providers("ns", enabled=[]) == {"a": Good, "b": AlsoGood}


def test_cache_hit_skips_rediscovery(monkeypatch):
    ep = FakeEP("a", Good)
    calls = install(monkeypatch, {"ns": [ep]})
    loader = DynamicLoader()
    loader.discover_providers("ns")
    loader.discover_providers("ns")
    assert calls["n"] == 1
    assert ep.load_count == 1


def test_cache_key_separates_enabled_and_base_class(monkeypatch):
    install(monkeypatch, {"ns": [FakeEP("a", Good), FakeEP("b", NotASubclass)]})
    loader = DynamicLoader()
    assert set(loader.discover_providers("ns")) == {"a", "b"}
    assert set(loader.discover_providers("ns", enabled=["a"])) == {"a"}
    assert set(loader.discover_providers("ns", base_class=Base)) == {"a"}


def test_clear_cache_forces_rediscovery(monkeypatch):
    calls = install(monkeypatch, {"ns": [FakeEP("a", Good)]})
    loader = DynamicLoader()
    loader.discover_providers("ns")
    loader.clear_cache()
    loader.discover_providers("ns")
    assert calls["n"] == 2


def test_broken_mechanism_degrades_to_empty_and_is_not_cached(monkeypatch):
    break_mechanism(monkeypatch)
    loader = DynamicLoader()
    assert loader.discover_providers("ns") == {}
    install(monkeypatch, {"ns": [FakeEP("a", Good)]})
    assert loader.discover_providers("ns") == {"a": Good}


# --- the failure ledger (BUG-36) ---


def test_import_failure_recorded_by_name(monkeypatch):
    install(monkeypatch, {"ns": [FakeEP("bad", exc=ImportError("no such module"))]})
    loader = DynamicLoader()
    assert loader.discover_providers("ns") == {}
    failures = loader.get_discovery_failures("ns")
    assert failures["bad"].startswith("import failed:")


def test_generic_load_failure_recorded_by_name(monkeypatch):
    install(monkeypatch, {"ns": [FakeEP("bad", exc=ValueError("boom"))]})
    loader = DynamicLoader()
    loader.discover_providers("ns")
    assert loader.get_discovery_failures("ns")["bad"].startswith("load failed:")


def test_success_clears_failure_entry(monkeypatch):
    install(monkeypatch, {"ns": [FakeEP("a", exc=ImportError("transient"))]})
    loader = DynamicLoader()
    loader.discover_providers("ns")
    assert "a" in loader.get_discovery_failures("ns")
    install(monkeypatch, {"ns": [FakeEP("a", Good)]})
    loader.clear_cache()
    assert loader.discover_providers("ns") == {"a": Good}
    assert "a" not in loader.get_discovery_failures("ns")


def test_get_discovery_failures_returns_a_copy(monkeypatch):
    install(monkeypatch, {"ns": [FakeEP("bad", exc=ImportError("x"))]})
    loader = DynamicLoader()
    loader.discover_providers("ns")
    loader.get_discovery_failures("ns").clear()
    assert "bad" in loader.get_discovery_failures("ns")


# --- delta 1: base_class validation ---


def test_base_class_rejection_goes_to_the_ledger(monkeypatch):
    install(monkeypatch, {"ns": [FakeEP("good", Good), FakeEP("stray", NotASubclass)]})
    loader = DynamicLoader()
    assert loader.discover_providers("ns", base_class=Base) == {"good": Good}
    assert loader.get_discovery_failures("ns")["stray"] == "not a Base subclass"


def test_base_class_rejects_non_type_objects(monkeypatch):
    install(monkeypatch, {"ns": [FakeEP("obj", object())]})
    loader = DynamicLoader()
    assert loader.discover_providers("ns", base_class=Base) == {}
    assert loader.get_discovery_failures("ns")["obj"] == "not a Base subclass"


# --- delta 2: single-EP get_provider_class ---


def test_get_provider_class_answers_from_group_cache(monkeypatch):
    install(monkeypatch, {"ns": [FakeEP("a", Good)]})
    loader = DynamicLoader()
    loader.discover_providers("ns")
    break_mechanism(monkeypatch)
    assert loader.get_provider_class("ns", "a") is Good


def test_get_provider_class_does_not_import_siblings(monkeypatch):
    sibling = FakeEP("sibling", AlsoGood)
    install(monkeypatch, {"ns": [FakeEP("a", Good), sibling]})
    loader = DynamicLoader()
    assert loader.get_provider_class("ns", "a") is Good
    assert sibling.load_count == 0


def test_get_provider_class_unknown_name_is_none_not_a_failure(monkeypatch):
    install(monkeypatch, {"ns": [FakeEP("a", Good)]})
    loader = DynamicLoader()
    assert loader.get_provider_class("ns", "ghost") is None
    assert "ghost" not in loader.get_discovery_failures("ns")


def test_get_provider_class_records_individual_failure(monkeypatch):
    install(monkeypatch, {"ns": [FakeEP("bad", exc=ImportError("nope")), FakeEP("a", Good)]})
    loader = DynamicLoader()
    assert loader.get_provider_class("ns", "bad") is None
    assert loader.get_discovery_failures("ns")["bad"].startswith("import failed:")
    assert loader.get_provider_class("ns", "a") is Good


def test_get_provider_class_applies_base_class(monkeypatch):
    install(monkeypatch, {"ns": [FakeEP("stray", NotASubclass)]})
    loader = DynamicLoader()
    assert loader.get_provider_class("ns", "stray", base_class=Base) is None
    assert loader.get_discovery_failures("ns")["stray"] == "not a Base subclass"


def test_get_provider_class_broken_mechanism_is_none(monkeypatch):
    break_mechanism(monkeypatch)
    loader = DynamicLoader()
    assert loader.get_provider_class("ns", "a") is None


# --- delta 3: list_registered (names without importing) ---


def test_list_registered_names_without_loading(monkeypatch):
    eps = [FakeEP("a", Good), FakeEP("b", exc=ImportError("would explode if loaded"))]
    install(monkeypatch, {"ns": eps})
    loader = DynamicLoader()
    assert loader.list_registered("ns") == ["a", "b"]
    assert all(ep.load_count == 0 for ep in eps)


def test_list_registered_broken_mechanism_is_empty(monkeypatch):
    break_mechanism(monkeypatch)
    loader = DynamicLoader()
    assert loader.list_registered("ns") == []


# --- historical loading semantics kept alongside ---


def test_list_available_providers_loads(monkeypatch):
    eps = [FakeEP("a", Good)]
    install(monkeypatch, {"ns": eps})
    loader = DynamicLoader()
    assert loader.list_available_providers("ns") == ["a"]
    assert eps[0].load_count == 1


# --- the shared artifact is state-free ---


def test_no_module_level_singleton():
    assert not hasattr(entry_point_loader, "dynamic_loader")


def test_real_importlib_metadata_path():
    """Unpatched smoke: the real entry_points() answers for a group that exists everywhere."""
    loader = DynamicLoader()
    names = loader.list_registered("console_scripts")
    assert isinstance(names, list)
