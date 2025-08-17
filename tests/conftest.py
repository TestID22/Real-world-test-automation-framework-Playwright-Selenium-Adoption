import pytest
from configuration.dynamic_imports import BrowserManager

@pytest.fixture(scope='session')
def browser():
    driver = BrowserManager.init_browser(instance_key="main", headless=False)
    print('Browser Initialized')
    print(f'Test framework is {BrowserManager}')
    yield driver
    BrowserManager.close_browser()
