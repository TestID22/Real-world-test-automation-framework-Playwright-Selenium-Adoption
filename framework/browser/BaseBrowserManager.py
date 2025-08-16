from abc import ABC, abstractmethod


class BaseBrowserManager(ABC):

    @classmethod
    @abstractmethod
    def init_browser(cls, instance_key=None, **kwargs):
        pass

    @classmethod
    @abstractmethod
    def close_browser(cls):
        pass
