from abc import ABC

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from framework.browser.selenium.SeleniumBrowserManager import SeleniumBrowserManager
from framework.page.BasePage import BasePage


class SeleniumBasePage(BasePage):
    """Base class for all page objects in Selenium."""

    def driver(self):
        return SeleniumBrowserManager.driver

    def open_new_window(self, url):
        self.driver().get(url)



