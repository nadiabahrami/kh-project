"""Url patterns for the group_coaching app."""
from django.conf.urls import url
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="coaching.html"), name="coaching"),
]
