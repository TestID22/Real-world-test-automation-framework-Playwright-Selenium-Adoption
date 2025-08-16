import os
import dotenv

dotenv.load_dotenv()

test_framework = os.getenv("TEST_FRAMEWORK")

if test_framework == "selenium":
    from framework.browser.selenium.SeleniumBrowserManager import SeleniumBrowserManager as BrowserManager
if test_framework == "playwright":
    from framework.browser.playwright.PlaywrightBrowserManager import PlaywrightBrowserManager as BrowserManager
