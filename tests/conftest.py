from configuration.dynamic_imports import BrowserManager
import pytest
"""
BrowserManager class it's a generic (like in Java) 
"""

@pytest.fixture(scope='session')
def browser():
    driver = BrowserManager.init_browser(headless=False)
    yield driver
    BrowserManager.close_browser()


@pytest.fixture(scope='session')
def browser_manager(request):
    return BrowserManager()
