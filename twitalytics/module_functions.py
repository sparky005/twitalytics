import locale
import tweepy
"""Helper functions for modules"""

def get_timeline(user, count, api):
    """Get user timeline"""
    if count>200:
        page_list, timeline = [], []
        for page in tweepy.Cursor(api.user_timeline, user, count=200).pages(16):
            page_list.append(page)
        for page in page_list:
            for status in page:
                timeline.append(status)
    else:
        timeline = api.user_timeline(user, count=count)
    return timeline

def print_general(user, timeline, count):

    # set locale
    locale.setlocale(locale.LC_ALL, '')

    # get human-readable forms of potentially large numbers
    followers_count = locale.format('%d', int(user.followers_count), grouping=True)
    friends_count = locale.format('%d', int(user.friends_count), grouping=True)

    # print general user information
    print("Information about %s: " % user.screen_name)
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
