"""Django urlpatterns declaration for tns_custom_metrics app."""

from django.templatetags.static import static
from django.urls import path
from django.views.generic import RedirectView

urlpatterns = [
    path("docs/", RedirectView.as_view(url=static("tns_custom_metrics/docs/index.html")), name="docs"),
]
