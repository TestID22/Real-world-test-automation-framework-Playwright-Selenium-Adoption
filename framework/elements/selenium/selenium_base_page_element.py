from framework.elements.base_page_element import BasePageElement
from framework.browser.selenium.selenium_browser_manager import SeleniumBrowserManager

class SeleniumBasePageElement(BasePageElement):

    @property
    def driver(self):
        return SeleniumBrowserManager().get_driver()
