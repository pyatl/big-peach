import logging
import arrow
from django.utils import timezone
from django.core.management.base import BaseCommand
from social_rpa.twitter import authenticate, update_status
from social_rpa.models import ScheduledTweet

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Publish scheduled tweets to Twitter'

    def handle(self, *args, **options):

        consumer_key = ''
        consumer_secret = ''
        access_token = ''
        access_token_secret = ''

        api = authenticate(consumer_key, consumer_secret, access_token, access_token_secret)

        arw = arrow.utcnow()
        from_time = arw.shift(hours=-1).datetime
        to_time = timezone.now()

        scheduled_tweets = ScheduledTweet.objects.filter(
            published=False).filter(
                scheduled_for__gte=from_time).filter(
                    scheduled_for__lte=to_time)

        if scheduled_tweets:
            for scheduled_tweet in scheduled_tweets:
                successful = update_status(api, scheduled_tweet.tweet.content)
                if successful:
                    scheduled_tweet.published = True
                    scheduled_tweet.save()
                    logger.info(f'Published scheduled tweet with pk: {scheduled_tweet.pk}')
                else:
                    logger.error(f'Error publishing scheduled tweet with pk: {scheduled_tweet.pk}')

        logger.info('publish scheduled tweets command ran successfully')
