# Reference: NAC-1725, Sprint 37
# ------------------------- models.py -------------------------
from django.db import models
from django.contrib.auth.models import AbstractUser
# Nautobot imports
from nautobot.apps.models import PrimaryModel, extras_features

# If you want to choose a specific model to overload in your class declaration, please reference the following documentation:
# how to chose a database model: https://docs.nautobot.com/projects/core/en/stable/plugins/development/#database-models
# If you want to use the extras_features decorator please reference the following documentation
# https://docs.nautobot.com/projects/core/en/stable/development/core/model-checklist/#extras-features
@extras_features("custom_links", "custom_validators", "export_templates", "graphql", "webhooks")
class {{ cookiecutter.model_class_name }}(PrimaryModel):  # pylint: disable=too-many-ancestors
    """Base model for {{ cookiecutter.verbose_name }} app."""

    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=200, blank=True)
    # additional model fields

    class Meta:
        """Meta class."""

        ordering = ["name"]

        # Option for fixing capitalization (i.e. "Snmp" vs "SNMP")
        # verbose_name = "{{ cookiecutter.verbose_name }}"

        # Option for fixing plural name (i.e. "Chicken Tenders" vs "Chicken Tendies")
        # verbose_name_plural = "{{ cookiecutter.verbose_name }}s"

    def __str__(self):
        """Stringify instance."""
        return self.name

class User(AbstractUser):
    team = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    # add additional fields as needed (e.g., organization)

class UserInteraction(models.Model):
    EVENT_TYPES = [
        ('ui', 'UI Interaction'),
        ('api', 'API Call'),
        ('login', 'User Login'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    event_type = models.CharField(max_length=10, choices=EVENT_TYPES)
    device_vendor = models.CharField(max_length=50, null=True, blank=True)
    device_type = models.CharField(max_length=50, null=True, blank=True)
    module = models.CharField(max_length=100, null=True, blank=True)

class SessionRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField()

class FeatureRelease(models.Model):
    name = models.CharField(max_length=100)
    release_date = models.DateTimeField()

class FeatureUsage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feature_name = models.CharField(max_length=100)
    timestamp = models.DateTimeField()
    module = models.CharField(max_length=100)

class APIRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    endpoint = models.CharField(max_length=200)
    timestamp = models.DateTimeField()
