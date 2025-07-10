import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.home_page import HomePage


@pytest.fixture
def setup():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://magento.softwaretestingboard.com/customer/account/login")
    driver.maximize_window()
    yield driver
    driver.quit()


def test_logout(setup):
    login = LoginPage(setup)
    login.login("senthil_test0015@gmail.com", "Test@02020")

    home = HomePage(setup)
    home.logout()

    assert "Customer Login" in setup.title
