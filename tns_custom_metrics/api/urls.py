"""Django URL patterns for tns_custom_metrics app."""

from django.urls import path

from . import views

urlpatterns = [
    path("app-metrics", views.AppMetricsView, name="tns_custom_metrics_app_view"),
]
