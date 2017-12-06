"""Group coaching models."""
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


DATE_FMT = '%b %d, %Y'
DEFAULT_LOGISTICS = """<ul>
    <li>8 group sessions total</li>
    <li>Weekly “office hours” (TBD in the new year) over the phone where I’m available for troubleshooting, Q&A, and check-ins</li>
    <li>Formation of daily self-care practice-exercises (Monday through Friday) to help you stay focused, build momentum, and move forward throughout the week</li>
    <li>Tailored invitations to work on between sessions to help you get stronger and more free</li>
</ul>"""
DEFAULT_LOCATION = "600 North 65th street, Seattle, WA"


class CoachingEvent(models.Model):
    """Model for a group coaching event."""

    start_date = models.DateField()
    end_date = models.DateField()
    meeting_days = models.CharField(max_length=1024, default='Wednesdays')
    start_time = models.TimeField()
    end_time = models.TimeField()
    cost = models.DecimalField(
        decimal_places=2, max_digits=5,
        help_text='Cost per person ($)', default=79.00
    )
    external_link = models.URLField(
        max_length=1024,
        help_text='Full URL to the event invite page. Ex: https://www.eventbrite.com/...'
    )
    location = models.CharField(default=DEFAULT_LOCATION, max_length=1024)
    logistics = models.TextField(default=DEFAULT_LOGISTICS)
    current_event = models.BooleanField(
        default=False, help_text='Is this the next group?'
    )

    def __repr__(self):
        return f"<Coaching Event | start { self.start_date.strftime(DATE_FMT) } >"

    def str(self):
        return f"Starting { self.start_date.strftime(DATE_FMT) }"


@receiver(post_save, sender=CoachingEvent)
def one_current(sender, **kwargs):
    if sender.current_event:
        events = CoachingEvent.objects.exclude(pk=sender.pk).filter_by(current_event=True).all()
        for event in events:
            event.current_event = False
            event.save()
