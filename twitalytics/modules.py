import locale


def get_user(user):
    """Print general user information"""

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


def print_tweets(tweet):
    """Prints user tweets, if requested"""

    print("    %s" % tweet.text)
    print("    at: %s" % tweet.created_at)
    print('\t  via %s' % tweet.source)

    # print newline to separate multiple users
    print()


def get_sources(tweet, sources):
    """Get tweet source and add tally to collection"""
    sources[tweet.source] += 1
    return sources

def get_locations(tweet, locations):
    """Get tweet location and add tally to collection"""
    if tweet.place:
        tweet.place.name = tweet.place.name
        locations[tweet.place.name] += 1
    return locations


def get_topics(tweet, words):
    """Get tweet words and add tally to collection"""
    # TODO: refine so that common words get skipped
    for word in tweet.text.split():
        if(len(word) > 4):
            words[word] += 1
    return words



def get_twp():
    """Get tweets per day"""
    pass
