import datetime

from django.test import TestCase
import pytz

from events.models import Location, Event
from events.feeds import Calendar
from events import utils


class CalendarTestCase(TestCase):

    def setUp(self):
        today = utils.now()
        year_ago = utils.year_ago()
        over_year_ago = year_ago - datetime.timedelta(days=1)
        next_month = today + datetime.timedelta(days=30)

        self.location = Location.objects.create(
            name='test location',
            slug='test-location',
            description='how to get there',
        )

        self.old_excluded_event = Event.objects.create(
            name='old excluded event',
            slug='old-excluded-event',
            short_description='event too old for calendar',
            start=over_year_ago,
            end=over_year_ago + datetime.timedelta(days=1),
            location=self.location,
            published=True,
        )

        self.old_included_event = Event.objects.create(
            name='old included event',
            slug='old-included-event',
            short_description='event old, but on calendar',
            start=year_ago,
            end=year_ago + datetime.timedelta(days=1),
            location=self.location,
            published=True,
        )

        self.current_included_event = Event.objects.create(
            name='current included event',
            slug='current-included-event',
            short_description='event current, and on calendar',
            start=today,
            end=today + datetime.timedelta(days=1),
            location=self.location,
            published=True,
        )

        self.new_included_event = Event.objects.create(
            name='new included event',
            slug='new-included-event',
            short_description='event new, and on calendar',
            start=next_month,
            end=next_month + datetime.timedelta(days=1),
            location=self.location,
            published=True,
        )

        self.new_excluded_event = Event.objects.create(
            name='new excluded event',
            slug='new-excluded-event',
            short_description='event new, and on calendar',
            start=next_month,
            end=next_month + datetime.timedelta(days=1),
            location=self.location,
            published=False,
        )

        self.feed = Calendar()

    def test_items(self):
        self.assertEqual(
            ['old excluded event',
             'old included event',
             'current included event',
             'new included event',
             'new excluded event',
            ],
            [e.name for e in Event.objects.all().order_by('start')],
        )
        self.assertEqual(
            ['old included event',
             'current included event',
             'new included event'],
            [self.feed.item_title(i) for i in self.feed.items()],
        )
