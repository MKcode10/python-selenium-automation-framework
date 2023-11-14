from selenium.webdriver.common.by import By
from base.base_driver import BasePage
from utilities.locators import HomePageLocators


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_book_name(self):
        return self.get_text(HomePageLocators.book_name)

    def assert_book(self):
        from pages.search_page import SearchPage
        sp = SearchPage(self.driver)
        assert self.get_book_name() == sp.get_book_title()
