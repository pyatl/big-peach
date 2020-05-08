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

        scheduled_tweets = ScheduledTweets.objects.filter(published=False) # add time range filter

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
