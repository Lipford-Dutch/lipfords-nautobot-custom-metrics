"""Test cases for tns_custom_metrics app metric function registry."""

import unittest

from tns_custom_metrics import __REGISTRY__, register_metric_func


class RegisterMetricFuncTestCase(unittest.TestCase):
    """Ensure functions can be registered and invalid types are rejected."""

    def test_register_metric_func(self):
        """Functions can be registered; non-callables raise ``TypeError``."""

        def myfunction():
            """Dummy metric function."""

        for invalid in ("test", {"test": "test"}, [1, 2, 3]):
            with self.assertRaises(TypeError):
                register_metric_func(invalid)

        register_metric_func(myfunction)
        self.assertIs(__REGISTRY__[-1], myfunction)
