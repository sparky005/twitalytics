import pytest
import vcr
from twitalytics import api
import datetime

@pytest.fixture
@vcr.use_cassette('tests/vcr_cassettes/timeline.yml')
def timeline():
    client_api = api.get_api()
    start_date = datetime.datetime.strptime('2016-01-01', '%Y-%m-%d')
    end_date = datetime.datetime.strptime('2017-08-22', '%Y-%m-%d')
    timeline = api.get_timeline('nytimes', 100, client_api, start_date, end_date)
    return timeline

@pytest.fixture
def client_api():
    client_api = api.get_api()
    return client_api

@pytest.fixture
def user_info():
    return """Information about nytimes:
    Real name: The New York Times
    Description: Where the conversation begins. Follow for breaking news, special reports, RTs of our journalists and more from https://t.co/YapuoqX0HS.
    Website: http://t.co/ahvuWqicF9
    Location: New York City
    Followers: 39,082,046
    Following: 883
    """
