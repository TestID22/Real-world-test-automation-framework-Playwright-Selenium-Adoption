import requests
from configuration.constants.APIpathes import APIpathes


def test_users(app_url):
    response = requests.get(f"{app_url}{APIpathes.USERS_URL}")
    assert response.status_code == 200