from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "pass")
    SIGN_IN_BTN = (By.ID, "send2")

    def login(self, email, password):
        self.enter_text(self.EMAIL, email)
        self.enter_text(self.PASSWORD, password)
        self.click(self.SIGN_IN_BTN)
