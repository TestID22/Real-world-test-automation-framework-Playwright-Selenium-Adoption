import pytest

from framework.browser.BaseBrowserManager import BaseBrowserManager


@pytest.fixture(scope='session')
def browser(request) -> BaseBrowserManager:

    browser = BaseBrowserManager.init_browser()
    return browser

