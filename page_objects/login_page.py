from page_objects.explicit_waits import wait_for_element_to_be_clickable, wait_for_element_to_be_visible
from page_objects.locators import LOGIN_BUTTON, USERNAME_TEXTFIELD1, PASSWORD_TEXTFIELD1, LOGIN_SUBMIT_BUTTON, \
    LOGIN_BUTTON_DISABLED, LOGIN_ERROR_MESSAGE, CLOSE_LOGIN_FORM_BUTTON


from tests.conftest import driver


class LoginPage:
    def  __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)
        # "https://www.hackerrank.com/dashboard"

    def initial_login_button(self):
        login_button1 = wait_for_element_to_be_clickable(self.driver, LOGIN_BUTTON, 10)
        login_button1.click()
        # self.driver.find_element(*LOGIN_BUTTON).click()

    def enter_username(self, username):
        enter_username_after_visible = wait_for_element_to_be_clickable(self.driver, USERNAME_TEXTFIELD1, 10)
        return enter_username_after_visible.send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*PASSWORD_TEXTFIELD1).send_keys(password)

    def click_login(self):
        self.driver.find_element(*LOGIN_SUBMIT_BUTTON).click()

    def login_disabled(self):
        return self.driver.find_element(*LOGIN_BUTTON_DISABLED).is_displayed()

    def login_error(self):
        login_error1 = wait_for_element_to_be_visible(self.driver, LOGIN_ERROR_MESSAGE, 10)
        return login_error1.is_displayed()

    def click_close_login_form_button_if_available(self):
        if self.driver.find_element(*CLOSE_LOGIN_FORM_BUTTON).is_displayed():
            return self.driver.find_element(*CLOSE_LOGIN_FORM_BUTTON).click()

