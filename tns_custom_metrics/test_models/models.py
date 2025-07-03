# Reference: NAC-1725, Sprint 37
# ------------------------- models.py (Reviewed) -------------------------
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class User(AbstractUser):
    """
    Extended user model with team, role, and organization.
    """
    team = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    organization = models.CharField(max_length=100, blank=True)
    groups = models.ManyToManyField(
        Group,
        related_name="tns_custom_metrics_test_user_groups",
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="tns_custom_metrics_test_user_permissions",
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["team", "username"]

    def __str__(self):
        return f"{self.username} ({self.team})"

class UserInteraction(models.Model):
    """
    Logs each user event: UI click, API call, or login.
    Includes device metadata and module context.
    """
    EVENT_UI = 'ui'
    EVENT_API = 'api'
    EVENT_LOGIN = 'login'

    EVENT_TYPES = [
        (EVENT_UI, 'UI Interaction'),
        (EVENT_API, 'API Call'),
        (EVENT_LOGIN, 'User Login'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='interactions')
    timestamp = models.DateTimeField(auto_now_add=True)
    event_type = models.CharField(max_length=10, choices=EVENT_TYPES)
    device_vendor = models.CharField(max_length=50, null=True, blank=True)
    device_type = models.CharField(max_length=50, null=True, blank=True)
    module = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['timestamp']),
            models.Index(fields=['user', 'event_type']),
        ]
        ordering = ['-timestamp']
        verbose_name = 'User Interaction'
        verbose_name_plural = 'User Interactions'

    def __str__(self):
        return f"{self.user.username} {self.event_type} at {self.timestamp.isoformat()}"

class SessionRecord(models.Model):
    """
    Tracks the start and end of a user session.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sessions')
    start = models.DateTimeField()
    end = models.DateTimeField()

    class Meta:
        indexes = [models.Index(fields=['start', 'end']),]
        verbose_name = 'Session Record'
        verbose_name_plural = 'Session Records'

    def __str__(self):
        duration = self.end - self.start
        return f"Session for {self.user.username}: {duration.total_seconds()}s"

class FeatureRelease(models.Model):
    """
    Records each feature release date for adoption tracking.
    """
    name = models.CharField(max_length=100, unique=True)
    release_date = models.DateTimeField()

    class Meta:
        ordering = ['-release_date']
        verbose_name = 'Feature Release'
        verbose_name_plural = 'Feature Releases'

    def __str__(self):
        return f"{self.name} released on {self.release_date.date()}"

class FeatureUsage(models.Model):
    """
    Logs each feature invocation by a user.
    Module field ties usage to app context.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feature_usages')
    feature_name = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    module = models.CharField(max_length=100)

    class Meta:
        indexes = [models.Index(fields=['feature_name', 'timestamp']),]
        verbose_name = 'Feature Usage'
        verbose_name_plural = 'Feature Usages'

    def __str__(self):
        return f"{self.user.username} used {self.feature_name} at {self.timestamp.isoformat()}"

class APIRequest(models.Model):
    """
    Logs each API request call for endpoint usage metrics.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='api_requests')
    endpoint = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [models.Index(fields=['endpoint', 'timestamp']),]
        verbose_name = 'API Request'
        verbose_name_plural = 'API Requests'

    def __str__(self):
        return f"{self.user.username} called {self.endpoint} at {self.timestamp.isoformat()}"
