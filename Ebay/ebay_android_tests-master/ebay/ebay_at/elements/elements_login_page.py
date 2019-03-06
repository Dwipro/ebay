from selenium import webdriver
class LoginPageElements:

    def __init__(self, driver):
        self.driver = driver

    def email_field(self):
        return self.driver.find_element_by_id("com.ebay.mobile:id/edit_text_username")

    def password_field(self):
        return self.driver.find_element_by_id("com.ebay.mobile:id/view_ebay_password")

    def login_button(self):
        return self.driver.find_element_by_id("com.ebay.mobile:id/button_sign_in")



