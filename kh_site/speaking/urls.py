from django.conf.urls import url
from speaking.views import PresentationsList


urlpatterns = [
    url(r'^$', PresentationsList.as_view(), name="presentation_list")
]
