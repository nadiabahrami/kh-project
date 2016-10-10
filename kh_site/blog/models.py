"""Models for blog posts."""
from django.db import models
from django.forms import ModelForm


def _image_path(instance, filename):
    """Photo will be uploaded to media root then correct folder."""
    return "user_{0}/{1}".format(instance.owner.id, filename)


class ArticleManager(models.Manager):
    """Define an Active Profile Manager class."""

    def get_queryset(self):
        """Return a list of all active users."""
        qs = super(ArticleManager, self).get_queryset()
        return qs.all()


class Article (models.Model):
    """Create a blog article."""

    tile = models.CharField(max_length=200, blank=True),
    content = models.CharField(max_length=5000, blank=True),
    blog_photo = models.ImageField(upload_to=_image_path),
    date_uploaded = models.DateTimeField(auto_now_add=True),
    date_modified = models.DateTimeField(auto_now=True),
    date_published = models.DateTimeField(null=True, blank=True),
    tags = models.CharField(max_length=30, blank=True),

    public = ArticleManager()


class AddArticle(ModelForm):
    """Form class for adding aa blog article."""

    class Meta:
        """Info to be served up to the form."""

        model = Article
        fields = ['title', 'content', 'blog_photo', 'tags']
