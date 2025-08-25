import requests
from framework.api.People import People
from pages.GooglePage import GooglePage


def test_one(browser):

    google = GooglePage()
    google.open_new_window("https://www.google.com")


def test_api():
    response = People.get_people(1)
    print(response.json()['name'])