from django.urls import re_path
from events.views import (
    EventView,
    EventsView,
    LocationView,
    LocationsView,
    EventInviteDownloadView,
)
from events.feeds import Calendar

slug = '(?P<slug>[-\\w\\d]+)'
pk = '(?P<pk>[0-9]+)'
date = '(?P<date>[0-9]{4}-?[0-9]{2}-?[0-9]{2})'

urlpatterns = [
    # location
    re_path(r'^location/{slug}/{pk}/$'.format(
        slug=slug,
        pk=pk),
        LocationView.as_view(),
        name='location'),
    re_path(r'^locations/$', LocationsView.as_view(), name='locations'),

    # event
    re_path(r'^{date}/{slug}/{pk}/$'.format(
        date=date,
        slug=slug,
        pk=pk),
        EventView.as_view(),
        name='event'),
    re_path(r'^invite/{pk}/$'.format(
        pk=pk),
        EventInviteDownloadView.as_view(),
        name='event-invite'),
    re_path(r'^$', EventsView.as_view(), name='events'),

    # calendar
    path('feed/ical/', Calendar(), name='calendar'),
]
