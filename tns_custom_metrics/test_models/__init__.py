"""App declaration for tns_custom_metrics.test_models.

Why is this here? In order to test the app model count metric mechanics, a app metric had to be introduced.
This was put into a separate app so that it is not installed whenever this app is installed, rather just when tests
are ran within this apps development environment.
"""

__version__ = "1.0.0"

from nautobot.apps import NautobotAppConfig


class TestConfig(NautobotAppConfig):
    """App configuration for the tns_custom_metrics app."""

    name = "tns_custom_metrics.test_models"
    verbose_name = "Metrics & Monitoring Extension Test Model App"
    version = __version__
    author = "Network to Code, LLC"
    author_email = "opensource@networktocode.com"
    description = "App that exists solely to test tns_custom_metrics, don't install.."
    base_url = "capacity-metrics-test"
    required_settings = []
    min_version = "2.0.0"
    max_version = "2.9999"
    default_settings = {}
    caching_config = {}


config = TestConfig  # pylint:disable=invalid-name
