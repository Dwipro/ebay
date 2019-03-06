import unittest

from ebay_at.actions.actions_browse_page import *
from ebay_at.actions.setup_class import SetUpClass


class SearchProduct(SetUpClass):
    def test_search_product_by_id(self):
        LoginPage(self.driver).login_full_case()
        BrowsePage(self.driver).search_product_by_id("TV 65")


class ResetSearchProduct(SetUpClass):
    def test_reset_search(self):
        SearchProduct.test_search_product_by_id(self)
        BrowsePage(self.driver).clear_search_input()


if __name__ == '__main__':
    unittest.main()
