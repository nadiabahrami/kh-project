from django.views.generic import DetailView
from django.shortcuts import render
from group_coaching.models import CoachingEvent


class EventDetail(DetailView):
    """View for displaying a single event's detail."""

    model = CoachingEvent
    template = 'group_coaching/next_event.html'
