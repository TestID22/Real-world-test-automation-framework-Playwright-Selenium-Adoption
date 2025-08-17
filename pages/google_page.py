from framework.elements.selenium.SeleniumBasePageElement import SeleniumBasePageElement as Element
from framework.page.BasePage import BasePage
from framework.page.playwrightpage.PlayWrightBasePage import PlayWrightBasePage
from framework.page.selenium.SeleniumBasePage import SeleniumBasePage


class GooglePageElements:
    google_search_input = Element()


class GooglePage(BasePage):

    @staticmethod
    def open_new_window(url):
        pass


# class GooglePageClicks(Element):
#
#     def search_button_click(self):
#         pass