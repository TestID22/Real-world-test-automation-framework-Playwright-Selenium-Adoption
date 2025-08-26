import pytest

from framework.api.People import People
from pages.GooglePage import GooglePage

# ----------------------------------------------------------------------------------------------------------------------
@pytest.mark.xfail(reason="just because")
def test_one(browser):
    google = GooglePage()
    google.open_new_window("https://www.google.com")
# ----------------------------------------------------------------------------------------------------------------------
@pytest.mark.regression
def test_api():
    expected_name = "Luke Skywalker".lower()
    response = People.get_people(1)
    assert response.status_code == 200
    actual_name = response.json()['name']
    assert expected_name == actual_name.lower(), "Luke Skywalker's name is not correct."
# ----------------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("a,b,result", [(1,2,3), (5,6,11)])
def test_sum(a,b,result):
    assert a + b == result
# ----------------------------------------------------------------------------------------------------------------------
LUKE = 'luke'

@pytest.mark.parametrize("name", [LUKE])
def test_sum(name):
    assert name == People.get_people(1).json()['name'].lower().split()[0]
# ----------------------------------------------------------------------------------------------------------------------

