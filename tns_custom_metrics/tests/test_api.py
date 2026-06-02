"""Unit tests for tns_custom_metrics."""

import pytest

pytest.importorskip("nautobot")

from django.conf import settings

if not hasattr(settings, "CELERY_TASK_DEFAULT_QUEUE"):
    pytest.skip("Celery not configured", allow_module_level=True)

User = get_user_model()


class PlaceholderAPITest(APITestCase):
    """Test the NautobotCapacityMetrics API."""

    def setUp(self):
        """Create a superuser and token for API calls."""
        self.user = UserFactory()
        self.token = TokenFactory(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")

    def test_placeholder(self):
        """Verify that devices can be listed."""
        url = reverse("dcim-api:device-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 0)
