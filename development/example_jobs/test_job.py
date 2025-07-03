"""This script contains an example of a job about users."""

import time

import pytest
from django import setup as django_setup
from django.conf import settings

if not settings.configured:
    settings.configure(
        INSTALLED_APPS=["django.contrib.contenttypes", "django.contrib.auth"],
        ALLOWED_URL_SCHEMES=["http", "https"],
        ROOT_URLCONF="tns_custom_metrics.urls",
    )
    django_setup()

try:  # Skip if Nautobot isn't fully configured
    from nautobot.core.celery import register_jobs
    from nautobot.extras.jobs import BooleanVar, IntegerVar, Job
except Exception as exc:  # pragma: no cover - import side effects
    pytest.skip(f"Nautobot unavailable: {exc}", allow_module_level=True)


class TestJob(Job):
    """Job to test metrics with."""

    sleep = IntegerVar(description="How long this job should sleep.")
    fail = BooleanVar(description="Whether this job should fail.")

    def run(self, sleep, fail):
        """Run the job."""
        self.logger.warning(f"Sleeping {sleep} seconds.")
        time.sleep(sleep)
        if fail:
            raise ValueError("I am supposed to fail!")


register_jobs(TestJob)
