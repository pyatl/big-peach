# ./manage.py test social_rpa -v=3

from django.test import TestCase
from unittest.mock import MagicMock
import unittest.mock as mock
from .twitter import authenticate, update_status


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
    auth = mock_uathenticate()
    auth.update_status = MagicMock(return_value=True)


class TestPublishScheduledTweetsCommand(TestCase):
    def setUp(self):
        self.consumer_key = '1'
        self.consumer_secret = '2'
        self.access_token = '3'
        self.access_token_secret = '4'
    
    @mock.patch('tweepy.API', side_effect=mock_authenticate)
    def test_twitter_authenticate_returns_true(self, mocko):
        self.assertTrue(authenticate(self.consumer_key,self.consumer_secret,self.access_token,self.access_token_secret))

    @mock.patch('tweepy.API.update_status', side_effect=mock_update_status)
    def test_twitter_update_status_returns_true(self, mocko):
        result = update_status(MockTweepy.API(), status='test')
        self.assertTrue(result)


# TODO:

# Add tests for publish_scheduled_tweets_command