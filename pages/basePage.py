from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from utils.constants import WAIT_TIMEOUT
from utils.attributes import URL_ATTR_NAME
from utils.messages import ErrorMessages as Err


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def go_to_page_via_link(self, locator_type, link_locator):
        link = self.browser.find_element(locator_type, link_locator)
        link.click()

    def move_cursor_to_element(self, locator):
        element = self.wait_until_element_is_visible(self.browser, locator)
        ActionChains(self.browser).move_to_element(element).perform()

    def go_to_page_via_top_menu(self, target_page_locator:tuple, parent_locator:tuple = None):
        if parent_locator:
            self.move_cursor_to_element(parent_locator)

        target_page_link = self.wait_until_element_is_clickable(self.browser, target_page_locator)
        target_page_link.click()

    def is_element_present(self, locator_type, locator):
        result = True

        try:
            self.browser.find_element(locator_type, locator)
        except NoSuchElementException:
            result = False

        return result

    def should_be_correct_url(self, expected_url):
        actual_url = self.browser.current_url
        assert expected_url == actual_url, Err.ELEMENTS_DO_NOT_MATCH_ERR_MSG.format(actual=actual_url, expected=expected_url,
                                                                                    el_name=URL_ATTR_NAME)

    def set_dropdown_value(self, locator_type, locator, value_to_set):
        select = Select(self.browser.find_element(locator_type, locator))
        current_value = select.first_selected_option.text.strip()

        if current_value == value_to_set:
            return

        select.select_by_visible_text(value_to_set)

    @classmethod
    def wait_until_element_is_visible(cls, browser, locator, timeout=WAIT_TIMEOUT):
        element = WebDriverWait(browser, timeout).until(ec.visibility_of_element_located(locator))
        return element

    @classmethod
    def wait_until_element_is_clickable(cls, browser, locator, timeout=WAIT_TIMEOUT):
        element = WebDriverWait(browser, timeout).until(ec.element_to_be_clickable(locator))
        return element

    @classmethod
    def wait_for_element_to_be_present(cls, browser, locator, timeout=WAIT_TIMEOUT):
        try:
            WebDriverWait(browser, timeout).until(ec.presence_of_element_located(locator))
        except TimeoutException:
            return False
        return True

