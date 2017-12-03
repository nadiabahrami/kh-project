"""Administration for the Speaking app."""
from django.contrib import admin
from speaking.models import Presentation
from django.db import models

FMT = '%b %d, %Y'


def creation_date_formatter(obj):
    """Format a date."""
    return obj.date_created.strftime(FMT)


def mod_date_formatter(obj):
    """Format a date."""
    return obj.last_modified.strftime(FMT)


creation_date_formatter.short_description = 'Created On'
mod_date_formatter.short_description = 'Last Modified On'


@admin.register(Presentation)
class PresentationAdmin(models.ModelAdmin):
    """Administration for the Presentation model."""

    date_hierarchy = 'date_created'
    empty_value_display = '-empty-'
    exclude = ['date_created']
    list_display = ['title', creation_date_formatter, mod_date_formatter]
