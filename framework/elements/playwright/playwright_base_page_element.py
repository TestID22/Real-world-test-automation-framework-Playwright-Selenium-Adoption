from selenium.webdriver.common.keys import Keys
from playwright.sync_api import Page, FrameLocator

from configuration.dynamic_imports import BrowserManager
from framework.elements.base_page_element import BasePageElement


class PlayWrightPageElement(BasePageElement):

    def push_enter(self):
        self.find_element().fill(Keys.ENTER)

    def send_keys(self, key):
        self.find_element().fill(key)

    def locator(self):
        return super()._locator

    @property
    def driver(self):
        driver = BrowserManager.get_driver()
        if driver is None:
            raise Exception("webdriver error")
        return driver

    def find_element(self):
        return self.driver.locator(f"{self._search_condition}={self._locator}")

    def as_tuple(self):
        return self._search_condition, self._locator, self._element_name
