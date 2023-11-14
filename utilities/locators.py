from selenium.webdriver.common.by import By


class HomePageLocators:
    search_box = (By.CSS_SELECTOR, "#twotabsearchtextbox")
    search_button = (By.ID, "nav-search-submit-button")
    # product = (By.XPATH, "//div[@data-asin='142156906X']//a//span[contains(@class,'a-text-normal')]")
    product = (By.XPATH, "//div[contains(@class,'s-image-fixed-height')]//img[@data-image-index=1]")
    cart_button = (By.XPATH, "//input[@id='add-to-cart-button']")
    go_cart = (By.XPATH, "//span[@id='sw-gtc']//a[normalize-space()='Go to Cart']")
    book_name = (By.XPATH, "//li//span[@class='a-truncate-cut']")


