from django_ical.views import ICalFeed
from events.models import Event
from events import utils


class Calendar(ICalFeed):
    product_id = '-//pyatl.dev//big-peach//EN'
    timezone = 'US/Eastern'
    file_name = 'pyatl.ics'
    title = 'PyATL Events'
    description = 'Atlanta-area Python User Group (PyATL) events calendar from https://pyatl.dev'

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
