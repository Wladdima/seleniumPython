from selenium.webdriver.common.by import By

from pages.basePage import BasePage
from utils.attributes import MainPageAttributes as mpAttr
from utils.messages import ErrorMessages as Err


REGISTER_LINK = (By.CSS_SELECTOR, '.ico-register')
LOGIN_LINK = (By.CSS_SELECTOR, '.ico-login')
HEADER_USER_ACCOUNT_LINK = (By.CSS_SELECTOR, 'div.header-links a.account')
HEADER_LOGOUT_LINK = (By.CSS_SELECTOR, 'div.header-links a.ico-logout')
ELECTRONICS_TOP_MENU_LINK = (By.CSS_SELECTOR, 'ul.top-menu li a[href="/electronics"]')
CELLPHONE_PRODUCT_LIST_TOP_MENU_LINK = (By.CSS_SELECTOR, 'ul.top-menu li a[href="/cell-phones"]')
SHOPPING_CART_ICON = (By.CSS_SELECTOR, '#topcartlink .ico-cart')
SHOPPING_CART_ICON_QUANTITY = (By.CSS_SELECTOR, '.ico-cart .cart-qty')
FLYOUT_CART = (By.CSS_SELECTOR, '#flyout-cart .mini-shopping-cart')
FLYOUT_CART_QUANTITY_MESSAGE = (By.CSS_SELECTOR, '.count')
FLYOUT_CART_PRODUCT_PRICE = (By.CSS_SELECTOR, '.item.first .price span')
FLYOUT_CART_TOTAL_PRICE = (By.CSS_SELECTOR, '.totals strong')
FLYOUT_CART_PRODUCT_TITLE = (By.CSS_SELECTOR, '.item.first .name a')
FLYOUT_CART_PRODUCT_ATTRS = (By.CSS_SELECTOR, '.item.first .attributes')


class MainPage(BasePage):
    def should_be_register_link(self):
        assert self.is_element_present(*REGISTER_LINK), (
            Err.ELEMENT_IS_MISSING_ERR_MSG.format(element=mpAttr.REGISTER_LINK_ATTR_NAME))

    def should_be_login_link(self):
        assert self.is_element_present(*LOGIN_LINK), (
            Err.ELEMENT_IS_MISSING_ERR_MSG.format(element=mpAttr.LOGIN_LINK_ATTR_NAME))

    def should_be_header_user_account_link(self):
        assert self.is_element_present(*HEADER_USER_ACCOUNT_LINK), (
            Err.ELEMENT_IS_MISSING_ERR_MSG.format(element=mpAttr.HEADER_USER_ACC_LINK_ATTR_NAME))

    def should_be_header_logout_link(self):
        assert self.is_element_present(*HEADER_LOGOUT_LINK), (
            Err.ELEMENT_IS_MISSING_ERR_MSG.format(element=mpAttr.HEADER_LOGOUT_LINK_ATTR_NAME))

    def should_be_correct_product_list_link(self, product_list_link, product_title):
        assert self.is_element_present(*product_list_link), (
            Err.ELEMENT_IS_MISSING_ERR_MSG.format(element=f'{mpAttr.PRODUCT_LIST_LINK_ATTR_NAME} for {product_title}'))

    def go_to_register_page(self):
        self.go_to_page_via_link(*REGISTER_LINK)

    def go_to_login_page(self):
        self.go_to_page_via_link(*LOGIN_LINK)

    def go_to_cellphone_product_list_page(self):
        self.go_to_page_via_top_menu(parent_locator=ELECTRONICS_TOP_MENU_LINK,
                                     target_page_locator=CELLPHONE_PRODUCT_LIST_TOP_MENU_LINK)
