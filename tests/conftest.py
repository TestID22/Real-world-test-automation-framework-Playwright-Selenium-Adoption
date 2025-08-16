from configuration.dynamic_imports import BrowserManager
import pytest
"""
BrowserManager class it's a generic (like in Java) 
"""

@pytest.fixture(scope='session')
def browser():
    driver = BrowserManager.init_browser(headless=False)
    print('Browser Initialized')
    print(f'Test framework is {BrowserManager}')
    yield driver
    BrowserManager.close_browser()


@pytest.fixture(scope='session')
def browser_manager(request):
    return BrowserManager()


def pytest_addoption(parser):
    parser.addoption(
        "--framework",
        action="store",
        default=None,
        help="Choose test framework: selenium or playwright"
    )

@pytest.fixture(scope="session", autouse=True)
def select_framework(pytestconfig):
    framework = pytestconfig.getoption("framework")
    if framework:
        import os
        os.environ["TEST_FRAMEWORK"] = framework
