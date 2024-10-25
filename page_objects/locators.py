from selenium.webdriver.common.by import By

LOGIN_BUTTON = (By.CSS_SELECTOR, ".hrds-btn.login-btn")
USERNAME_TEXTFIELD1 = (By.CSS_SELECTOR, "input[name='username']")
PASSWORD_TEXTFIELD1 = (By.CSS_SELECTOR, "input[name='password']")
LOGIN_SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type ='submit']")
LOGIN_ERROR_MESSAGE = (By.XPATH, "//h3[text()='Invalid login or password. Please try again.']")
LOGIN_BUTTON_DISABLED = (By.XPATH, "//button[@disabled]")
CLOSE_LOGIN_FORM_BUTTON = (By.XPATH, "//button[@aria-label='Close']")

PROFILE_DROPDOWN = (By.CSS_SELECTOR, ".ui-icon-chevron-down.down-icon")
PROFILE_BUTTON = (By.CSS_SELECTOR, ".profile-nav-item-link.profile-progress")
PROFILE_EDIT_BUTTON = (By.CSS_SELECTOR, "span.hr-flex.hr-justify-center.hr-align-center.profile-edit-button")
CLEAR_MOBILE_NUMBER = (By.CSS_SELECTOR, "input[name='phoneNumber']")
PHONE_NUMBER_TEXTFIELD = (By.CSS_SELECTOR, "#phoneNumber")
SAVE_PROFILE_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
INVALID_INPUT_MOBILE_NUMBER = (By.CSS_SELECTOR, "div[role='alert']>svg")
PROFILE_UPDATED_SUCCESSFULLY_MESSAGE = (By.CSS_SELECTOR, "#toast-portal-container>div>div:first-of-type>div>div>ol>li>div")