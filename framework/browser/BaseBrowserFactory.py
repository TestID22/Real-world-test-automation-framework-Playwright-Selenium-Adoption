from abc import ABC, abstractmethod


class BrowserFactoryBase(ABC):
    """Base class for browser factories with common functionality."""
    """by abstract base class I established a contract to all that will use this base class"""


    @abstractmethod
    def get_browser_driver(self, browser=None, headless=False, **kwargs):
        """Contract for getting a browser driver instance"""
        pass

