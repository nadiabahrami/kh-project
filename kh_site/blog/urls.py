"""Urls routes for main site."""
from django.conf.urls import url
from django.views.generic import TemplateView
from blog.views import add_article, blog_view
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^add/', login_required(add_article), name='add_bpost'),
    url(r'^$', blog_view, name="blog"),
]
