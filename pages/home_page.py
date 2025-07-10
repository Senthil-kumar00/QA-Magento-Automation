from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class HomePage(BasePage):
    CUSTOMER_MENU = (By.CSS_SELECTOR, ".customer-welcome")
    SIGN_OUT = (By.LINK_TEXT, "Sign Out")

    def logout(self):
        wait = WebDriverWait(self.driver, 10)

        # Hover over the "Welcome, User" dropdown menu
        customer_menu = wait.until(EC.visibility_of_element_located(self.CUSTOMER_MENU))
        ActionChains(self.driver).move_to_element(customer_menu).perform()

        # Wait and click the "Sign Out" link
        sign_out_link = wait.until(EC.element_to_be_clickable(self.SIGN_OUT))
        sign_out_link.click()

        # Optional: wait for redirection to login page
        wait.until(EC.title_contains("Customer Login"))
