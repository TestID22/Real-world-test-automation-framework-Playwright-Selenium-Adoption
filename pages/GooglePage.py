from configuration.dynamic_imports import BasePage
from configuration.dynamic_imports import DynamicPageElement
from pages.PageCategory import PageCategory


class GooglePageElements:
    search_input = DynamicPageElement("//*[@name='q']", "search_input")

class GooglePage(BasePage):

    def __init__(self):
        super().__init__(*self.elements.search_input.as_tuple())

    @property
    def elements(self):
        return GooglePageElements

    @property
    def set(self):
        return GooglePageSets(self)


class GooglePageSets(PageCategory):
    def set_search_input(self, key):
        input_element = self.page.elements.search_input.find_element()
        input_element.send_keys(key)
