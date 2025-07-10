import pytest
from selenium import webdriver
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
    login.login("senthil_test0001@gmail.com", "Test@01010")
    account = AccountPage(setup)
    account.change_password("Test@01010", "Test@10101")
    assert "You saved the account information." in setup.page_source
