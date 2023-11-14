from base.base_driver import BasePage
from selenium.webdriver.common.by import By
from pages.search_page import SearchPage
from utilities.locators import HomePageLocators


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def send_search_value(self, book):
        self.send(HomePageLocators.search_box, book)

    def click_search(self):
        self.click(HomePageLocators.search_button)

    def search_book(self, book):
        self.send_search_value(book)
        self.click_search()
        next_page = SearchPage(self.driver)
        return next_page
