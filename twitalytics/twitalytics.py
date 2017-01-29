from .api import *

def main():
    api = get_api()
    api.update_status('hi')
