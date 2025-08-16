from framework.browser.BaseBrowserManager import BaseBrowserManager
from framework.browser.playwright.PlaywrightBrowserFactory import PlaywrightBrowserFactory


class PlaywrightBrowserManager(BaseBrowserManager):

    def init_browser(self, browser=None, headless=False, **kwargs):
        """Contract for getting a browser driver instance"""

        driver = PlaywrightBrowserFactory.get_browser_driver(headless=headless, **kwargs)
        return driver.page