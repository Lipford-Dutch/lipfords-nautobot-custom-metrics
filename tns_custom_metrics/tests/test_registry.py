"""Test cases for tns_custom_metrics app metric function registry."""

import unittest

import pytest

pytest.importorskip("nautobot")

from tns_custom_metrics import __REGISTRY__, register_metric_func


class RegistryTests(unittest.TestCase):
    """Test cases for ensuring the registry is working properly."""

    def test_register_metric_func(self):
        """Ensure the function to add functions to the registry is working properly."""

        def myfunction():
            """Dummy metric function."""

        self.assertRaises(TypeError, register_metric_func, "test")
        self.assertRaises(TypeError, register_metric_func, {"test": "test"})
        self.assertRaises(TypeError, register_metric_func, [1, 2, 3])

        register_metric_func(myfunction)
        self.assertEqual(__REGISTRY__[-1], myfunction)
