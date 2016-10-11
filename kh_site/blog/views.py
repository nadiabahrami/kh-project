"""Views for blog page."""
from django.shortcuts import render
from blog.models import Article, AddArticle
from django.http import HttpResponseRedirect


def blog_view(request):
    """Populate articles on blog page."""
    articles = Article.objects.all()
    return render(request, 'blog.html', {'articles': articles})


def add_article(request):
    """View to add a blog article to database through UI."""
    form = AddArticle(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/blog/')
    return render(request, 'add_article.html', context={'form': form})


def edit_article(request, pk):
    """Edit an article."""
    if request.method == 'POST':
        blog = Article.objects.get(id=pk)
        form = AddArticle(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/blog/')
        return render(request, 'edit_article.html', context={'form': form})
    else:
        blog = Article.objects.get(id=pk)
        form = AddArticle(instance=blog)
        return render(request, 'edit_article.html', context={'form': form})
