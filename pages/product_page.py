from selenium.webdriver.common.by import By
from base.base_driver import BasePage
from pages.product_page2 import GoCart
from utilities.locators import HomePageLocators


class AddProduct(BasePage):
    # cart_button = (By.XPATH, "//input[@id='add-to-cart-button']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def add_to_cart(self):
        self.click(HomePageLocators.cart_button)
        gocart = GoCart(self.driver)
        return gocart
