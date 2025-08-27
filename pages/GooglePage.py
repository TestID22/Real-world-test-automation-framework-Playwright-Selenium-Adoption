from abc import ABC

from configuration.dynamic_imports import BasePage
from configuration.dynamic_imports import DynamicPageElement


class GooglePageElements:
    search_input = DynamicPageElement("//*[@name='q']", "search_input")

class GooglePage(BasePage):

    def __init__(self):
        super().__init__("xpath", "//title[text()='Google']", "google_start_page")

    @property
    def elements(self):
        return GooglePageElements

    def set_search_input(self, key):
        input_element = self.elements.search_input.find_element()
        input_element.send_keys(key)
