import os
import dotenv

dotenv.load_dotenv()

test_framework = os.getenv("TEST_FRAMEWORK").lower()

if test_framework == "selenium":

    from framework.browser.selenium.selenium_browser_manager import SeleniumBrowserManager as BrowserManager
    from framework.page.selenium.selenium_base_page import SeleniumBasePage as BasePage
    from framework.elements.selenium.selenium_base_page_element import SeleniumBasePageElement as DynamicPageElement

elif test_framework == "playwright":
    from framework.browser.playwright.playwright_browser_manager import PlaywrightBrowserManager as BrowserManager
    from framework.page.playwrightpage.play_wright_base_page import PlayWrightBasePage as Page

else:
    raise ValueError(f"Unknown TEST_FRAMEWORK: {test_framework}")
