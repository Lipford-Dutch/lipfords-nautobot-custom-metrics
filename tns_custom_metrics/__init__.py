"""App declaration for tns_custom_metrics."""

# Metadata is inherited from Nautobot. If not including Nautobot in the environment, this should be added
from importlib import metadata
from importlib.metadata import PackageNotFoundError
from typing import Callable

try:
    from nautobot.apps import NautobotAppConfig
except ModuleNotFoundError:  # pragma: no cover - allow tests without Nautobot

    class NautobotAppConfig:  # type: ignore[too-few-public-methods]
        """Fallback placeholder when Nautobot isn't installed."""

        pass


try:
    __version__ = metadata.version(__name__)
except PackageNotFoundError:  # pragma: no cover - fallback for tests
    __version__ = "0.0.0"

# Registry of functions that can generate additional application metrics
# All functions in the registry should take no argument and return an Iterator (or list) of prometheus Metric Object
# The Registry can be populated from the configuration file or using register_metric_func()
__REGISTRY__ = []


def register_metric_func(func: Callable):
    """Register an additional function to generate application metrics.

    Args:
        func (Callable): python function, taking no argument that return a list of Prometheus Metric Object
    """
    if not callable(func):
        raise TypeError(
            f"Trying to register a {type(func)} into the application metric registry, only function (callable) are supporter"
        )

    __REGISTRY__.append(func)


class TnsCustomMetricsConfig(NautobotAppConfig):
    """App configuration for the tns_custom_metrics app."""

    name = "tns_custom_metrics"
    verbose_name = "Data, Metrics, and Monitoring Prometheus Endpoints"
    version = __version__
    author = "Network to Code, LLC"
    description = "Lightweight Nautobot App to expose additional metrics as Prometheus endpoints. Includes exposing Nautobot object data and metrics that can be collected and later viewed in Visualization tools."
    base_url = "capacity-metrics"
    required_settings = []
    min_version = "3.1.0"
    max_version = "3.9999"
    default_settings = {
        "app_metrics": {
            "models": {
                "dcim": {
                    "Location": True,
                    "Rack": True,
                    "Device": True,
                },
                "ipam": {"IPAddress": True, "Prefix": True},
            },
            "jobs": True,
            "queues": True,
            "versions": {
                "basic": False,
                "plugins": False,
            },
        }
    }
    caching_config = {}
    docs_view_name = "plugins:tns_custom_metrics:docs"


config = TnsCustomMetricsConfig  # pylint:disable=invalid-name
