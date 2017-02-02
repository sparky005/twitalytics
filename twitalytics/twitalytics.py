import sys
import argparse
from .modules import *
from .api import *


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-t", "--test",
        action='store_true',
        help="This is a test"
    )
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
        help="Number of tweets to fetch."
    )
    parser.add_argument(
        "-p",
        "--print",
        action='store_true',
        help="Print gathered tweets"
    )
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    args = parser.parse_args()
    return args


def main():
    api = get_api()
    args = parse_arguments()
    # do API stuff here so we only do it once per user
    for handle in args.users:
        # get information from api
        try:
            user = api.get_user(handle)
            timeline = get_timeline(handle, args.count, api)
        except tweepy.TweepError:
            print("Error: Couldn't query tweepy API. Quitting!")
            sys.exit(1)

        if args.test:
            print("test confirmed")
        if args.users:
            get_general(user, timeline, args.print)