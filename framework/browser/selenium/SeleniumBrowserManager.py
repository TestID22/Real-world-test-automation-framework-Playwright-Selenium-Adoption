from framework.browser import BaseBrowserFactory
from framework.browser.BaseBrowserManager import BaseBrowserManager


class SeleniumBrowserManager(BaseBrowserManager):

    def init_browser(cls, browser=None, headless=False, **kwargs):
        driver = BaseBrowserFactory.get_browser_driver(browser=browser, headless=headless, **kwargs)
        return driver
