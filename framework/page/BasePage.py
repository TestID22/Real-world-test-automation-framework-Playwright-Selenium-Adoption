from abc import abstractmethod, ABC

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage(ABC):
    """Base class for all page objects in Selenium."""

    # ------------------------
    # Page navigation
    # ------------------------
    @abstractmethod
    def open_url(self, url: str):
        pass

    # ------------------------
    # Element interactions
    # ------------------------
    @abstractmethod
    def find_element(self, locator: tuple):
        pass

    @abstractmethod
    def click(self, locator: tuple):
        pass

    @abstractmethod
    def send_keys(self, locator: tuple, text: str, clear_first: bool = True):
        pass

    @abstractmethod
    def get_text(self, locator: tuple) -> str:
        pass

    @abstractmethod
    def is_visible(self, locator: tuple) -> bool:
        pass

    @abstractmethod
    def is_present(self, locator: tuple) -> bool:
        pass
