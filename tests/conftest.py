import pytest

from configuration.dynamic_imports import BrowserManager



@pytest.fixture(scope='session')
def browser(request):
    browser = 'chrome'
    browser = BrowserManager().init_browser(browser=browser, headless=False)
    return browser

