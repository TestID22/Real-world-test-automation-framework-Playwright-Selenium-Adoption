from framework.browser.base_browser_manager import BaseBrowserManager
from framework.browser.playwright.playwright_browser_factory import PlaywrightBrowserFactory


class PlaywrightBrowserManager(BaseBrowserManager):
    driver_instance = None
    playwright_instance = None

    @classmethod
    def init_browser(cls, browser=None, headless=False, **kwargs):
        """Contract for getting a browser driver instance"""

        driver = PlaywrightBrowserFactory.get_browser_driver(headless=headless, **kwargs)
        cls.driver_instance = driver.page
        cls.playwright_instance = driver
        return driver.page

    @classmethod
    def close_browser(cls):
        """Contract for closing browser. Abstract method implementation."""
        if cls.playwright_instance:
            cls.playwright_instance.page.close()
            cls.playwright_instance.browser_context.close()
            cls.playwright_instance.browser.close()
