"""Urls routes for main site."""
from django.conf.urls import url, include
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^about/$', TemplateView.as_view(template_name="about.html"), name="about"),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^contact/$', TemplateView.as_view(template_name="contact.html"), name="contact"),
    url(r'^resources/$', TemplateView.as_view(template_name="resources.html"), name="resources"),
    url(r'^services/$', TemplateView.as_view(template_name="services.html"), name="services"),
    url(r'^coaching/$', TemplateView.as_view(template_name="coaching.html"), name="coaching"),
    url(r'^speaking/$', TemplateView.as_view(template_name="speaking.html"), name="speaking"),
    url(r'^$', TemplateView.as_view(template_name="index.html"), name="home"),
]
