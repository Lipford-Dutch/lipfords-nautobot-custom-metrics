"""Unit tests for tns_custom_metrics.__init__."""

import importlib
import sys
import types

import pytest

pytestmark = pytest.mark.unit


def import_init():
    """Import ``tns_custom_metrics.__init__`` with a dummy Nautobot module."""
    dummy_nautobot = types.ModuleType("nautobot")
    apps = types.ModuleType("nautobot.apps")

    class DummyConfig:
        pass

    apps.NautobotAppConfig = DummyConfig
    dummy_nautobot.apps = apps
    sys.modules["nautobot"] = dummy_nautobot
    sys.modules["nautobot.apps"] = apps
    if "tns_custom_metrics.__init__" in sys.modules:
        del sys.modules["tns_custom_metrics.__init__"]
    return importlib.import_module("tns_custom_metrics.__init__")


@pytest.fixture()
def metrics_module():
    """Return the freshly imported module under test."""
    return import_init()


def test_register_metric_func_valid(metrics_module):
    """Verify that ``register_metric_func`` adds the callable to the registry."""
    mod = metrics_module
    called = []

    def func():
        called.append(True)

    mod.register_metric_func(func)
    assert mod.__REGISTRY__[-1] is func  # noqa: S101


@pytest.mark.parametrize("val", [123, "x", object()])
def test_register_metric_func_invalid(metrics_module, val):
    """Ensure ``register_metric_func`` rejects non-callables."""
    mod = metrics_module
    with pytest.raises(TypeError):
        mod.register_metric_func(val)
