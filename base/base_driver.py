class BasePage:
    """
    The Purpose Of BasePage Is To Contain Methods Common To All Page Objects
    """
    def __init__(self, driver):
        self.driver = driver

    def find(self, *locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        self.find(*locator).click()

    def get_text(self, locator):
        return self.find(*locator).text

    def get_title(self):
        return self.driver.title

    def send(self, locator, value):
        self.find(*locator).clear()
        self.find(*locator).send_keys(value)

    def get_current_window(self):
        return self.driver.current_window_handle

    def get_all_windows(self):
        return self.driver.window_handles

    def new_window(self):
        all_windows = self.get_all_windows()
        current_window = self.get_current_window()
        new_w = all_windows.pop()
        self.driver.switch_to.window(new_w)
