"""Models used solely for exercising the app-metric model-count mechanics in tests.

This module intentionally defines a single trivial model. It exists so the
``metric_models`` collector has a concrete, app-local model to count during the
development/test environment. It must stay in sync with
``migrations/0001_initial.py`` (UUID primary key + ``name`` char field).
"""

from django.db import models
from nautobot.apps.models import BaseModel


class TestModel(BaseModel):
    """Trivial model used to validate the ``nautobot_model_count`` metric."""

    name = models.CharField(max_length=20)

    def __str__(self):
        """Return the model's name."""
        return self.name
