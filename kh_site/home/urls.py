"""Urls routes for main site."""
from django.conf.urls import include, url
from django.views.generic import TemplateView

#TODO: create view and plug here for home route
urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="index.html")),
]

