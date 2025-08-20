import pytest
from configuration.dynamic_imports import BrowserManager
from framework.browser.playwright.playwright_browser_manager import PlaywrightBrowserManager
from framework.browser.selenium.selenium_browser_manager import SeleniumBrowserManager


@pytest.fixture(scope='session')
def browser():
    driver = None
    try:
        if BrowserManager is SeleniumBrowserManager:
            driver = BrowserManager.init_browser(instance_key="main", headless=False)
            print('Browser Initialized')
            print(f'Test framework is Selenium')
            yield driver
        if BrowserManager is PlaywrightBrowserManager:
            driver = BrowserManager.init_browser()
            print('Browser Initialized')
            print(f'Test framework is Playwright')
            yield driver
    finally:
        if driver:
            BrowserManager.close_browser()