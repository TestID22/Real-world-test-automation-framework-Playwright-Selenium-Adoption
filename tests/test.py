from pages.google_page import GooglePage


def test_one(browser):

    google = GooglePage()
    google.open_new_window("https://www.google.com")
