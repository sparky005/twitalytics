from .api import *
import sys
import locale

def get_general(users, count, api):
    """Get general information about Twitter user"""

    # set locale
    locale.setlocale(locale.LC_ALL, '')

    for handle in users:
        # get information from api
        try:
            user = api.get_user(handle)
            timeline = api.user_timeline(handle, count=count)
        except tweepy.TweepError:
            print("Error: Couldn't query tweepy API. Quitting!")
            sys.exit(1)

        # get human-readable forms of potentially large numbers
        followers_count = locale.format('%d', int(user.followers_count), grouping=True)
        friends_count = locale.format('%d', int(user.friends_count), grouping=True)
        
        # print information
        print("Information about %s: " % handle)
        print("    Real name: %s" % user.name)
        print("    Description: %s" % user.description)
        print("    Website: %s" % user.url)
        print("    Location: %s" % user.location)
        print("    Followers: %s" % followers_count)
        print("    Following: %s" % friends_count)
        print("    Last %d tweets: " % count)
        for tweet in timeline:
            print("     %s" % tweet.text)
            print('\t    via %s' % tweet.source)
        print()

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
