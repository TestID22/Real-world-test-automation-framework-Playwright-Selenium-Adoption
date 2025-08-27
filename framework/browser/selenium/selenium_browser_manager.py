from selenium.webdriver.chrome.webdriver import WebDriver

from configuration.constants.Browser import Browser
from framework.browser.base_browser_manager import BaseBrowserManager
from framework.browser.selenium.selenium_browser_factory import SeleniumBrowserFactory


class SeleniumBrowserManager(BaseBrowserManager):
    """
    to initialize driver
    """
    driver = None

    @classmethod
    def init_browser(cls, instance_key=None, browser=Browser.CHROME, headless=False, full_screen=True, **kwargs):
        driver = SeleniumBrowserFactory.get_browser_driver(
            browser=browser,
            headless=headless,
            **kwargs
        )

        cls._browsers[instance_key] = driver
        cls._active_driver = driver

        if full_screen:
            cls._browsers[instance_key].maximize_window()
        return driver

    @classmethod
    def get_driver(cls) -> WebDriver:
        """Returns the main driver (WebDriver) for the current instance."""
        instance_key = cls._get_active_driver_key()
        return cls._browsers[instance_key] if instance_key else None

    # close_browser:
    #   - Gets the current active driver key
    #   - Quits the corresponding browser instance
    #   - Resets cls.driver and cls._active_driver to None
    @classmethod
    def close_browser(cls):
        instance_key = cls._get_active_driver_key()
        if cls._browsers[instance_key]:
            cls._browsers[instance_key].quit()
            cls.driver_instance = None
            cls._active_driver = None

    @classmethod
    def open_url(cls, url):
        cls.get_driver().get(url)
