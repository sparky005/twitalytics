import locale
from collections import Counter


def get_general(user, timeline, print_tweets):
    """Print general information"""

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

    # print tweets if requested
    if print_tweets:
        print("    Last tweets: ")
        for tweet in timeline:
            print("     %s" % tweet.text)
            print("     at: %s" % tweet.created_at)
            print('\t    via %s' % tweet.source)

    # print newline to separate multiple users
    print()


def get_sources(timeline):
    """Get top devices that user tweets from"""
    sources = Counter()
    for tweet in timeline:
        sources[tweet.source] += 1
    # TODO: what do I want to do from here? a graph?
    print(sources.most_common(10))


def get_locations(timeline):
    """Get top locations that user tweets from"""
    locations = Counter()
    for tweet in timeline:
        if tweet.place:
            tweet.place.name = tweet.place.name
            locations[tweet.place.name] += 1
    print(locations.most_common(10))


def get_topics(timeline):
    """Get top topics the user tweets about"""
    # TODO: refine so that common words get skipped
    words = Counter()
    for tweet in timeline:
        for word in tweet.text.split():
            words[word] += 1
    print(words.most_common(10))



def get_twp():
    """Get tweets per day"""
    pass
