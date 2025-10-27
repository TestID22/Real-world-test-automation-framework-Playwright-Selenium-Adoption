import json
import os
import dotenv
import pytest

from configuration.constants.urls import URL
from configuration.dynamic_imports import BrowserManager
from framework.browser.playwright.playwright_browser_manager import PlaywrightBrowserManager
from framework.browser.selenium.selenium_browser_manager import SeleniumBrowserManager


@pytest.fixture(scope="session")
def config():
    with open("configuration/test_env.json") as f:
        return json.load(f)


@pytest.fixture(autouse=True)
def envs():
    dotenv.load_dotenv()


@pytest.fixture
def app_url():
    return os.getenv("APPLICATION_URL")


@pytest.fixture(scope='session')
def browser():
    driver = None
    try:
        if BrowserManager is SeleniumBrowserManager:
            driver = BrowserManager.init_browser(instance_key=1, headless=False)
            print('Browser Initialized')
            print(f'Test framework is Selenium')
            driver.get(URL.DEMO)
            yield driver
        if BrowserManager is PlaywrightBrowserManager:
            driver = BrowserManager.init_browser(instance_key=1, headless=False)
            print('Browser Initialized')
            print(f'Test framework is Playwright')
            driver.goto(URL.DEMO)
            yield driver
    finally:
        if driver:
            BrowserManager.close_browser()

