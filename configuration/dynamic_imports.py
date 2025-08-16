import os
import dotenv

dotenv.load_dotenv()

test_framework = os.getenv("TEST_FRAMEWORK")

if test_framework == "selenium":
    from framework.browser.selenium.SeleniumBrowserManager import SeleniumBrowserManager as BrowserManager
    from framework.page.selenium.SeleniumBasePage import SeleniumBasePage as Page

elif test_framework == "playwright":
    from framework.browser.playwright.PlaywrightBrowserManager import PlaywrightBrowserManager as BrowserManager
    from framework.page.playwrightpage.PlayWrightBasePage import PlayWrightBasePage as Page

else:
    raise ValueError(f"Unknown TEST_FRAMEWORK: {test_framework}")
