import datetime

from django_ical.views import ICalFeed
from django.urls import reverse

from events.models import Event
from events import utils


class Calendar(ICalFeed):
    product_id = '-//pyatl.dev//big-peach//EN'
    timezone = 'US/Eastern'
    file_name = 'pyatl.ics'

    def items(self):
        # Include events from the last year and into the future.
        start = utils.year_ago()
        return Event.objects.filter(
            published=True,
            start__gte=start,
        ).order_by('start')

    def item_title(self, item):
        return item.name

    def item_description(self, item):
        return item.description
