from abc import ABC, abstractmethod


class BaseBrowserManager(ABC):
    _browsers = {}
    _context_stacks = {}
    _generic_key_counter = 1
    _instance_key = None
    _active_driver = None
    __main_window_handle = None

    # This method returns the key of the currently active driver
    # this gives opportunity to define driver which we can work with
    @classmethod
    def _get_active_driver_key(cls):
        for key, driver in cls._browsers.items():
            if driver == cls._active_driver:
                return key
        return None

    @classmethod
    @abstractmethod
    def init_browser(cls, instance_key=None, **kwargs):
        pass

    @classmethod
    @abstractmethod
    def close_browser(cls):
        pass
