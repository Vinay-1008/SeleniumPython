import time

import pytest

from page_objects.update_profile import UpdateProfile
from tests.login_fixtures import login_page_after_successful

@pytest.mark.parametrize("mobile_number" , [(""), (79978200651), (8019731787), (7997820065)])
def test_profile_updation(login_page_after_successful, mobile_number):
    driver = login_page_after_successful
    profile_update = UpdateProfile(driver)
    profile_update.click_profile_dropdown()
    profile_update.click_on_profile_button()
    profile_update.click_on_profile_edit_button()
    profile_update.clear_mobile_number_textfield()
    profile_update.enter_mobile_number(mobile_number)
    profile_update.save_the_input()
    profile_update.check_profile_updated_message()
    if mobile_number is not "":
        profile_update.check_mobile_number_updated_successfully(mobile_number)


@pytest.mark.parametrize("mobile_number", [("hgiujnh"), ("&^8897$#"), ("njhi76567"), ("    "), ("^% 65 jbh")])
def test_profile_updation_with_invalid_inputs(login_page_after_successful, mobile_number):
    driver = login_page_after_successful
    profile_update = UpdateProfile(driver)
    profile_update.click_profile_dropdown()
    profile_update.click_on_profile_button()
    profile_update.click_on_profile_edit_button()
    profile_update.clear_mobile_number_textfield()
    profile_update.enter_mobile_number(mobile_number)
    profile_update.save_the_input()
    assert profile_update.error_message_for_invalid_mobile_number()