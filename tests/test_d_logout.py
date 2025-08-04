import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
    login.login("senthil_test2@gmail.com", "Test@20202")

    home = HomePage(setup)
    home.logout()

    WebDriverWait(setup, 10).until(EC.title_contains("Home Page"))

    assert "Home Page" in setup.title

