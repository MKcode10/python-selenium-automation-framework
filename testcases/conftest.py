from selenium import webdriver
import pytest


@pytest.fixture(scope="class")
def initialize_driver(request, browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "edge":
        driver = webdriver.Edge()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    driver.get("https://www.amazon.in/")
    driver.implicitly_wait(5)
    driver.maximize_window()
    request.cls.driver = driver
    yield print("Close browser")
    driver.close()


def pytest_addoption(parser):
    parser.addoption('--browser')


@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption('--browser')