"""Models for event posts."""
from django.db import models
from django.forms import ModelForm
import datetime


def _image_path(instance, filename):
    """Photo will be uploaded to media root then correct folder."""
    return "{0}/{1}".format(datetime.date.today(), filename)


class EventManager(models.Manager):
    """Define an Active Profile Manager class."""

    def get_queryset(self):
        """Return a list of all active users."""
        qs = super(EventManager, self).get_queryset()
        return qs.all()


class Event(models.Model):
    """Create a blog article."""

    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(max_length=5000, blank=False)
    event_photo = models.ImageField(upload_to=_image_path, blank=True)
    date_published = models.DateTimeField(default=datetime.datetime.now)
    address = models.CharField(max_length=200, blank=True)
    event_date = models.DateTimeField()
    event_time = models.CharField(max_length=20, blank=True)
    objects = EventManager()


class AddEvent(ModelForm):
    """Form class for adding aa blog article."""

    class Meta:
        """Content for blog post form."""

        model = Event
        fields = ['event_photo', 'title', 'description', 'address', 'event_date', 'event_time']
