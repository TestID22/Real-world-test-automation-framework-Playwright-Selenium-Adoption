import time

import pytest

from configuration.utils.test_step import TestStep
from framework.api.People import People
from pages.GooglePage import GooglePage
from pages.SwagLabsLoginPage import SwagLabsLoginPage
from pages.SwagLabsProductsPage import SwagLabsProductsPage


# ----------------------------------------------------------------------------------------------------------------------
# @pytest.mark.xfail(reason="just because") doesn't make sense as Starter page is set up in conftest
# def test_web_test(browser):
#     Page Object
    # google = GooglePage()
    #
    # with TestStep("1. Open Google page."):
    #     google.open_url("https://www.google.com") # use
# ----------------------------------------------------------------------------------------------------------------------
def test_login(browser, config):
    # Page Object
    swag_lab_page = SwagLabsLoginPage()
    swag_products_page = SwagLabsProductsPage()

    with TestStep("1: Login with correct credentials"):
        swag_lab_page.login(config['test_user']["username"], config['test_user']["password"])
        swag_lab_page.click.click_login_button()

    with TestStep("2: Check that page is opened. Check for inventory Title"):
        swag_products_page.elements.inventory_title.wait_for_text_visible("Products")
# ----------------------------------------------------------------------------------------------------------------------
def test_page_title(browser):
    # page object
    google_page = GooglePage()

    with TestStep("1. Check the Google Title"):
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

    with TestStep("1. Make a summation request."):
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