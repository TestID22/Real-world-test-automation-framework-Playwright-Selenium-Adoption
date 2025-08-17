from pages.GooglePage import GooglePage


def test_one(browser):

    google = GooglePage()
    google.open_new_window("https://www.google.com")
    google.set_search_input("test")

