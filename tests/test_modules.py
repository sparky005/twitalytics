from twitalytics import modules
import vcr
import tweepy
from collections import Counter
import sklearn
import textblob

@vcr.use_cassette('tests/vcr_cassettes/user.yml')
def test_get_user(client_api, capsys, user_info):
    user = client_api.get_user('nytimes')
    desired_output = user_info
    desired_output = desired_output.strip()

    assert isinstance(user, tweepy.models.User)
    modules.get_user(user)
    out, err = capsys.readouterr()
    out = out.strip()
    assert out == desired_output

def test_print_tweets(timeline, capsys):
    desired_output = """    RT @maggieNYT: Bannon was set for a relatively smooth exit. Then Charlottesville happened. w @jwpetersNYT https://t.co/V7AciakOA8
    at: 2017-08-21 02:22:49
	  via SocialFlow

"""
    assert len(timeline) == 100, "Make sure timeline is the right length"
    modules.print_tweets(timeline[0])
    out, err = capsys.readouterr()
    assert out == desired_output

def test_get_sources(timeline):
    sources = Counter()
    for tweet in timeline:
        modules.get_sources(tweet, sources)

    assert isinstance(sources, Counter)
    assert len(sources) == 2
    assert set(['SocialFlow', 'TweetDeck']).issubset(sources)
    assert sum(sources.values()) == 100
    keys = list(sources.keys())

def test_get_locations(timeline):
    #TODO: get a timeline with some locations
    locations = Counter()
    for tweet in timeline:
        modules.get_locations(tweet, locations)
    assert isinstance(locations, Counter)
    assert len(locations) == 0

def test_get_words(timeline):
    words = Counter()
    for tweet in timeline:
        modules.get_words(tweet, words)

    assert len(words.most_common(5)) == 5
    assert 'eclipse' in words
    assert 'new' in words
    assert 'U.S.' in words

def test_get_sentiment(timeline):
    sentiment = modules.get_sentiment(timeline)
    assert set(['positive', 'negative']).issubset(sentiment)
    assert sum(sentiment.values()) == 100

def test_get_tweets_per_day(timeline):
    dates = [tweet.created_at for tweet in timeline]
    mean  = modules.get_tweets_per_day(dates)
    assert isinstance(mean, float)
    assert mean == 50

