from framework.browser.base_browser_manager import BaseBrowserManager
from framework.browser.playwright.playwright_browser_factory import PlaywrightBrowserFactory


class PlaywrightBrowserManager(BaseBrowserManager):
    page_instance = None
    playwright_instance = None

    @classmethod
    def init_browser(cls, instance_key=None, browser=None, headless=False, **kwargs):
        """Contract for getting a page instance"""

        driver = PlaywrightBrowserFactory.get_browser_driver(headless=headless, **kwargs)

        if instance_key is None:
            instance_key = 1

        cls.page_instance = driver.page
        cls.playwright_instance = driver
        cls._browsers[instance_key] = driver
        return cls.page_instance

    @classmethod
    def close_browser(cls):
        """Contract for closing browser. Abstract method implementation."""
        if cls.playwright_instance:
            cls.playwright_instance.page.close()
            cls.playwright_instance.browser_context.close()
            cls.playwright_instance.browser.close()

    @classmethod
    def get_driver(cls):
        """Returns the main Page representation (Page) for the current instance."""
        return cls.page_instance

    @classmethod
    def open_url(cls, url):
        cls.page_instance.goto(url)
