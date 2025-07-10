import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.home_page import HomePage

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("https://magento.softwaretestingboard.com/customer/account/login")
    yield driver
    driver.quit()

def test_logout(setup):
    login = LoginPage(setup)
    login.login("senthil_test0001@gmail.com", "Test@01010")
    home = HomePage(setup)
    home.logout()
    assert "Customer Login" in setup.title
