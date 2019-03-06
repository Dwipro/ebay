import unittest

import HtmlTestRunner

from ebay_at.test_cases.acc_page_search_acc import SearchAccount
from ebay_at.test_cases.add_prod_to_wish_list import AddToWishListTesting

from ebay_at.test_cases.browse_page_search_prod import SearchProduct
from ebay_at.test_cases.login import AppLogin

# get all tests

login_test = unittest.TestLoader().loadTestsFromTestCase(AppLogin)
search_product_test = unittest.TestLoader().loadTestsFromTestCase(SearchProduct)
add_prod_to_wish_list_test = unittest.TestLoader().loadTestsFromTestCase(AddToWishListTesting)
search_accounts_test = unittest.TestLoader().loadTestsFromTestCase(SearchAccount)


suite = unittest.TestSuite((login_test, search_product_test, add_prod_to_wish_list_test, search_accounts_test,))
unittest.TextTestRunner(verbosity=2).run(suite)

# open the report file
outfile = open('/Users/user/PycharmProjects/ebay/reports/ebay/reports/e_reports/SeleniumPythonTestsSummary.html', 'w')

# configure HTMLTestRunner options
runner = HtmlTestRunner.HTMLTestRunner(output='ebay_reports')

# run the suite using HTMLTestRunner
runner.run(suite)
