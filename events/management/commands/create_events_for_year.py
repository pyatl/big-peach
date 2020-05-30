
import pytz
import dateutil.relativedelta as relativedelta
import dateutil.rrule as rrule
from datetime import datetime, timedelta
from django.utils import timezone
from django.utils.text import slugify
from django.core.management.base import BaseCommand, CommandError
from events.models import Event, Location


class Command(BaseCommand):
    help = 'Create all PYATL events for a calndar year.'

    TWITCH_LOCATION_NAME = 'PyATL Official Twitch Channel'
    TWITCH_LOCATION_DESCRIPTION_HTML = '''<p>
    The event will be live streamed through the official
    <a href="https://twitch.com/pyatl">PyATL Twitch Channel</a>.
    </p>
    '''

    DISCORD_LOCATION_NAME = 'PyATL Official Discord'
    DISCORD_LOCATION_DESCRIPTION_HTML = '''<p>
    The event will be live on our Jam Session Discord channel. Join us at the <a href="https://discord.gg/5UBnR3P">PyATL Discord here.</a>
    </p>
    '''

    TWITCH_EVENT_NAME_CODING_LIVE_STREAM = 'Live coding stream on PyATL\'s official Twitch channel'
    TWITCH_EVENT_SHORT_DESCRIPTION = 'Twitch streaming session on the official PyATL Twitch channell.'
    TWITCH_EVENT_DESCRIPTION_HTML = '''
    <p>
    Coding live streams about Python and related technologies.
    You can also watch the event after it is finished by visiting
    our official Twitch PyATL channel.
    </p>
    <p>
    The event will be live streamed through the official
    <a href="https://twitch.com/pyatl">PyATL Twitch Channel</a>.
    </p>

    <p>
    <iframe
    src="https://player.twitch.tv/?channel=pyatl&parent=pyatl.dev"
    height="360"
    width="640"
    frameborder="0"
    scrolling="no"
    allowfullscreen="true">
    </iframe>
    </p>
    '''

    JAM_SESSION_EVENT_NAME = 'PyATL Jam Session'
    JAM_SESSION_EVENT_SHORT_DESCRIPTION = 'Jam Session meetings are intended to be hands-on, collaborative experiences with your fellow PyATL members.'
    JAM_SESSION_EVENT_DESCRIPTION_HTML = '''
    <p>
    Note: all Jam Sessions will be held online on our <a href="https://discord.gg/5UBnR3P">Discord instance</a> until further notice. We hope that will be able to meet all of you face to face later! The event will be hosted on the PyATL Discord channel; the link will be displayed after you RSVP.
    <p>

    <p>
    What is a Jam Session?
    https://github.com/pyatl/jam-sessions/wiki
    </p>

    <p>
    Jam Session meetings are intended to be hands-on, collaborative experiences with your fellow PyATL members. Programmers of all experience levels are welcome! We will be meeting from 7pm to 10pm to work together on a coding challenge or on any project you want. We recommend bringing a laptop with you, optionally with Python installed (but the coding challenge does not require it).
    </p>

    <p>
    Each month we provide a coding puzzle or exercise that is designed to be accessible to novices to Python, but that also provide additional challenges for more advanced users. We use the online platform at https://www.cyber-dojo.org/ to run the challenge and share our solutions with each other.
    </p>

    <p>
    The Jam session is also a safe space to work and ask for help on any Python project. Bring your own hobby projects, a work project, your new startup idea - whatever you like. Or come along and see others are working on, and sit down with them! The organizers will be there a bit early to help introduce people, organize, and make sure everyone is comfortable.
    </p>'''

    MEETUP_EVENT_NAME = 'Python Atlanta Meetup'
    MEETUP_EVENT_SHORT_DESCRIPTION = 'Python Atlanta Meetup Monthly Event'
    MEETUP_EVENT_DESCRIPTION_HTML = '''
    <p>All in-person events are on hold until further notice.</p>
    <p>We will be holding events live on our Twitch channel.</p>
    
    <p>
    <iframe
    src="https://player.twitch.tv/?channel=pyatl&parent=pyatl.dev"
    height="360"
    width="640"
    frameborder="0"
    scrolling="no"
    allowfullscreen="true">
    </iframe>
    </p>

    <p>The meeting starts at 7:30PM in the North Avenue room. Some of us get together before the meeting between 6:00 and 6:30 to have dinner and talk.</p>

    <p>Excellent Talks Scheduled: To be announced</p>
    '''

    def create_event(self, name, short_description, description, start, end, location):
        event, created = Event.objects.get_or_create(
            name=name,
            slug=slugify(name),
            short_description=short_description,
            description=description,
            start=start,
            end=end,
            published=True,
            location=location)
        return event

    def handle(self, *args, **options):
        # get the current year
        # starting date - now when the script is run
        # end date - last day of the year
        # rules = every tuesday and friday. Every 1st and 2nd thursday
        # for each of the rules, we need to create a specific event.
        now = timezone.now()
        start_date = datetime(now.year, 1, 1, 19, 0, 0).replace(tzinfo=pytz.utc)
        end_date = datetime(now.year, 12, 31, 19, 0, 0).replace(tzinfo=pytz.utc)

        # location for twitch related events

        twitch_location = Location.objects.create(
            name=self.TWITCH_LOCATION_NAME,
            slug=slugify(self.TWITCH_LOCATION_NAME),
            description=self.TWITCH_LOCATION_DESCRIPTION_HTML,)
        
        discord_location = Location.objects.create(
            name=self.DISCORD_LOCATION_NAME,
            slug=slugify(self.DISCORD_LOCATION_NAME),
            description=self.DISCORD_LOCATION_DESCRIPTION_HTML,)

        tuesdays = rrule.rrule(
            rrule.WEEKLY,
            byweekday=relativedelta.TU,
            dtstart=start_date)

        fridays = rrule.rrule(
            rrule.WEEKLY,
            byweekday=relativedelta.FR,
            dtstart=start_date)

        thursdays = rrule.rrule(
            rrule.WEEKLY,
            byweekday=relativedelta.TH,
            dtstart=start_date)

        tuesdays_days = tuesdays.between(
            start_date,
            end_date,
            inc=True)

        fridays_days = fridays.between(
            start_date,
            end_date,
            inc=True)

        thursdays_days = thursdays.between(
            start_date,
            end_date,
            inc=True)

        # first get the first and second thursdays of the month
        first_and_second_thursdays = []
        for thursday in thursdays_days:
            if thursday.day <= 14:
                first_and_second_thursdays.append(thursday)

        # then get the first thirsdays
        first_thursdays = []
        for thursday in first_and_second_thursdays:
            if thursday.day <= 7:
                first_thursdays.append(thursday)
                # remove the first thursday so we only endup
                # with second thursdays on this list
                first_and_second_thursdays.remove(thursday)
        # reassign for redability
        second_thursdays = first_and_second_thursdays

        # streaming on tuesdays 
        for day in tuesdays_days:
            tuesday_event = self.create_event(
                self.TWITCH_EVENT_NAME_CODING_LIVE_STREAM,
                self.TWITCH_EVENT_SHORT_DESCRIPTION,
                self.TWITCH_EVENT_DESCRIPTION_HTML,
                day,
                day+timedelta(hours=2),
                twitch_location)

        # streaming on fridays
        for day in fridays_days:
            friday_event = self.create_event(
                self.TWITCH_EVENT_NAME_CODING_LIVE_STREAM,
                self.TWITCH_EVENT_SHORT_DESCRIPTION,
                self.TWITCH_EVENT_DESCRIPTION_HTML,
                day,
                day+timedelta(hours=2),
                twitch_location)

        # jam session
        for day in first_thursdays:
            jam_session = self.create_event(
                self.JAM_SESSION_EVENT_NAME,
                self.JAM_SESSION_EVENT_SHORT_DESCRIPTION,
                self.JAM_SESSION_EVENT_DESCRIPTION_HTML,
                day,
                day+timedelta(hours=2),
                discord_location)

        # meetup
        for day in second_thursdays:
            meetup_event = self.create_event(
                self.MEETUP_EVENT_NAME,
                self.MEETUP_EVENT_SHORT_DESCRIPTION,
                self.MEETUP_EVENT_DESCRIPTION_HTML,
                day,
                day+timedelta(hours=2),
                discord_location)

        self.stdout.write(self.style.SUCCESS('Events Created'))