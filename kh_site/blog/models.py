"""Models for blog posts."""
from django.db import models
from django.forms import ModelForm
import datetime


def _image_path(instance, filename):
    """Photo will be uploaded to media root then correct folder."""
    return "{0}/{1}".format(datetime.date.today(), filename)


class ArticleManager(models.Manager):
    """Define an Active Profile Manager class."""

    def get_queryset(self):
        """Return a list of all active users."""
        qs = super(ArticleManager, self).get_queryset()
        return qs.all()


class Article(models.Model):
    """Create a blog article."""

    title = models.CharField(max_length=200, blank=True)
    content = models.TextField(max_length=5000, blank=False)
    blog_photo = models.ImageField(upload_to=_image_path, blank=True)
    date_published = models.DateField(default=datetime.datetime.now)
    tags = models.CharField(max_length=30, blank=True)
    objects = ArticleManager()


class AddArticle(ModelForm):
    """Form class for adding aa blog article."""

    class Meta:
        """Content for blog post form."""

        model = Article
        fields = ['blog_photo', 'title', 'content', 'tags']


class DeleteArticle(ModelForm):
    """Form class for adding aa blog article."""

    class Meta:
        """Content for blog post form."""

        model = Article
        fields = []
