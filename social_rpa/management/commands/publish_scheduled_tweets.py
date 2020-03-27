import arrow
from django.utils import timezone
from django.core.management.base import BaseCommand, CommandError
from social_rpa.models import ScheduledTweet
from social_rpa.twitter import autheticate, update_status

class Command(BaseCommand):
    help = 'Publish scheduled tweets to Twitter'

    def handle(self, *args, **options):

        consumer_key = ''
        consumer_secret = ''
        access_token = ''
        access_token_secret = ''

        api = authenticate(consumer_key, consumer_secret, access_token, access_token_secret)

        arw = arrow.utcnow()
        arw.shift(hour=-1)
        from_time = arw.datetime
        to_time = timezone.now()
        
        scheduled_tweets = ScheduledTweets.objects.filter(published=False
        ).filter(scheduled_for__gte=from_time).filter(scheduled_for__lte=to_time)

        if scheduled_tweets:
            for scheduled_tweet in scheduled_tweets:
                successful = update_status(api, scheduled_tweet.tweet.content)
                if successful:
                    scheduled_tweet.published = True
                    scheduled_tweet.save()
                    # log success
                else:
                    pass
                    # log errors
            # log job ran and published tweets
        else:
            # log job ran but no tweets
