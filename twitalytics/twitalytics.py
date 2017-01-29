import argparse
import sys
from .modules import *
from .api import *

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--test", action = 'store_true', help="This is a test")
    parser.add_argument("-u", "--users", "--user", nargs='*', metavar="username", help="User(s) to get information about.")
    parser.add_argument("-c", "--count", type=int, default=3, metavar="int", help="Number of tweets to fetch.")
    if len(sys.argv)==1:
        parser.print_help()
        sys.exit(1)
    args = parser.parse_args()
    return args

def main():
    api = get_api()
    args = parse_arguments()
    if args.test:
        print("test confirmed")
    if args.users:
        get_general(args.users, args.count, api)