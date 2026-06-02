"""Smoke tests for the Nautobot REST API with tns_custom_metrics installed."""

import pytest
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .factories import TokenFactory, UserFactory

pytestmark = pytest.mark.integration


class PlaceholderAPITest(TestCase):
    """Verify the Nautobot REST API responds correctly while the app is installed."""

    def setUp(self):
        """Create a superuser and token for API calls."""
        self.user = UserFactory()
        self.token = TokenFactory(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")

    def test_list_devices(self):
        """Verify that devices can be listed."""
        url = reverse("dcim-api:device-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 0)
