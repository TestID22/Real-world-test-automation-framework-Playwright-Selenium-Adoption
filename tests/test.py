from pages.GooglePage import GooglePage


def test_one(browser):
    # browser.goto("https://www.google.com")
    google = GooglePage()


    google.google_search_input.driver.get("https://www.google.com")