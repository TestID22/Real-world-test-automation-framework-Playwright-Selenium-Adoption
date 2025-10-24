from framework.browser.base_browser_factory import BaseBrowserFactory
from playwright.sync_api import BrowserContext, Page, Browser, sync_playwright


class PlaywrightBrowserInstance:
    browser_context: BrowserContext
    page: Page
    browser: Browser

    def __init__(self, browser_context: BrowserContext, page: Page, browser: Browser):
        self.browser_context = browser_context
        self.page = page
        self.browser = browser

class PlaywrightBrowserFactory(BaseBrowserFactory):
    PlaywrightBrowserInstance: PlaywrightBrowserInstance

    @classmethod
    def get_browser_driver(cls, headless=False, **kwargs):
        playwright = sync_playwright().start()

        browser = cls.__get_chrome_driver(playwright=playwright, headless=headless, **kwargs)
        browser_context = browser.new_context(no_viewport=False)
        page = browser.new_page()
        return PlaywrightBrowserInstance(browser=browser, page=page, browser_context=browser_context)

    @classmethod
    def __get_chrome_driver(cls, playwright, headless=False, **kwargs):
        chrome_browser = playwright.chromium.launch(headless=headless,  args=["--start-maximized"], **kwargs) 
        return chrome_browser

    @classmethod
    def __get_firefox_driver(cls, headless=False, **kwargs):
        playwright = sync_playwright().start()
