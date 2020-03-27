import tweepy


def authenticate(consumer_key, consumer_secret, access_token, access_token_secret):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return tweepy.API(auth)


def update_status(api, status):
    try:
        api.update_status(status)
        return True
    except (tweepy.TweepError, ) as e:
        pass
    return False
