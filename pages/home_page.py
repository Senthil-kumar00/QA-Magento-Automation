from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    ARROW_BTN = (By.CLASS_NAME, "action switch")
    SIGN_OUT = (By.CLASS_NAME, "authorization-link")

    def logout(self):
        self.click(self.ARROW_BTN)
        self.click(self.SIGN_OUT)

