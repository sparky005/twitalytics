import tweepy
import json
import os.path
import webbrowser as wb
from . import consumer


def store_access_token():
    """Get Access Token and store in .json file"""

    # create oauth handler
    auth = tweepy.OAuthHandler(consumer.CONSUMER_KEY, consumer.CONSUMER_SECRET)

    try:
        wb.open(auth.get_authorization_url())
    except tweepy.TweepError:
        print("Error! Could not get request token")
    verifier = input("Verification code: ")
    try:
        access_token = auth.get_access_token(verifier)
    except tweepy.TweepError:
        print("Failed to get token")

    with open('twitter_credentials.json', 'w') as f:
        # save the access token
        # TODO: save the creds in a better place
        json.dump(access_token, f)


def get_api():
    """
    Get authentication information and create API
    If no token exists, get the token
    """

    # check if file exists
    if not os.path.exists('twitter_credentials.json'):
        store_access_token()

    try:
        with open('twitter_credentials.json') as f:
            access_token = json.load(f)
    except FileNotFoundError:
        print("Error: couldn't find credentials file")

    auth = tweepy.OAuthHandler(consumer.CONSUMER_KEY, consumer.CONSUMER_SECRET)
    auth.set_access_token(access_token[0], access_token[1])
    api = tweepy.API(auth)
    return api

