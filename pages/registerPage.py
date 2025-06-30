from selenium.webdriver.common.by import By

from pages.mainPage import MainPage
from utils.urls import REGISTER_URL
from utils.attributes import URL_ATTR_NAME
from utils.attributes import RegisterPageAttributes as rpAttr
from utils.messages import ErrorMessages as Err


REGISTER_FORM = (By.CSS_SELECTOR, 'form[action="/register"]')
REGISTER_MALE_GENDER_RADIO_BTN = (By.CSS_SELECTOR, '#gender-male')
REGISTER_FEMALE_GENDER_RADIO_BTN = (By.CSS_SELECTOR, '#gender-female')
REGISTER_FIRSTNAME_FIELD = (By.CSS_SELECTOR, '#FirstName')
REGISTER_LASTNAME_FIELD = (By.CSS_SELECTOR, '#LastName')
REGISTER_EMAIL_FIELD = (By.CSS_SELECTOR, '#Email')
REGISTER_PASSWORD_FIELD = (By.CSS_SELECTOR, '#Password')
REGISTER_CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, '#ConfirmPassword')
REGISTER_SUBMIT_BTN = (By.CSS_SELECTOR, '#register-button')
REGISTER_CONTINUE_BTN = (By.CSS_SELECTOR, 'input.register-continue-button')


class RegisterPage(MainPage):
    def should_be_register_page(self):
        self.should_be_register_url()
        self.should_be_register_form()

    def should_be_register_url(self):
        actual_url = self.browser.current_url
        assert REGISTER_URL == actual_url, Err.ELEMENTS_DO_NOT_MATCH_ERR_MSG.format(
            actual=actual_url, expected=REGISTER_URL,
            el_name=URL_ATTR_NAME
        )

    def should_be_register_form(self):
        assert self.is_element_present(*REGISTER_FORM), (
            Err.ELEMENT_IS_MISSING_ERR_MSG.format(element=rpAttr.REGISTER_FORM_ATTR_NAME))

    def register_new_user(self, new_user):
        firstname_field = self.browser.find_element(*REGISTER_FIRSTNAME_FIELD)
        lastname_field = self.browser.find_element(*REGISTER_LASTNAME_FIELD)
        email_field = self.browser.find_element(*REGISTER_EMAIL_FIELD)
        password_field = self.browser.find_element(*REGISTER_PASSWORD_FIELD)
        confirm_password_field = self.browser.find_element(*REGISTER_CONFIRM_PASSWORD_FIELD)
        register_submit_btn = self.browser.find_element(*REGISTER_SUBMIT_BTN)

        firstname_field.send_keys(new_user.firstname)
        lastname_field.send_keys(new_user.lastname)
        email_field.send_keys(new_user.email)
        password_field.send_keys(new_user.password)
        confirm_password_field.send_keys(new_user.password)

        register_submit_btn.click()

    def user_should_be_registered(self):
        self.should_be_register_continue_btn()
        self.should_be_header_user_account_link()
        self.should_be_header_logout_link()

    def should_be_register_continue_btn(self):
        assert self.is_element_present(*REGISTER_CONTINUE_BTN), (
            Err.ELEMENT_IS_MISSING_ERR_MSG.format(element=rpAttr.REGISTER_CONTINUE_BTN_ATTR_NAME))
