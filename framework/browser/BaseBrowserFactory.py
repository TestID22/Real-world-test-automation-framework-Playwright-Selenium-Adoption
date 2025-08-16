from abc import ABC, abstractmethod

from selenium.webdriver.chrome import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class BrowserFactoryBase(ABC):
    """Base class for browser factories with common functionality."""
    """by abstract base class I established a contract to all that will use this base class"""


    @abstractmethod
    def get_browser_driver(self, browser=None, headless=False, **kwargs):
        """Contract for getting a browser driver instance"""
        options = Options()

        if headless:
            options.headless = headless

        if browser == "chrome":
            service = Service(ChromeDriverManager().install())
            driver = webdriver.ChromiumDriver(service=service, options=options)

        return driver

