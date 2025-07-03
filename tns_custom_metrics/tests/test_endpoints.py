"""Test cases for tns_custom_metrics views."""

import pytest

pytest.importorskip("nautobot")

from django.test import TestCase
from django.urls import NoReverseMatch, reverse
from rest_framework import status
from rest_framework.test import APIClient

try:
    APP_METRIC_URL = reverse(
        "plugins-api:tns_custom_metrics-api:tns_custom_metrics_app_view"
    )
except NoReverseMatch:
    pytest.skip("Nautobot plugin API not configured", allow_module_level=True)


class AppMetricEndpointTests(TestCase):
    """Test cases for ensuring application metric endpoint is working properly."""

    app_metric_url = APP_METRIC_URL

    def test_endpoint(self):
        """Ensure the endpoint is working properly and is not protected by authentication."""
        client = APIClient()
        resp = client.get(self.app_metric_url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_model_count_metrics(self):
        """Ensure that the model count metrics work correctly."""
        resp = self.client.get(self.app_metric_url)
        if "TestModel" not in resp.content.decode("utf-8"):
            self.fail(
                "tns_custom_metrics.test_models.models.TestModel does not report its count."
            )
