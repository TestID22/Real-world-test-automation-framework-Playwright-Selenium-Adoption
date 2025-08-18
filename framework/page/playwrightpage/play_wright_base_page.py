from framework.browser.playwright.playwright_browser_manager import PlaywrightBrowserManager
from framework.page.base_page import BasePage


class PlayWrightBasePage(BasePage):
    """Base class for all page objects in Selenium."""

    @property
    def driver(self):
        return PlaywrightBrowserManager

    def open_new_window(self, url):
        self.driver().driver_instance.goto(url)
