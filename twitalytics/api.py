import tweepy
import json
import os.path
import webbrowser as wb
from . import consumer


def store_access_token(token_file):
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

    with open(token_file, 'w') as f:
        # save the access token
        json.dump(access_token, f)


def get_api():
    """
    Get authentication information and create API
    If no token exists, get the token
    """

    # get where we think the token should be stored
    token_file = os.path.expanduser('~') + '/.twitalytics/twitter_credentials.json'

    # check if file exists
    if not os.path.exists(token_file):
        os.makedirs(os.path.expanduser('~' + '/.twitalytics'))
        store_access_token(token_file)

    try:
        with open(token_file) as f:
            access_token = json.load(f)
    except FileNotFoundError:
        print("Error: couldn't find credentials file")

    auth = tweepy.OAuthHandler(consumer.CONSUMER_KEY, consumer.CONSUMER_SECRET)
    auth.set_access_token(access_token[0], access_token[1])
    api = tweepy.API(auth)
    return api


def get_timeline(user, count, api, start_date, end_date):
    """Get user timeline"""

    page_list, timeline = [], []

    # get specified number of tweets
    # use cursor so we can get up to 3200
    for status in tweepy.Cursor(api.user_timeline, user).items(count):
        if (status.created_at >= start_date and status.created_at <= end_date):
            timeline.append(status)
    return timeline
