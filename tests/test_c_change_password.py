import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.account_page import AccountPage


@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("https://magento.softwaretestingboard.com/customer/account/login")
    yield driver
    driver.quit()


def test_change_password(setup):
    login = LoginPage(setup)
    login.login("senthil_test2@gmail.com", "Test@02020")

    account = AccountPage(setup)
    account.change_password("Test@02020", "Test@20202", "Test@20202")

    # Wait for the success message after password change
    WebDriverWait(setup, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".message-success"))
    )

    # Extract and assert the success message
    success_msg = setup.find_element(By.CSS_SELECTOR, ".message-success").text
    assert "You saved the account information." in success_msg
