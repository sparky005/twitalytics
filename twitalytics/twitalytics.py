import sys
import argparse
import datetime
from collections import Counter
from .modules import *
from .api import *


def make_date(date_string):
    """Convert user input to a date type"""
    try:
        return datetime.datetime.strptime(date_string, '%Y-%m-%d')
    except ValueError:
        raise argparse.ArgumentTypeError(date_string + " is not a proper date.")


def parse_arguments(argv):
    parser = argparse.ArgumentParser(argv)
    parser.add_argument(
        "-u",
        "--users",
        "--user",
        nargs='*',
        metavar="username",
        required=True,
        help="User(s) to get information about."
    )
    parser.add_argument(
        "-c",
        "--count",
        type=int,
        default=100,
        metavar="int",
        help="Number of tweets to fetch (Default 100)"
    )
    parser.add_argument(
        "-p",
        "--print",
        action='store_true',
        help="Optionally print gathered tweets"
    )
    parser.add_argument(
        "-d",
        "--devices",
        action='store_true',
        help="Show most frequently used devices"
    )
    parser.add_argument(
        "-l",
        "--locations",
        action='store_true',
        help="Show most frequent locations"
    )
    parser.add_argument(
        "-w",
        "--words",
        action='store_true',
        help="Show most frequently used words."
    )
    parser.add_argument(
        "--start",
        type=make_date,
        default='1970-01-01',
        metavar="start_date",
        help="Starting date for tweets in ISO 8601 format"
    )
    parser.add_argument(
        "--end",
        type=make_date,
        default=datetime.datetime.now(),
        metavar="end_date",
        help="Ending date for tweets in ISO 8601 format"
    )
    parser.add_argument(
        "--tweets_per_day",
        "--tpd",
        action='store_true',
        help="Calculate and print average number of tweets per day",
    )
    parser.add_argument(
        "-s",
        "--sentiment",
        action='store_true',
        help="Classify tweets by sentiment"
    )
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    args = parser.parse_args()
    return args


def main(argv=None):
    api = get_api()
    args = parse_arguments(argv)

    # fix off by one error on end date
    args.end += datetime.timedelta(days=1)

    # do API stuff here so we only do it once per user
    for handle in args.users:
        # get information from api
        try:
            user = api.get_user(handle)
            timeline = get_timeline(handle, args.count, api, args.start, args.end)
        except tweepy.TweepError:
            print("Error: Couldn't query twitter API. Quitting!")
            sys.exit(1)

        # create some collections to hold information
        sources = Counter()
        locations = Counter()
        words = Counter()
        dates = []

        # first, print general user information
        get_user(user)
        # use flag to ensure "last tweets" head only prints once
        print_flag = True
        for tweet in timeline:
            sources = get_sources(tweet, sources)
            locations = get_locations(tweet, locations)
            words = get_words(tweet, words)
            dates.append(tweet.created_at)
            if(args.print):
                if(print_flag):
                    print("\n    Last tweets: ")
                    # make sure we don't print this header again
                    print_flag = False
                print_tweets(tweet)
        if(args.devices):
            print('\nTop devices:')
            total = sum(sources.values())
            for source in sources:
                print('%s: %.2f%%' % (source, sources[source]/total*100))
        if(args.locations):
            print('\nTop locations:')
            total = sum(locations.values())
            for location in locations:
                print('%s: %.2f%%' % (location, locations[location]/total*100))
        if(args.words):
            # not sure if we want to do percentages here
            print(words.most_common(10))
        if(args.tweets_per_day):
            tpd = get_tweets_per_day(dates)
            print('\nAverage number of tweets per day: %.2f' % tpd)
        if(args.sentiment):
            sentiments = get_sentiment(timeline)
            total = sum(sentiments.values())
            for sentiment in sentiments:
                print('%s: %.2f%%' % (sentiment, sentiments[sentiment]/total*100))

