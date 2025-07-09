"""Unit tests for tns_custom_metrics app."""

import os
import pkgutil

import pytest

if not (pkgutil.find_loader("django") and pkgutil.find_loader("nautobot")):
    pytest.skip("Django or Nautobot not installed", allow_module_level=True)

os.environ.setdefault("NAUTOBOT_TEST_USE_FACTORIES", "true")

from django.conf import settings

if not settings.configured:
    settings.configure(
        SECRET_KEY="testing",
        INSTALLED_APPS=[
            "django.contrib.contenttypes",
            "django.contrib.auth",
            "django.contrib.sessions",
            "rest_framework",
            "nautobot.users",
            "nautobot.extras",
            "tns_custom_metrics",
        ],
        DATABASES={
            "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}
        },
        ROOT_URLCONF="tns_custom_metrics.urls",
        ALLOWED_URL_SCHEMES=["http", "https"],
        USE_TZ=True,
    )

    import django

    django.setup()
