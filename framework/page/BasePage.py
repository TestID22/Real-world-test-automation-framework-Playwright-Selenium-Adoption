from abc import abstractmethod, ABC


class BasePage(ABC):
    """Base class for all page objects in Selenium."""
    def __init__(self, search_condition, locator, page_name):
        self.locator = locator
        self.search_condition = search_condition
        self.page_name = page_name

    @property
    @abstractmethod
    def driver(self):
        pass

    @staticmethod
    @abstractmethod
    def open_new_window(url):
        pass


