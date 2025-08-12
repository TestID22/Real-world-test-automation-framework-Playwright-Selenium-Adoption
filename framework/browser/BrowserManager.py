from abc import ABC, abstractmethod


class BaseBrowserManager(ABC):

    @classmethod
    @abstractmethod
    def start_browser(cls, key):
        pass

