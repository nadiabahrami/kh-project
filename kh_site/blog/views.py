"""Views for blog page."""

from django.shortcuts import render
from blog.models import Article, AddArticle
from django.http import HttpResponseRedirect

# Create your views here.


def blog_view(request):
    """Populate articles on blog page."""
    articles = Article.public.all()
    return render(request, 'blog.html', {'articles': articles, 'hello': 'hello'})


def add_article(request):
    """View to add a blog article to database through UI."""
    form = AddArticle(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/blog/')
    return render(request, 'add_article.html', context={'form': form})
