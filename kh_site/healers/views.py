"""Views for play page."""
from django.shortcuts import render
from healers.models import Event, AddEvent
from django.http import HttpResponseRedirect


def play_view(request):
    """Populate articles on blog page."""
    events = Event.objects.all()
    return render(request, 'play.html', {'articles': events})


def add_event(request):
    """View to add a blog article to database through UI."""
    form = AddEvent(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/play/')
    return render(request, 'add_event.html', context={'form': form})


def edit_event(request, pk):
    """Edit an article."""
    if request.method == 'POST':
        event = Event.objects.get(id=pk)
        form = AddEvent(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/play/')
        return render(request, 'edit_event.html', context={'form': form})
    else:
        event = Event.objects.get(id=pk)
        form = AddEvent(instance=event)
        return render(request, 'edit_event.html', context={'form': form})
