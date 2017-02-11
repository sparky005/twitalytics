import locale


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
    sources = {}
    for tweet in timeline:
        if tweet.source in sources:
            sources[tweet.source] += 1
        else:
            sources[tweet.source] = 1
    print(sources)
    # TODO: what do I want to do from here? a graph?


def get_locations():
    """Get top locations that user tweets from"""
    pass


def get_topics():
    """Get top topics the user tweets about"""
    pass


def get_twp():
    """Get tweets per day"""
    pass
