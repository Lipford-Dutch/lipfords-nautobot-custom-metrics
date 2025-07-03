"""Unit tests for metrics helper functions."""

import importlib
import sys
import types

import pytest

pytest.importorskip("prometheus_client")
from prometheus_client.core import GaugeMetricFamily


def load_metrics():
    """Import the metrics module with a minimal Django shim."""
    # minimal django
    conf = types.ModuleType("django.conf")
    conf.settings = types.SimpleNamespace(
        VERSION="0",
        PLUGINS_CONFIG={"tns_custom_metrics": {"app_metrics": {}}},
        PLUGINS=[],
    )
    django_mod = types.ModuleType("django")
    django_mod.conf = conf
    django_mod.utils = types.ModuleType("django.utils")
    tz = types.ModuleType("django.utils.timezone")
    tz.now = lambda: 0
    tz.timedelta = lambda **kwargs: 0
    django_mod.utils.timezone = tz
    django_mod.db = types.ModuleType("django.db")
    django_mod.db.models = types.ModuleType("django.db.models")
    sys.modules["django"] = django_mod
    django_mod.db.models.Count = object
    django_mod.db.models.Avg = object
    django_mod.db.models.F = object
    sys.modules["django.conf"] = conf
    sys.modules["django.utils"] = django_mod.utils
    django_contrib = types.ModuleType("django.contrib")
    django_contrib.auth = types.ModuleType("django.contrib.auth")
    django_contrib.auth.models = types.ModuleType("django.contrib.auth.models")
    django_contrib.auth.models.AbstractUser = object
    sys.modules["django.contrib"] = django_contrib
    sys.modules["django.contrib.auth"] = django_contrib.auth
    sys.modules["django.contrib.auth.models"] = django_contrib.auth.models
    sys.modules["django.utils.timezone"] = tz
    sys.modules["django.db"] = django_mod.db
    sys.modules["django.db.models"] = django_mod.db.models

    nb_choices = types.ModuleType("nautobot.extras.choices")
    nb_choices.JobResultStatusChoices = [("ok", "ok")]
    sys.modules["nautobot.extras.choices"] = nb_choices
    nb_models = types.ModuleType("nautobot.extras.models")

    class JobResult: ...

    nb_models.JobResult = JobResult
    sys.modules["nautobot.extras.models"] = nb_models

    placeholder_models = types.ModuleType("tns_custom_metrics.models")
    for cls in [
        "APIRequest",
        "FeatureRelease",
        "FeatureUsage",
        "SessionRecord",
        "User",
        "UserInteraction",
    ]:
        setattr(placeholder_models, cls, type(cls, (), {}))
    sys.modules["tns_custom_metrics.models"] = placeholder_models

    if "tns_custom_metrics.metrics" in sys.modules:
        del sys.modules["tns_custom_metrics.metrics"]
    return importlib.import_module("tns_custom_metrics.metrics")


def test_collect_extras_metric():
    """Ensure extra metric functions are executed and collected."""
    mod = load_metrics()
    gauge = GaugeMetricFamily("x", "x")

    def good():
        return [gauge]

    def bad_iter():
        return "not_iter"

    metrics = list(mod.collect_extras_metric([good, bad_iter, "nope"]))
    assert gauge in metrics  # noqa: S101
