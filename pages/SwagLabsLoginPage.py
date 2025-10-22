from configuration.dynamic_imports import BasePage
from configuration.dynamic_imports import DynamicPageElement
from pages.PageCategory import PageCategory


class SwagLabsPageElements:

    username_input = DynamicPageElement(locator="//input[@id='user-name']", element_name="username_input")
    password_input = DynamicPageElement(locator="//input[@id='password']", element_name="password_input")

    #Buttons
    login_button = DynamicPageElement(locator="//input[@id='login-button']", element_name="login_button")


class SwagLabsLoginPage(BasePage):

    def __init__(self):
        super().__init__(*self.elements.username_input.as_tuple())

    @property
    def elements(self):
        return SwagLabsPageElements

    @property
    def click(self):
        return SwagLabsLoginPageClicks(self)

    @property
    def set(self):
        return SwagLabsSets(self)

    def login(self, user_name, password):
        self.elements.username_input.send_keys(user_name)
        self.elements.password_input.send_keys(password)


class SwagLabsLoginPageClicks(PageCategory):

    def click_login_button(self):
        self.page.elements.login_button.click()


class SwagLabsSets(PageCategory):

    def set_user_name(self, user_name):
        self.page.elements.username_input.send_keys(user_name)