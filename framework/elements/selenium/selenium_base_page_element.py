from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from framework.elements.base_page_element import BasePageElement
from configuration.dynamic_imports import BrowserManager

class SeleniumBasePageElement(BasePageElement):

    def locator(self):
        return super()._locator

    @property
    def driver(self) -> WebDriver:
        driver = BrowserManager.get_driver()
        if driver is None:
            raise Exception("webdriver error")
        return driver

    def find_element(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((self._search_condition, self._locator))
        )

    def as_tuple(self):
        return self._search_condition, self._locator, self._element_name
