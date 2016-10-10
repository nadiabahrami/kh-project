from django.shortcuts import render
from models import AddArticle
from django.http import HttpResponseRedirect

# Create your views here.


def add_article(request):
    """View to add a blog article to database through UI."""
    form = AddArticle(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.owner = request.user
            form.save()
            return HttpResponseRedirect('/blog/')
    return render(request, 'add_article.html', context={'form': form})
