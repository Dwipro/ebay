import unittest

from appium import webdriver


class SetUpClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        caps = {}
        caps["platformName"] = "Android"
        caps["platformVersion"] = "7.0"
        caps["deviceName"] = "Mi Note 4"
        caps["appPackage"] = "com.schneiderelectric.eCommissionSmartXIPController.Internal"
        caps["appActivity"] = "md5e3e0ca5a61fc8aa16e6e0a6d7e9daa42.SplashScreen"

        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
