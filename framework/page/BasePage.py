from abc import abstractmethod, ABC

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage(ABC):
    """Base class for all page objects in Selenium."""

    @abstractmethod
    def driver(self):
        pass

    @staticmethod
    @abstractmethod
    def open_new_window(url):
        pass


