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
    page.signup("Senthil", "Kumar", "senthil_test0015@gmail.com", "Test@02020")
    assert "My Account" in setup.title
