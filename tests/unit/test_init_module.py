"""Unit tests for tns_custom_metrics.__init__."""
import importlib
import sys
import types

import pytest


def import_init():
    dummy_nautobot = types.ModuleType("nautobot")
    apps = types.ModuleType("nautobot.apps")
    class DummyConfig:
        pass
    apps.NautobotAppConfig = DummyConfig
    dummy_nautobot.apps = apps
    sys.modules['nautobot'] = dummy_nautobot
    sys.modules['nautobot.apps'] = apps
    if 'tns_custom_metrics.__init__' in sys.modules:
        del sys.modules['tns_custom_metrics.__init__']
    return importlib.import_module('tns_custom_metrics.__init__')


def test_register_metric_func_valid():
    mod = import_init()
    called = []
    def func():
        called.append(True)
    mod.register_metric_func(func)
    assert mod.__REGISTRY__[-1] is func


@pytest.mark.parametrize('val', [123, 'x', object()])
def test_register_metric_func_invalid(val):
    mod = import_init()
    with pytest.raises(TypeError):
        mod.register_metric_func(val)
