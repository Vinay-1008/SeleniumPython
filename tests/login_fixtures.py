import pytest

from page_objects.login_page import LoginPage


@pytest.fixture(scope="function")
def login_page_after_successful(driver):
    login_page = LoginPage(driver)
    login_page.open_page("https://www.hackerrank.com/dashboard")
    login_page.initial_login_button()
    login_page.enter_username("vinayreddy100800@gmail.com")
    login_page.enter_password("Vinay@1008")
    login_page.click_login()
    return driver