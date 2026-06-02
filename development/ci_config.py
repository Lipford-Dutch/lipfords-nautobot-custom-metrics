"""Minimal Nautobot settings used for CI (system checks, migrations, unit tests).

This configuration deliberately keeps Nautobot's default ``MIDDLEWARE`` and uses
a permissive ``ALLOWED_HOSTS`` so the Django/DRF test client host ("testserver")
is accepted during ``nautobot-server test``. It is **not** intended for
production use -- the development/runtime configuration is
``development/nautobot_config.py``.
"""

import os

from nautobot.core.settings import *  # noqa: F403
from nautobot.core.settings_funcs import is_truthy  # noqa: F401

# Permissive so the test client's "testserver" host is accepted.
ALLOWED_HOSTS = ["*"]
SECRET_KEY = os.getenv("NAUTOBOT_SECRET_KEY", "ci-only-not-a-secret-key-0123456789abcdef")

DATABASES = {
    "default": {
        "NAME": os.getenv("NAUTOBOT_DB_NAME", "nautobot"),
        "USER": os.getenv("NAUTOBOT_DB_USER", "nautobot"),
        "PASSWORD": os.getenv("NAUTOBOT_DB_PASSWORD", "nautobot"),
        "HOST": os.getenv("NAUTOBOT_DB_HOST", "localhost"),
        "PORT": os.getenv("NAUTOBOT_DB_PORT", "5432"),
        "CONN_MAX_AGE": 300,
        "ENGINE": "django.db.backends.postgresql",
    }
}

# Enable the app. The test-only model app is registered as a plain Django app
# (not a PLUGINS entry) because Nautobot 3.x resolves PLUGINS entries by Django
# app label, which would not match this nested app's dotted module path.
PLUGINS = [
    "tns_custom_metrics",
]
INSTALLED_APPS.append("tns_custom_metrics.test_models.TestConfig")  # noqa: F405

PLUGINS_CONFIG = {
    "tns_custom_metrics": {
        "app_metrics": {
            "gitrepositories": True,
            "jobs": True,
            "models": {
                "dcim": {"Location": True, "Rack": True, "Device": True},
                "ipam": {"IPAddress": True, "Prefix": True},
                "test_models": {"_module": "tns_custom_metrics", "TestModel": True},
            },
            "queues": True,
            "versions": {"basic": True, "plugins": True},
        }
    },
}
