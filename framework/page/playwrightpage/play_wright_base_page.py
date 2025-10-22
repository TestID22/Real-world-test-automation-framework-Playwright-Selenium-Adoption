from framework.browser.playwright.playwright_browser_manager import PlaywrightBrowserManager
from framework.page.base_page import BasePage


class PlayWrightBasePage(BasePage):
    """Base class for all page objects in Selenium."""

    @staticmethod
    def open_url(url):
        PlaywrightBrowserManager.page_instance.goto(url)

    @property
    def driver(self):
        return PlaywrightBrowserManager.get_driver()

    def get_page_title(self):
        return PlaywrightBrowserManager.page_instance.title()
