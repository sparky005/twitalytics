import locale
from nltk.corpus import stopwords
import pandas as pd
from .lemmas import *
import pickle

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


def get_words(tweet, words):
    """Get tweet words and add tally to collection"""
    for word in tweet.text.split():
        if(not word.lower().startswith(tuple(stopwords.words('english'))) and not word.startswith(('@', 'RT'))):
            words[word] += 1
    return words

def get_topics(tweets):
    """Figure out what this user tweets about"""
    # load the classifier we built earlier
    tweets_text = [tweet.text for tweet in tweets]
    cl = pickle.load(open('tweet_emotion_classifier.pkl', 'rb'))
    topics = cl.predict(tweets_text)
    return topics



def get_tweets_per_day(dates):
    """Get tweets per day"""

    # creates a series of tweets indexed by date
    ones = [1]*len(dates)
    idx = pd.DatetimeIndex(dates, tz='UTC')
    idx = idx.tz_convert('US/Eastern')
    tweets = pd.Series(ones, index=idx)
    # counts up tweets in 1 day increments
    tweets_per_day = tweets.resample('1D').sum().fillna(0)

    # return the mean
    return tweets_per_day.mean()