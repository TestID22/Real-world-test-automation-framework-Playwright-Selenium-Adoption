import pytest

from framework.api.People import People
from pages.GooglePage import GooglePage

# ----------------------------------------------------------------------------------------------------------------------
# @pytest.mark.xfail(reason="just because")
def test_web_test(browser):
    # Page Object
    google = GooglePage()
    google.open_url("https://www.google.com")
# ----------------------------------------------------------------------------------------------------------------------\
def test_static_page_open(browser):
    # page object
    google_page = GooglePage()

    google_page.open_url("https://www.google.com")
    assert google_page.driver.title == "Google", "Title is wrong"  # TODO: move get_title to BaseClass and implement both
    # options for Playwright and Selenium
#-----------------------------------------------------------------------------------------------------------------------
@pytest.mark.regression
@pytest.mark.api
def test_first_person():
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
def test_first_name_person(name):
    assert name == People.get_people(1).json()['name'].lower().split()[0]
# ----------------------------------------------------------------------------------------------------------------------

