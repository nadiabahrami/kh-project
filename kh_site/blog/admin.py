"""Site administration for the Blog application."""
from django.contrib import admin
from blog.models import Article

DATE_FMT = '%b %d, %Y'


def last_modified_formatter(obj):
    return obj.last_modified.strftime(DATE_FMT)

last_modified_formatter.short_description = 'Last updated on'


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """."""

    fields = [
        'title', 'slug', 'content', 'status',
        last_modified_formatter, 'date_published',
    ]
    list_display = [
        'title', 'slug', 'status', 'date_created', 'date_published'
    ]
    date_hierarchy = 'date_created'
    empty_value_display = '-- empty --'
    readonly_fields = [last_modified_formatter]

    prepopulated_fields = {'slug': ('title',), }
