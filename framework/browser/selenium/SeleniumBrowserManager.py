from configuration.constants.Browser import Browser
from framework.browser.BaseBrowserManager import BaseBrowserManager
from framework.browser.selenium.SeleniumBrowserFactory import SeleniumBrowserFactory


class SeleniumBrowserManager(BaseBrowserManager):
    """
    to initialize driver
    """
    driver = None

    @classmethod
    def init_browser(cls, browser=Browser.CHROME, headless=False, **kwargs):
        driver = SeleniumBrowserFactory.get_browser_driver(browser=browser, headless=headless, **kwargs)
        return driver

    @classmethod
    def close_browser(cls):
        if cls.driver:
            cls.driver.quit()
            cls.driver = None


