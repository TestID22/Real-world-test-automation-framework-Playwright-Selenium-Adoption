from framework.browser.BaseBrowserManager import BaseBrowserManager
from framework.browser.playwright.PlaywrightBrowserFactory import PlaywrightBrowserFactory


class PlaywrightBrowserManager(BaseBrowserManager):
    driver = None


    @classmethod
    def init_browser(self, browser=None, headless=False, **kwargs):
        """Contract for getting a browser driver instance"""

        driver = PlaywrightBrowserFactory.get_browser_driver(headless=headless, **kwargs)
        return driver.page

    @classmethod
    def close_browser(cls):
        """Contract for closing browser"""
        if cls.driver:
            cls.driver.page.close()
            cls.driver.browser_context.close()
            cls.driver.page.close()

