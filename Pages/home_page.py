from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    SIGN_OUT = (By.LINK_TEXT, "Sign Out")

    def logout(self):
        self.click(self.SIGN_OUT)
