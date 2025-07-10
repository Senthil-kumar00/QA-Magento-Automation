from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SignupPage(BasePage):
    FIRST_NAME = (By.ID, "firstname")
    LAST_NAME = (By.ID, "lastname")
    EMAIL = (By.ID, "email_address")
    PASSWORD = (By.ID, "password")
    CONFIRM_PASSWORD = (By.ID, "password-confirmation")
    CREATE_BTN = (By.XPATH, "//button[@title='Create an Account']")

    def signup(self, first, last, email, password):
        self.enter_text(self.FIRST_NAME, first)
        self.enter_text(self.LAST_NAME, last)
        self.enter_text(self.EMAIL, email)
        self.enter_text(self.PASSWORD, password)
        self.enter_text(self.CONFIRM_PASSWORD, password)
        self.click(self.CREATE_BTN)
