#TODO

import tweepy
from Helper import getAuth

auth = tweepy.OAuth2BearerHandler(getAuth("Twitter", "Bearer_Token"))
api = tweepy.API(auth)

api.update_status ('Updating using OAuth authentication via Tweepy!')