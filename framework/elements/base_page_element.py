from abc import ABC, abstractmethod
from selenium.webdriver.common.by import By


class BasePageElement(ABC):

    def __init__(self, locator, element_name, search_condition=By.XPATH):
        self._search_condition = search_condition
        self._locator = locator
        self._element_name = element_name

    @property
    @abstractmethod
    def driver(self):
        pass

    @abstractmethod
    def find_element(self):
        pass

    @abstractmethod
    def locator(self):
        pass


    @abstractmethod
    def as_tuple(self):
        pass

    @abstractmethod
    def send_keys(self, key):
        pass

    @abstractmethod
    def push_enter(self):
        pass