import pytest
from selenium import webdriver
from pages.signup_page import SignupPage

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("https://magento.softwaretestingboard.com/customer/account/create/")
    yield driver
    driver.quit()

def test_signup(setup):
    page = SignupPage(setup)
    page.signup("Senthil", "Kumar", "senthil_test0001@gmail.com", "Test@01010")
    assert "My Account" in setup.title
