from django_ical.views import ICalFeed
from events.models import Event
from events import utils


class Calendar(ICalFeed):
    product_id = '-//pyatl.dev//big-peach//EN'
    timezone = str(utils._tz)
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

    def item_guid(self, item):
        return 'pyatl{}'.format(item.id)

    def item_start_datetime(self, item):
        return item.start

    def item_end_datetime(self, item):
        return item.end

    def item_location(self, item):
        return item.location.name

    def item_geolocation(self, item):
        return item.location.map_embed_code
