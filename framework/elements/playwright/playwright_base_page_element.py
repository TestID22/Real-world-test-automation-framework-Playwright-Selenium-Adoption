from playwright.sync_api import expect
from playwright.sync_api import Page

from configuration.dynamic_imports import BrowserManager
from framework.elements.base_page_element import BasePageElement

class PlayWrightPageElement(BasePageElement):

    @property
    def driver(self) -> Page:
        driver = BrowserManager.get_driver()
        if driver is None:
            raise Exception("webdriver error")
        return driver

    def click(self):
        self.find_element().first.click()

    def push_enter(self):
        self.driver.keyboard.down("Enter")

    def send_keys(self, key):
        self.find_element().fill(key)

    def locator(self):
        return super()._locator

    def find_element(self):
        return self.driver.locator(f"{self._search_condition}={self._locator}")

    def as_tuple(self):
        return self._search_condition, self._locator, self._element_name

    def wait_for_text_visible(self, text):
        locator = self.find_element()
        expect(locator).to_have_text(text)

    def execute_script(self, script):
        self.driver.evaluate(script)

