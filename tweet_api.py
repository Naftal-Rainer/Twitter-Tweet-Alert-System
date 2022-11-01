import tweepy
import configparser

# Read configs

config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['API_Key']
api_key_secret = config['twitter']['API_Key_Secret']
access_tocken = config['twitter']['Access_Tocken']
access_tocken_secret = config['twitter']['Access_Tocken_Secret']

# Authenticate app to twitter API

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_tocken, access_tocken_secret)

# Make API instance

api = tweepy.API(auth)

public_tweets = api.home_timeline()

print(public_tweets)