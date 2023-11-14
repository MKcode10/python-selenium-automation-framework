from base.base_driver import BasePage
from selenium.webdriver.common.by import By
from pages.product_page import AddProduct
from utilities.locators import HomePageLocators


class SearchPage(BasePage):
    # product = (By.XPATH, "//div[@data-asin='142156906X']//a//span[contains(@class,'a-text-normal')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_book_title(self):
        return self.get_text(HomePageLocators.product)

    def click_book(self):
        self.get_current_window()
        self.click(HomePageLocators.product)
        self.new_window()
        add_product = AddProduct(self.driver)
        return add_product
