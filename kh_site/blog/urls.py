"""Urls routes for main site."""
from django.conf.urls import url
from blog.views import add_article, blog_view, edit_article
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^add/', login_required(add_article), name='add_bpost'),
    url(r'^edit/(?P<pk>[0-9]+)/', login_required(edit_article), name='edit_bpost'),
    url(r'^$', blog_view, name="blog"),
]
