from selenium.webdriver.common.by import By
from base.base_driver import BasePage
from pages.cart_page import CartPage
from utilities.locators import HomePageLocators


class GoCart(BasePage):
    # go_cart = (By.XPATH, "//span[@id='sw-gtc']//a[normalize-space()='Go to Cart']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def go_to_cart(self):
        self.click(HomePageLocators.go_cart)
        cart_new_page = CartPage(self.driver)
        return cart_new_page
