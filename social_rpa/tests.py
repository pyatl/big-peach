# ./manage.py test social_rpa -v=3
from django.test import TestCase
from django.core.management import call_command
from django.contrib.auth.models import User
from django.utils import timezone
from unittest.mock import MagicMock
import unittest.mock as mock
from social_rpa.twitter import authenticate, update_status
from social_rpa.models import ScheduledTweet, Tweet


class MockTweepy:
    class API:
        def __init__(self, *args, **kwargs):
            pass

        def __str__(self):
            return 'test'

        def update_status(self, args, **kwargs):
            return True


def mock_authenticate(*args, **kwargs):
    return MockTweepy.API()


def mock_update_status(*args, **kwargs):
    auth = mock_authenticate()
    auth.update_status = MagicMock(return_value=True)


class TestTwitter(TestCase):
    def setUp(self):
        self.consumer_key = '1'
        self.consumer_secret = '2'
        self.access_token = '3'
        self.access_token_secret = '4'

    @mock.patch('tweepy.API', side_effect=mock_authenticate)
    def test_twitter_authenticate_returns_true(self, mocko):
        self.assertTrue(authenticate(self.consumer_key,
                                     self.consumer_secret,
                                     self.access_token,
                                     self.access_token_secret))

    @mock.patch('tweepy.API.update_status', side_effect=mock_update_status)
    def test_twitter_update_status_returns_true(self, mocko):
        result = update_status(MockTweepy.API(), status='test')
        self.assertTrue(result)


class TestPublishScheduledTweetsCommand(TestCase):
    def setUp(self):
        self.test_user = User.objects.create(
            username='test_user',
            password='123',
            email='test@test.com'
        )

        self.tweet = Tweet.objects.create(
            author=self.test_user,
            title='test tweet title',
            content='test tweet content',
        )

        self.scheduled_tweet = ScheduledTweet.objects.create(
            scheduled_for=timezone.now(),
            published=False,
            tweet=self.tweet,
            scheduled_by=self.test_user,
        )

    @mock.patch('tweepy.API', side_effect=mock_authenticate)
    @mock.patch('tweepy.API.update_status', side_effect=mock_update_status)
    def test_scheduled_tweet_get_published(self, mocko_authenticate, mocko_update_status):
        call_command('publish_scheduled_tweets')
        self.scheduled_tweet.refresh_from_db()
        self.assertTrue(self.scheduled_tweet.published)
