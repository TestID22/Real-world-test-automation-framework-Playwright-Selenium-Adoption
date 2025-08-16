from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from framework.page.BasePage import BasePage


class SeleniumBasePage(BasePage):
    """Base class for all page objects in Selenium."""

    def __init__(self, driver: WebDriver, timeout: int = 10):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver, timeout)

    # ------------------------
    # Page navigation
    # ------------------------
    def open_url(self, url: str):
        """Navigate to the given URL."""
        self.driver.get(url)

    # ------------------------
    # Element interactions
    # ------------------------
    def find_element(self, locator: tuple):
        """Find a single element with wait."""
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            raise Exception(f"Element {locator} not found within {self.timeout} seconds")

    def click(self, locator: tuple):
        """Click an element after waiting for it to be clickable."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def send_keys(self, locator: tuple, text: str, clear_first: bool = True):
        """Send keys to an input element."""
        element = self.find_element(locator)
        if clear_first:
            element.clear()
        element.send_keys(text)

    def get_text(self, locator: tuple) -> str:
        """Get text from an element."""
        element = self.find_element(locator)
        return element.text

    def is_visible(self, locator: tuple) -> bool:
        """Check if an element is visible."""
        try:
            return self.wait.until(EC.visibility_of_element_located(locator)) is not None
        except TimeoutException:
            return False

    def is_present(self, locator: tuple) -> bool:
        """Check if an element exists in DOM (may not be visible)."""
        try:
            self.driver.find_element(*locator)
            return True
        except:
            return False
