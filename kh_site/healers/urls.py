"""Healer app urls."""
from django.conf.urls import url
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^play/$', TemplateView.as_view(template_name="play.html"), name="play"),
    url(r'^dance/$', TemplateView.as_view(template_name="beyonce.html"), name="beyonce"),
    url(r'^coaching/$', TemplateView.as_view(template_name="coaching.html"), name="coaching"),
    url(r'^$', TemplateView.as_view(template_name="healers.html"), name="healers"),
]
