from django.views.generic import TemplateView
from django.conf import settings


class ContactView(TemplateView):
    template_name = "base/contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['GOOGLE_KEY'] = settings.GOOGLE_KEY
        return context
