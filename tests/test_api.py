from twitalytics import api
import vcr
import pytest
import datetime

@pytest.fixture
def client_api():
    client_api = api.get_api()
    return client_api

@vcr.use_cassette('tests/vcr_cassettes/timeline.yml')
def test_get_timeline(capsys, client_api):
    start_date = datetime.datetime.strptime('2016-01-01', '%Y-%m-%d')
    end_date = datetime.datetime.strptime('2017-08-20', '%Y-%m-%d')
    timeline = api.get_timeline('cnn', 100, client_api, start_date, end_date)
    assert len(timeline) == 100, "Should get 100 tweets"
