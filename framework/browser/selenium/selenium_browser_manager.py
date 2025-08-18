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

        cls.driver = driver
        cls._browsers[instance_key] = driver
        cls._active_driver = driver

        if full_screen:
            cls.driver.maximize_window()

        return driver


    @classmethod
    def get_driver(cls) -> WebDriver:
        """Returns the main driver (WebDriver) for the current instance."""
        instance_key = cls._get_active_driver_key()
        return cls._browsers[instance_key] if instance_key else None

    @classmethod
    def close_browser(cls):
        if cls.driver:
            cls.driver.quit()
            cls.driver = None
            cls._active_driver = None

    @classmethod
    def open_url(cls, url):
        cls.driver.get(url)
