from django.core.management.base import BaseCommand, CommandError
from social_rpa.models import ScheduledTweet

class Command(BaseCommand):
    help = 'Published scheduled tweets to Twitter'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Successfully published scheduled tweets'))