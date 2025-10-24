from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

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

    def click(self):
        self.find_element().click()

    def as_tuple(self):
        return self._search_condition, self._locator, self._element_name

    def push_enter(self):
        self.send_keys(Keys.ENTER)

    def send_keys(self, key):
        self.find_element().send_keys(key)

    def execute_script(self, script):
        self.driver.execute_script(script)

    def wait_for_text_visible(self, text, timeout=5):
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element((self._search_condition, self._locator), text)
        )
        return self.find_element()