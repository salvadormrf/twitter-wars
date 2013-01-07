import sys
import tweepy

from tasks import analyse_tweet

# application created on Twitter dev account
consumer_key="Lm9bxQ4iAWWxniVCgVIU0w"
consumer_secret="nbyVlqGWZRvKFLMf0k6NAooWYihjluKGPyzQlAzQk"
access_key = "143383751-4EQIepueLFNfPITRy7hHcNnJZNxmqmiRnuuSz4Dk"
access_secret = "6FHSvYW6gVEardPIVLAX1rwxMLZjAydiB2MlX33Iyo"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

class CustomStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        # analyse if tweet has geo information
        if status.geo:
            # let's analyse the tweet text asynchronously
            analyse_tweet.delay(status.text, status.geo)
    
    def on_error(self, status_code):
        return True # Don't kill the stream

    def on_timeout(self):
        return True # Don't kill the stream


# London -0.351468,51.38494,0.14788,51.672343
# Exeter -3.570203,50.687391,-3.456359,50.761465
sapi = tweepy.streaming.Stream(auth, CustomStreamListener())
sapi.filter(locations=[-0.351468, 51.38494, 0.14788, 51.672343, -3.570203, 50.687391, -3.456359, 50.761465])
