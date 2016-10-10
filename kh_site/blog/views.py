"""Views for blog page."""

from django.shortcuts import render
from models import AddArticle, Article
from django.http import HttpResponseRedirect

# Create your views here.


def blog_view(request):
    """Populate articles on blog page."""
    articles = Article.objects.all()
    return render(request, 'blog.html', {'articles': articles})


def add_article(request):
    """View to add a blog article to database through UI."""
    form = AddArticle(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.owner = request.user
            form.save()
            return HttpResponseRedirect('/blog/')
    return render(request, 'add_article.html', context={'form': form})
