import time

import pytest

from configuration.utils.test_step import TestStep
from framework.api.People import People
from pages.GooglePage import GooglePage

# ----------------------------------------------------------------------------------------------------------------------
# @pytest.mark.xfail(reason="just because")
def test_web_test(browser):
    # Page Object
    google = GooglePage()

    with TestStep("1. Open Google page."):
        google.open_url("https://www.google.com")
# ----------------------------------------------------------------------------------------------------------------------
def test_google_request(browser):
    google = GooglePage()
    with TestStep("1. Open Google page."):
        google.open_url("https://www.google.com")
    with TestStep("2. Make a search request."):
        google.set.set_search_input("TEST")
        google.elements.search_input.push_enter()
        time.sleep(1)
# ----------------------------------------------------------------------------------------------------------------------
def test_page_title(browser):
    # page object
    google_page = GooglePage()

    google_page.open_url("https://www.google.com")
    assert google_page.get_page_title() == "Google", "Title is wrong"
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
# Debugging
def test_element_representation_as_tuple_debug(browser):
    google = GooglePage()
    assert tuple is type(google.elements.search_input.as_tuple())
# ----------------------------------------------------------------------------------------------------------------------