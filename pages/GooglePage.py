from selenium.webdriver.common.by import By
from configuration.dynamic_imports import Page


class GooglePageElements:
    google_search_input = (By.XPATH, '//input[@id="search"]', "Google Search Input")


class GooglePage(Page):

    def __init__(self):
        super().__init__(By.XPATH, "//title[text()='Google']", "google_start_page")



# class GooglePageClicks(Element):
#
#     def search_button_click(self):
#         pass