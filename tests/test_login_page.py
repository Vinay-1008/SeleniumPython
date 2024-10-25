import pytest

from page_objects.login_page import LoginPage


@pytest.mark.parametrize("username, password", [("vinayreddy100800@gmail.com", ""), ("mHTf756#$", 654324),
                                                ("    ", "     "), (756865, "vvyt564$#%@")])
def test_login_unsuccessful(driver, username, password):
    login_page = LoginPage(driver)
    login_page.open_page("https://www.hackerrank.com/dashboard")
    login_page.initial_login_button()
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()

    if username is "" or password is "":
        login_diabled1 = login_page.login_disabled()
        assert login_diabled1
    else:
        login_error_message1 = login_page.login_error()
        assert login_error_message1

def test_login_successful(driver):
    login_page = LoginPage(driver)
    login_page.open_page("https://www.hackerrank.com/dashboard")
    login_page.initial_login_button()
    login_page.enter_username("vinayreddy100800@gmail.com")
    login_page.enter_password("Vinay@1008")
    login_page.click_login()