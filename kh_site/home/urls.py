"""Urls routes for main site."""
from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^about/$', TemplateView.as_view(template_name="about.html"), name="about"),
    url(r'^blog/$', TemplateView.as_view(template_name="blog.html"), name="blog"),
    url(r'^contact/$', TemplateView.as_view(template_name="contact.html"), name="contact"),
    url(r'^resources/$', TemplateView.as_view(template_name="resources.html"), name="resources"),
    url(r'^faq/$', TemplateView.as_view(template_name="faq.html"), name="faq"),
    url(r'^services/$', TemplateView.as_view(template_name="services.html"), name="services"),
    url(r'^speaking/$', TemplateView.as_view(template_name="speaking.html"), name="speaking"),
    url(r'^healers/$', TemplateView.as_view(template_name="healers.html"), name="healers"),
    url(r'^$', TemplateView.as_view(template_name="index.html"), name="home"),
]
