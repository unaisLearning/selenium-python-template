from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class CartPage(BasePage):

    #locators
    PAGE_TITLE = (By.CLASS_NAME, "title")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")
    CART_ITEM = (By.CSS_SELECTOR, "div.inventory_item_name")
    REMOVE_BUTTON = (By.CSS_SELECTOR, "button[id^='remove-']")

    def get_page_title(self):
        return self.get_text(self.PAGE_TITLE)

    def get_added_item_name(self):
        return self.get_text(self.CART_ITEM)

    def remove_from_cart(self):
        self.click(self.REMOVE_BUTTON)

    def continue_shopping(self):
        self.click(self.CONTINUE_SHOPPING_BUTTON)
        from pages.inventory_page import InventoryPage
        return InventoryPage(self.driver)

    def is_cart_empty(self):
        try:
            self.find_element(self.CART_ITEM)
            return False
        except Exception:
            return True
