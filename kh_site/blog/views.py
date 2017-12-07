"""Views for blog page."""
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import Article, AddArticle, DeleteArticle
from django.http import HttpResponseRedirect


class BlogView(ListView):
    """List all of the blog articles in descending order."""

    model = Article
    queryset = Article.published.order_by('-date_published').all()
    context_object_name = 'articles'
    template_name = 'blog/blog.html'
    paginate_by = 5


class BlogDetail(DetailView):
    """Get the detail for one blog post by pk or by slug."""

    model = Article
    queryset = Article.published.all()
    context_object_name = 'article'
    template_name = 'blog/detail_article.html'
    query_pk_and_slug = True


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


def delete_article(request, pk):
    """Edit an article."""
    if request.method == 'POST':
        blog = Article.objects.get(id=pk)
        form = DeleteArticle(request.POST, instance=blog)
        if form.is_valid():
            blog.delete()
            return HttpResponseRedirect('/blog/')
        return render(request, 'delete_article.html', context={'form': form})
    else:
        blog = Article.objects.get(id=pk)
        form = DeleteArticle(request.POST, instance=blog)
        return render(request, 'delete_article.html', context={'form': form})
