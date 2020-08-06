import logging
from django.utils import timezone
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404
from events.models import (
    Event,
    EventInvite,
    Location,
)

logger = logging.getLogger(__name__)


class EventDetailView(DetailView):
    model = Event
    context_object_name = 'event'


class EventsListView(ListView):
    model = Event
    context_object_name = 'events'

    def get_queryset(self):
        return Event.objects.filter(published=True, start__gte=timezone.now())


class LocationDetailView(DetailView):
    model = Location
    context_object_name = 'location'


class LocationsListView(ListView):
    model = Location
    context_object_name = 'locations'


class EventInviteDownloadView(View):
    '''
    Allows user to download a calendar invite
    for an event.
    '''

    def get(self, request, **kwargs):
        '''
        Generates the ical (ics) invite
        for users to download.
        '''
        event = get_object_or_404(Event, pk=kwargs['pk'], published=True)
        event_invite = EventInvite(event, request.META.get('HTTP_HOST'), request.scheme)
        invite = event_invite.generate()
        response = HttpResponse(invite, content_type='text/calendar')
        response['Filename'] = f'{event.slug}-{event.slugify_start}.ics'
        response['Content-Disposition'] = f'attachment; filename={event.slug}-{event.slugify_start}.ics'
        return response
