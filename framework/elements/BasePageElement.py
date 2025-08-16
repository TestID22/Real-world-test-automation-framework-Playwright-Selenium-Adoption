from abc import ABC, abstractmethod


class BasePageElement(ABC):

    @abstractmethod
    def driver(self):
        pass