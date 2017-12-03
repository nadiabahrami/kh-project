"""Views for handling speaking engagements."""
from django.views.generic import ListView
from speaking.models import Presentation

# Create your views here.


class PresentationsList(ListView):
    """View for listing presentations."""

    model = Presentation
    context_object_name = 'presentations'
    template_name = "speaking/speaking.html"

    def get_context_data(self, **kwargs):
        """Chop the presentations into pairs."""
        context = super().get_context_data(**kwargs)
        presentations = context['presentations']
        context['presentation_pairs'] = []
        for i in range(0, len(context[self.context_object_name]) - 1, 2):
            context['presentation_pairs'].append([presentations[i], presentations[i + 1]])
        return context
