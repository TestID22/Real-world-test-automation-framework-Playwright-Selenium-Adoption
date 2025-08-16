from configuration.constants.Browser import Browser
from framework.browser.BaseBrowserFactory import BaseBrowserFactory

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class SeleniumBrowserFactory(BaseBrowserFactory):
    """
    To set up driver
    """
    @classmethod
    def get_browser_driver(cls, browser: str=None, headless: bool=None, **kwargs):
        """Contract for getting a browser driver instance"""

        if browser == Browser.CHROME:
            return cls.__get_chrome_driver(headless=headless)
        if browser == Browser.FIREFOX:
            return cls.__get_gecko_driver(headless=headless)
        raise ValueError(f"Browser '{browser}' is not supported")

    @staticmethod
    def __get_chrome_driver(headless: bool = False):
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless")
        service = ChromeService(ChromeDriverManager().install())
        return webdriver.Chrome(service=service, options=options)

    @classmethod
    def __get_gecko_driver(cls, headless: bool=False):
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")

        service = FirefoxService(GeckoDriverManager().install())
        return webdriver.Firefox(service=service, options=options)
