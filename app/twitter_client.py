import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

class TwitterClient:
    def __init__(self):
        self.api_key = os.getenv("TWITTER_API_KEY")
        self.api_secret = os.getenv("TWITTER_API_SECRET")
        self.access_token = os.getenv("TWITTER_ACCESS_TOKEN")
        self.access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
        self.target_account = os.getenv("TWITTER_TARGET_ACCOUNT")
        
        auth = tweepy.OAuthHandler(self.api_key, self.api_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        self.api = tweepy.API(auth)

    def get_user_tweets(self, count=100):
        try:
            tweets = self.api.user_timeline(
                screen_name=self.target_account,
                count=count,
                tweet_mode="extended"
            )
            return tweets
        except Exception as e:
            print(f"Error fetching tweets: {str(e)}")
            return []
