"""Test cases for tns_custom_metrics app metric function registry."""

import pytest

pytestmark = [pytest.mark.unit]

pytest.importorskip("nautobot")

from tns_custom_metrics import __REGISTRY__, register_metric_func  # noqa: E402


def test_register_metric_func():
    """Ensure functions can be registered and invalid types are rejected."""

    def myfunction():
        """Dummy metric function."""

    with pytest.raises(TypeError):
        register_metric_func("test")
    with pytest.raises(TypeError):
        register_metric_func({"test": "test"})
    with pytest.raises(TypeError):
        register_metric_func([1, 2, 3])

    register_metric_func(myfunction)
    assert __REGISTRY__[-1] is myfunction
