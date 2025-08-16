from configuration.constants.Browser import Browser
from framework.browser.BaseBrowserFactory import BrowserFactoryBase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class SeleniumBrowserFactory(BrowserFactoryBase):

    @classmethod
    def get_browser_driver(cls, browser=None, headless=False, **kwargs):
        """Contract for getting a browser driver instance"""

        if browser == Browser.CHROME:
            driver_instance = cls.__get_chrome_driver(browser=browser, headless=headless)

        return driver_instance

    @classmethod
    def __get_chrome_driver(cls, browser=None, headless=False, **kwargs):
        options = Options()

        if headless:
            options.headless = True

        driver = webdriver.Chrome()
        return driver


