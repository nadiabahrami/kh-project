"""Urls routes for main site."""
from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^about/$', TemplateView.as_view(template_name="base/about.html"), name="about"),
    url(r'^contact/$', TemplateView.as_view(template_name="base/contact.html"), name="contact"),
    url(r'^resources/$', TemplateView.as_view(template_name="base/resources.html"), name="resources"),
    url(r'^services/$', TemplateView.as_view(template_name="base/counseling.html"), name="counseling"),
    url(r'^$', TemplateView.as_view(template_name="base/index.html"), name="home"),
]
