from django.views.generic import TemplateView
from resource.models import Category, Resource


class ResourceView(TemplateView):
    template_name = 'resources/resource_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['resources'] = Resource.objects.all()
        return context
