class AccountsPageElements:
    def __init__(self, driver):
        self.driver = driver

####--- left corner = button 

    def accounts_page_in_router(self):
        return self.driver.find_element_by_xpath("android.widget.ImageButton[@resource-id='com.ebay.mobile:id/home']")

#ebay logo in home page as title
    def accounts_page_title(self):
        return self.driver.find_element_by_xpath("android.widget.ImageView[@resource-id='com.ebay.mobile:id/logo']")
#near to title selling in home page 
    def near_you_title(self):
        return self.driver.find_element_by_xpath("android.widget.TextView[@resource-id='com.ebay.mobile:id/home_pill']")


