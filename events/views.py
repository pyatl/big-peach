from django.utils import timezone
from django.http import HttpResponse
from django.views.generic import TemplateView, View
from django.shortcuts import get_object_or_404
from events.models import (
    Event,
    EventInvite,
    Location,
)


class EventView(TemplateView):
    ''' Show single Event '''
    template_name = 'events/event-detail.html'

    def get_context_data(self, **kwargs):
        context = super(EventView, self).get_context_data(**kwargs)
        context['event'] = get_object_or_404(Event, pk=kwargs['pk'], published=True)
        return context


class EventsView(TemplateView):
    ''' List all Events '''
    template_name = 'events/events.html'

    def get_context_data(self, **kwargs):
        context = super(EventsView, self).get_context_data(**kwargs)
        context['events'] = Event.objects.filter(published=True, start__gte=timezone.now())
        return context


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
        response['Filename'] = '{0}-{1}.ics'.format(event.slug, event.slugify_start)
        response['Content-Disposition'] = 'attachment; filename={0}-{1}.ics'.format(
            event.slug, event.slugify_start)
        return response


class LocationView(TemplateView):
    ''' Show single Location '''
    template_name = 'events/location-detail.html'

    def get_context_data(self, **kwargs):
        context = super(LocationView, self).get_context_data(**kwargs)
        context['location'] = get_object_or_404(Location, pk=kwargs['pk'])
        return context


class LocationsView(TemplateView):
    ''' List all Locations '''
    template_name = 'events/locations.html'

    def get_context_data(self, **kwargs):
        context = super(LocationsView, self).get_context_data(**kwargs)
        context['locations'] = Location.objects.all()
        return context
