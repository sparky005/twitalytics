import sys
import argparse
import datetime
from .modules import *
from .api import *


def make_date(date_string):
    """Convert user input to a date type"""
    try:
        return datetime.datetime.strptime(date_string, '%Y-%m-%d')
    except ValueError:
        raise argparse.ArgumentTypeError(date_string + " is not a proper date.")


def parse_arguments():
    parser = argparse.ArgumentParser()
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
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    args = parser.parse_args()
    return args


def main():
    api = get_api()
    args = parse_arguments()

    # fix off by one error on end date
    args.end += datetime.timedelta(days=1)

    # do API stuff here so we only do it once per user
    for handle in args.users:
        # get information from api
        try:
            user = api.get_user(handle)
            timeline = get_timeline(handle, args.count, api, args.start, args.end)
        except tweepy.TweepError:
            print("Error: Couldn't query tweepy API. Quitting!")
            sys.exit(1)

        get_general(user, timeline, args.print)
        if(args.devices):
            get_sources(timeline)
