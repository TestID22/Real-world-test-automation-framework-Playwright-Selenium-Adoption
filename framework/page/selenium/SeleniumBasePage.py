from framework.browser.selenium.SeleniumBrowserManager import SeleniumBrowserManager
from framework.page.BasePage import BasePage

class SeleniumBasePage(BasePage):
    """Base class for all page objects in Selenium."""

    @property
    def driver(self):
        return SeleniumBrowserManager.driver

    def open_new_window(self, url):
        self.driver.get(url)
