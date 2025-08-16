import pytest

from configuration.constants.Browser import Browser
from configuration.dynamic_imports import BrowserManager



@pytest.fixture(scope='session')
def browser(request):
    browser = BrowserManager().init_browser(browser=Browser.FIREFOX, headless=False)
    return browser

