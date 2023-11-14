import pytest
from pages.amazon_home_page import HomePage
import unittest
from ddt import ddt, data, file_data, unpack
from utilities import utils


@pytest.mark.usefixtures("initialize_driver")
@ddt
class TestAmazon(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.home_page = HomePage(self.driver)

    # @file_data("../testdata/testdata.json")
    @data(*utils.get_data_from_excel("../testdata/testdata.xlsx"),)
    @unpack
    def test_amazon_pages(self, book_name):
        product_search = self.home_page.search_book(book_name)
        product_select = product_search.click_book()
        product_cart = product_select.add_to_cart()
        final_page = product_cart.go_to_cart()
        print(final_page.get_book_name())
