from .api import *
from .module_functions import *
import sys

def get_general(users, count, api):
    """Get general information about Twitter user"""


    for handle in users:
        # get information from api
        try:
            user = api.get_user(handle)
            timeline = get_timeline(handle, count, api)
        except tweepy.TweepError:
            print("Error: Couldn't query tweepy API. Quitting!")
            sys.exit(1)

        print_general(user, timeline, count)


def get_devices():
    """Get top devices that user tweets from"""
    pass

def get_locations():
    """Get top locations that user tweets from"""
    pass

def get_topics():
    """Get top topics the user tweets about"""
    pass

def get_twp():
    """Get tweets per day"""
    pass
