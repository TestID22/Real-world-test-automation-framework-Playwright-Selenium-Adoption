
from framework.browser.BaseBrowserManager import BaseBrowserManager
from framework.browser.selenium.SeleniumBrowserFactory import SeleniumBrowserFactory


class SeleniumBrowserManager(BaseBrowserManager):

    def init_browser(self, browser=None, headless=False, **kwargs):
        driver = SeleniumBrowserFactory.get_browser_driver(browser=browser, headless=headless, **kwargs)
        return driver

