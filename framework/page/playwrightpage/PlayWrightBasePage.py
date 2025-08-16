from framework.browser.playwright.PlaywrightBrowserManager import PlaywrightBrowserManager
from framework.page.BasePage import BasePage


class PlayWrightBasePage(BasePage):
    """Base class for all page objects in Selenium."""

    def driver(self):
        return PlaywrightBrowserManager

    def open_new_window(self, url):
        self.driver().driver.page.goto(url)


