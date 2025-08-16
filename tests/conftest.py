import pytest

from framework.browser.BaseBrowserManager import BaseBrowserManager


@pytest.fixture(scope='session')
def browser(request, browser_manager) -> BaseBrowserManager:
    browser = BaseBrowserManager.init_browser()
    return browser

@pytest.fixture
def browser_manager() -> BrowserManager:
    return BrowserManager()