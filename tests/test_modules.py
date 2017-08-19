from twitalytics import modules

def test_get_user(capsys):
    modules.get_user('sparky_005')
    out, error = capsys.readouterror()
    assert out.contains('hi')

