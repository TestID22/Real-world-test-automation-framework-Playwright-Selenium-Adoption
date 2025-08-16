from framework.elements.selenium.SeleniumBasePageElement import SeleniumBasePageElement as Element
from framework.page.BasePage import BasePage
from framework.page.selenium.SeleniumBasePage import SeleniumBasePage


class GooglePageElements:
    google_search_input = Element()


class GooglePage(SeleniumBasePage):

    @property
    def click(self):
        pass


# class GooglePageClicks(Element):
#
#     def search_button_click(self):
#         pass