from selenium.webdriver.common.by import By

from pages.mainPage import MainPage
from utils.urls import LOGIN_URL
from utils.attributes import URL_ATTR_NAME
from utils.attributes import LoginPageAttributes as lpAttr
from utils.messages import ErrorMessages as Err


LOGIN_FORM = (By.CSS_SELECTOR, 'form[action="/login"]')
LOGIN_EMAIL_FIELD = (By.CSS_SELECTOR, '#Email')
LOGIN_PASSWORD_FIELD = (By.CSS_SELECTOR, '#Password')
LOGIN_SUBMIT_BTN = (By.CSS_SELECTOR, '.login-button')


class LoginPage(MainPage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()

    def should_be_login_url(self):
        actual_url = self.browser.current_url
        assert LOGIN_URL == actual_url, Err.ELEMENTS_DO_NOT_MATCH_ERR_MSG.format(actual=actual_url, expected=LOGIN_URL,
                                                                                 el_name=URL_ATTR_NAME)

    def should_be_login_form(self):
        assert self.is_element_present(*LOGIN_FORM), (
            Err.ELEMENT_IS_MISSING_ERR_MSG.format(element=lpAttr.LOGIN_FORM_ATTR_NAME))

    def log_in_user(self, user):
        email_field = self.browser.find_element(*LOGIN_EMAIL_FIELD)
        password_field = self.browser.find_element(*LOGIN_PASSWORD_FIELD)
        login_submit_btn = self.browser.find_element(*LOGIN_SUBMIT_BTN)

        email_field.send_keys(user.email)
        password_field.send_keys(user.password)
        login_submit_btn.click()

    def user_should_be_logged_in(self):
        self.should_be_header_user_account_link()
        self.should_be_header_logout_link()
