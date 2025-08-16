from framework.elements.BasePageElement import BasePageElement
from framework.browser.selenium.SeleniumBrowserManager import SeleniumBrowserManager

class SeleniumBasePageElement(BasePageElement):

    @property
    def driver(self):
        return SeleniumBrowserManager().get_driver()
