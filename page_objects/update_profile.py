import time

from selenium.webdriver.common.by import By

from page_objects.explicit_waits import wait_for_element_to_be_clickable, wait_for_element_to_be_visible
from page_objects.locators import PROFILE_DROPDOWN, PROFILE_BUTTON, PROFILE_EDIT_BUTTON, PHONE_NUMBER_TEXTFIELD, \
    SAVE_PROFILE_BUTTON, INVALID_INPUT_MOBILE_NUMBER, CLEAR_MOBILE_NUMBER, PROFILE_UPDATED_SUCCESSFULLY_MESSAGE


class UpdateProfile:
    def __init__(self, driver):
        self.driver = driver

    def click_profile_dropdown(self,):
        wait_for_element_to_be_clickable(self.driver, PROFILE_DROPDOWN, 10).click()

    def click_on_profile_button(self):
        wait_for_element_to_be_clickable(self.driver, PROFILE_BUTTON, 10).click()

    def click_on_profile_edit_button(self):
        wait_for_element_to_be_clickable(self.driver, PROFILE_EDIT_BUTTON, 10).click()

    def clear_mobile_number_textfield(self):
        wait_for_element_to_be_clickable(self.driver, CLEAR_MOBILE_NUMBER, 10).clear()

    def enter_mobile_number(self, mobile_number):
        wait_for_element_to_be_clickable(self.driver, PHONE_NUMBER_TEXTFIELD, 10).send_keys(mobile_number)

    def save_the_input(self):
        wait_for_element_to_be_clickable(self.driver, SAVE_PROFILE_BUTTON, 10).click()

    def error_message_for_invalid_mobile_number(self):
        invalid_mobile_number = wait_for_element_to_be_visible(self.driver, INVALID_INPUT_MOBILE_NUMBER, 10)
        return invalid_mobile_number.is_displayed()

    def check_profile_updated_message(self):
        profile_updated_successfully_message_displayed = wait_for_element_to_be_visible(self.driver, PROFILE_UPDATED_SUCCESSFULLY_MESSAGE, 10)
        return profile_updated_successfully_message_displayed.is_displayed()

    def get_mobile_number_xpath(self, mobile_number):
        return (By.XPATH, f"//div[contains(text(),'{mobile_number}')]")

    def check_mobile_number_updated_successfully(self, mobile_number):
        check_updated_mobile_number = wait_for_element_to_be_visible(self.driver, self.get_mobile_number_xpath(mobile_number), 10)
        return check_updated_mobile_number.is_displayed()