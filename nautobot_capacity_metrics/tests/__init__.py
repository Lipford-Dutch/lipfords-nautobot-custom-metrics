"""Unit tests for nautobot_capacity_metrics app."""

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
            "nautobot_capacity_metrics",
        ],
        DATABASES={"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}},
        ROOT_URLCONF="nautobot_capacity_metrics.urls",
        ALLOWED_URL_SCHEMES=["http", "https"],
        USE_TZ=True,
    )

    import django

    django.setup()
