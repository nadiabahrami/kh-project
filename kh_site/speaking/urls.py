from django.conf.urls import url
from speaking.views import (
    PresentationsList,
    PresentationsJSONList,
    PresentationDetail
)


urlpatterns = [
    url(r'^$', PresentationsList.as_view(), name="presentation_list"),
    url(r'^api/list/$', PresentationsJSONList.as_view(), name="presentation_json_list"),
    url(r'^api/detail/(?P<pk>[0-9]+)/$', PresentationDetail.as_view(), name='presentation_detail')
]
