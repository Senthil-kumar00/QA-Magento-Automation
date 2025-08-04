from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from pages.base_page import BasePage


class HomePage(BasePage):
    ARROW_BTN = (By.CSS_SELECTOR, "button.action.switch")
    SIGN_OUT = (By.LINK_TEXT, "Sign Out")

    def logout(self):
        # Move to the dropdown and click the arrow
        arrow_element = self.wait.until(EC.element_to_be_clickable(self.ARROW_BTN))
        ActionChains(self.driver).move_to_element(arrow_element).click().perform()

        # Optional: Wait a short time for the dropdown animation
        sleep(2)

        # Now click the 'Sign Out' link
        signout_link = self.wait.until(EC.element_to_be_clickable(self.SIGN_OUT))
        signout_link.click()

