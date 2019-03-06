import unittest

from appium import webdriver


class SetUpClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        caps = {}
        caps["platformName"] = "android"
        caps["platformVersion"] = "7.0"
        caps["deviceName"] = "Mi note 4"
        caps["UDID"]="34e7c9ec0104"
		caps["appPackage"]="com.ebay.mobile"
		caps["appActivity"]="com.ebay.mobile.activities.MainActivity"

        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
