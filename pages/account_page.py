from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AccountPage(BasePage):
    CHANGE_PASSWORD_LINK = (By.LINK_TEXT, "Change Password")
    CURRENT_PASSWORD = (By.ID, "current-password")
    NEW_PASSWORD = (By.ID, "password")
    CONFIRM_NEW_PASSWORD = (By.ID, "password-confirmation")
    SAVE_BTN = (By.XPATH, "//button[@title='Save']")

    def change_password(self, current_pwd, new_pwd):
        self.click(self.CHANGE_PASSWORD_LINK)
        self.enter_text(self.CURRENT_PASSWORD, current_pwd)
        self.enter_text(self.NEW_PASSWORD, new_pwd)
        self.enter_text(self.CONFIRM_NEW_PASSWORD, new_pwd)
        self.click(self.SAVE_BTN)
