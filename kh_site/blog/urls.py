"""Urls routes for main site."""
from django.conf.urls import url
from blog.views import add_article, blog_view, edit_article, delete_article
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^add/', login_required(add_article), name='add_bpost'),
    url(r'^edit/(?P<pk>[0-9]+)/', login_required(edit_article), name='edit_bpost'),
    url(r'^$', blog_view, name="blog"),
    url(r'^delete/(?P<pk>[0-9]+)/', login_required(delete_article), name='delete_bpost'),
    url(r'^(?P<pk>\d+)/$', blog_view, name="blog_detail_pk"),
    url(r'^(?P<slug>[\w\-\_]+)/$', blog_view, name="blog_detail_slug"),
]
