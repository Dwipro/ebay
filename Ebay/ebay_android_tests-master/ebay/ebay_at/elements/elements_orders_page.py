class OrdersPageElements:
    def __init__(self, driver):
        self.driver = driver

    def orders_button_in_router(self):
        return self.driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.ebay.mobile:id/item_title']")

    def orders_page_title(self):
        return self.driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.ebay.mobile:id/title']")
