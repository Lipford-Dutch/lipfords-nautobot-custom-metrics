# Reference: NAC-1725, Sprint 37
# ------------------------- models.py -------------------------
from django.db import models
from django.contrib.auth.models import AbstractUser

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
