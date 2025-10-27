import requests


def test_users(app_url):
    response = requests.get(app_url + "/api/users")
    assert response.status_code == 200