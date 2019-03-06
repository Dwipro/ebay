	from selenium.common.exceptions import NoSuchElementException


	class BrowsePageElements:
		def __init__(self, driver):
			self.driver = driver

		def browse_page_title(self):
			return self.driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.ebay.mobile:id/search_box']")

		def search_input(self):
			return self.driver.find_element_by_id("com.ebay.mobile:id/search_box")

		def product_id_string(self, id_path):
			return self.driver.find_element_by_xpath(id_path)

		def product_name_string(self, name_path):
			return self.driver.find_element_by_xpath(name_path)

		def reset_search_button(self):
			return self.driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.ebay.mobile:id/search_box']")

		def star_button_disabled(self):
			for n in range(3):
				try:
					return self.driver.find_element_by_id("star-" + str(n) + "-removed")

				except NoSuchElementException:
					continue

			raise Exception("There aren't any disabled star-buttons")

		def star_button_enabled(self):
			return self.driver.find_element_by_id("star-1-added")

		def firs_element_to_scroll(self):
			return self.driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.ebay.mobile:id/item_title']")

		def second_element_to_scroll(self):
			return self.driver.find_element_by_xpath("//android.widget.TextView[@text='com.ebay.mobile:id/item_title']")
# cart button
		def cart_button(self):
			return self.driver.find_element_by_xpath("//android.widget.ImageView[@resource-id='com.ebay.mobile:id/action_view_icon']")
# click on button Add to basket 
		def add_to_cart_button(self, product_number):
			return self.driver.find_element_by_xpath('(//android.widget.ImageView[@resource-id='com.ebay.mobile:id/action_view_icon'])[' + str(product_number) + ']')
