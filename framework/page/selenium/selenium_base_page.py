from framework.browser.selenium.selenium_browser_manager import SeleniumBrowserManager
from framework.page.base_page import BasePage

class SeleniumBasePage(BasePage):
    """Base class for all page objects in Selenium."""

    @property
    def driver(self):
        return SeleniumBrowserManager.driver

    def open_new_window(self, url):
        self.driver.get(url)
