import os
import dotenv

dotenv.load_dotenv()

test_framework = os.getenv("TEST_FRAMEWORK")

if test_framework == "selenium":

    from framework.browser.selenium.SeleniumBrowserManager import SeleniumBrowserManager as BrowserManager
    from framework.page.selenium.SeleniumBasePage import SeleniumBasePage as Page
    from framework.elements.selenium.SeleniumBasePageElement import SeleniumBasePageElement as DynamicPageElement

elif test_framework == "playwright":
    from framework.browser.playwright.playwright_browser_manager import PlaywrightBrowserManager as BrowserManager
    from framework.page.playwrightpage.play_wright_base_page import PlayWrightBasePage as Page

else:
    raise ValueError(f"Unknown TEST_FRAMEWORK: {test_framework}")
