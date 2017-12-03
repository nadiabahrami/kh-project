from django.views.generic import ListView
from speaking.models import Presentation

# Create your views here.


class PresentationsList(ListView):
    model = Presentation
    context_object_name = 'presentations'
    template_name = "speaking/speaking.html"
