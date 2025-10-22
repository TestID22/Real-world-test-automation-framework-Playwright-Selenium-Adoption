from configuration.dynamic_imports import BasePage
from configuration.dynamic_imports import DynamicPageElement
from pages.PageCategory import PageCategory



class SwagLabsProductsPageElements:

    inventory_title = DynamicPageElement(locator="//span[contains(@class, 'title')]", element_name="inventory_title")


class SwagLabsProductsPage:

    def __init__(self):
        pass

    @property
    def elements(self):
        return SwagLabsProductsPageElements


