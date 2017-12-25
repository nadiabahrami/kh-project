from django.conf.urls import url
from speaking.views import PresentationsList, PresentationDetail


urlpatterns = [
    url(r'^$', PresentationsList.as_view(), name="presentation_list"),
    url(r'^api/(?P<pk>[0-9]+)/', PresentationDetail.as_view(), name='presentation_detail')
]
