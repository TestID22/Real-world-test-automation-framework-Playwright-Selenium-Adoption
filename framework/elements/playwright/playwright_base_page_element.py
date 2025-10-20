from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from configuration.dynamic_imports import BrowserManager
from framework.elements.base_page_element import BasePageElement


class PlayWrightPageElement(BasePageElement):

    def locator(self):
        return super()._locator

    @property
    def driver(self):
        driver = BrowserManager.get_driver()
        if driver is None:
            raise Exception("webdriver error")
        return driver

    def find_element(self):
        return NonImplemented
