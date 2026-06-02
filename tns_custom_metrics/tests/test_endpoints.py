"""Test cases for tns_custom_metrics views."""

import pytest
from django.test import TestCase
from django.urls import reverse
from rest_framework import status

pytestmark = pytest.mark.integration


class AppMetricEndpointTests(TestCase):
    """Test cases for ensuring application metric endpoint is working properly."""

    def setUp(self):
        """Resolve the app-metrics endpoint URL for each test."""
        self.app_metric_url = reverse("plugins-api:tns_custom_metrics-api:tns_custom_metrics_app_view")

    def test_endpoint(self):
        """Ensure the endpoint is working properly and is not protected by authentication."""
        resp = self.client.get(self.app_metric_url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_model_count_metrics(self):
        """Ensure that the model count metrics work correctly."""
        resp = self.client.get(self.app_metric_url)
        if "TestModel" not in resp.content.decode("utf-8"):
            self.fail("tns_custom_metrics.test_models.models.TestModel does not report its count.")
