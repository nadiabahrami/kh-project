"""Urls routes for main site."""
from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^about/$', TemplateView.as_view(template_name="about.html"), name="about"),
    url(r'^blog/$', TemplateView.as_view(template_name="blog.html"), name="blog"),
    url(r'^$', TemplateView.as_view(template_name="index.html"), name="home"),
]
