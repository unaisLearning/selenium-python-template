from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):

    #Locators
    USER_NAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_SECTION = (By.CSS_SELECTOR, "h3[data-test='error']")

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username, password):
        self.enter_text(self.USER_NAME_FIELD, username)
        self.enter_text(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)

        from pages.inventory_page import InventoryPage
        return InventoryPage(self.driver)

    def get_error_message(self):
        return self.get_text(self.ERROR_SECTION)

