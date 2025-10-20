from selenium.webdriver.chrome.webdriver import WebDriver

from framework.browser.selenium.selenium_browser_manager import SeleniumBrowserManager
from framework.page.base_page import BasePage


class SeleniumBasePage(BasePage):
    """Base class for all page objects in Selenium."""

    # call is in SelenBasePage
    @staticmethod
    def open_url(url):
        SeleniumBrowserManager.open_url(url)

    @property
    def driver(self) -> WebDriver:
        return SeleniumBrowserManager.get_driver()

    def get_page_title(self):
        return self.driver.title
