import pytest
import requests
from http import HTTPStatus

from configuration.constants.APIpathes import APIpathes


@pytest.fixture
def users(app_url):
    response = requests.get(f"{app_url}{APIpathes.USERS_URL}")
    assert response.status_code == HTTPStatus.OK
    return response.json()


def test_users(app_url):
    response = requests.get(f"{app_url}{APIpathes.USERS_URL}")
    assert response.status_code == HTTPStatus.OK, "Users API call failed"


@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_user_exists(app_url, user_id):
    response = requests.get(f"{app_url}{APIpathes.USERS_URL}/{user_id}")
    assert response.status_code == HTTPStatus.OK


def test_duplicate_users(app_url, users):
    response = requests.get(f"{app_url}{APIpathes.USERS_URL}")
    assert response.status_code == HTTPStatus.OK
    user_ids = [user['id'] for user in users]
    assert len(user_ids) == len(set(user_ids)), "There are duplicate users"
