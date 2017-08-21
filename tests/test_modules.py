from twitalytics import modules, api
import pytest
import vcr
import tweepy

@pytest.fixture
@vcr.use_cassette('tests/vcr_cassettes/timeline.yml')
def timeline():
    client_api = api.get_api()
    start_date = datetime.datetime.strptime('2016-01-01', '%Y-%m-%d')
    end_date = datetime.datetime.strptime('2017-08-22', '%Y-%m-%d')
    timeline = api.get_timeline('nytimes', 100, client_api, start_date, end_date)
    return timeline

@pytest.fixture
@vcr.use_cassette('tests/vcr_cassettes/user.yml')
def user():
    return client_api.get_user('nytimes')

@pytest.fixture
def client_api():
    client_api = api.get_api()
    return client_api


@vcr.use_cassette('tests/vcr_cassettes/user.yml')
def test_get_user(client_api, capsys):
    user = client_api.get_user('nytimes')
    desired_output = """Information about nytimes:
    Real name: The New York Times
    Description: Where the conversation begins. Follow for breaking news, special reports, RTs of our journalists and more from https://t.co/YapuoqX0HS.
    Website: http://t.co/ahvuWqicF9
    Location: New York City
    Followers: 39,082,046
    Following: 883
    """
    desired_output = desired_output.strip()

    assert isinstance(user, tweepy.models.User)
    modules.get_user(user)
    out, err = capsys.readouterr()
    out = out.strip()
    assert out == desired_output
