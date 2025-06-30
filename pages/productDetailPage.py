from decimal import Decimal

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pages.basePage import BasePage
from pages.mainPage import (SHOPPING_CART_ICON_QUANTITY,
                            SHOPPING_CART_ICON,
                            FLYOUT_CART,
                            FLYOUT_CART_QUANTITY_MESSAGE,
                            FLYOUT_CART_PRODUCT_PRICE,
                            FLYOUT_CART_TOTAL_PRICE,
                            FLYOUT_CART_PRODUCT_TITLE,
                            FLYOUT_CART_PRODUCT_ATTRS)
from utils.attributes import PAGE_TITLE_ATTR_NAME
from utils.attributes import MainPageAttributes as mpAttr
from utils.attributes import ProductDetailPageAttributes as dpAttr
from utils.messages import ErrorMessages as Err
from utils.messages import ProductDetailPage as pdMsg
from utils.messages import MainPage as mpMsg
from utils.regex import PRODUCT_COLOR_REGEX


PRODUCT_NAME_LOCATOR = (By.CSS_SELECTOR, 'div.product-name h1')
PRODUCT_ID_LOCATOR = (By.CSS_SELECTOR, '#product-details-form [data-productid]')
DYNAMIC_PRODUCT_QUANTITY_INPUT_FIELD = (By.CSS_SELECTOR, 'input#addtocart_{prod_id}_EnteredQuantity')
DYNAMIC_PRODUCT_COLOR_DROPDOWN = (By.CSS_SELECTOR, 'select#product_attribute_{prod_id}_1_38')
DYNAMIC_PRODUCT_MANUFACTURER_DROPDOWN = (By.CSS_SELECTOR, 'select#product_attribute_{prod_id}_2_37')
ADD_TO_CART_BTN = (By.CSS_SELECTOR, '.add-to-cart-button')
PRODUCT_ADDED_TO_CART_SUCCESS_MSG = (By.CSS_SELECTOR, '.bar-notification.success p')


class ProductDetailPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)
        self.flyout_cart = None

    def should_be_correct_product_detail_page(self, product):
        self.should_be_correct_url(product.url)
        self.should_be_correct_product_title(product.title)
        self.should_be_correct_product_id(product.id)

    def should_be_correct_product_title(self, expected_product_title):
        actual_product_title = self.browser.find_element(*PRODUCT_NAME_LOCATOR).text
        assert expected_product_title == actual_product_title, Err.ELEMENTS_DO_NOT_MATCH_ERR_MSG.format(
            actual=actual_product_title, expected=expected_product_title, el_name=PAGE_TITLE_ATTR_NAME)

    def should_be_correct_product_id(self, expected_product_id):
        prod_id_attr_name = dpAttr.PRODUCT_ID_ATTR_NAME
        actual_product_id = self.browser.find_element(*PRODUCT_ID_LOCATOR).get_attribute(prod_id_attr_name)
        assert expected_product_id == actual_product_id, Err.ELEMENTS_DO_NOT_MATCH_ERR_MSG.format(
            actual=actual_product_id, expected=expected_product_id, el_name=prod_id_attr_name)

    def set_product_attributes(self, product):
        for attr, handler in self._DISPATCH.items():
            # Checks if product contains specific attribute and calls corresponding set handler method
            value = getattr(product, attr, None)

            if value is not None:
                handler(self, product)

    def set_product_quantity(self, product):
        locator_type, locator = DYNAMIC_PRODUCT_QUANTITY_INPUT_FIELD
        quantity_input_field = self.browser.find_element(locator_type, locator.format(prod_id=product.id))
        current_value = quantity_input_field.get_attribute('value') or ''

        if current_value == product.quantity:
            return

        quantity_input_field.send_keys(Keys.CONTROL, 'a', Keys.DELETE)
        quantity_input_field.send_keys(product.quantity)

    def set_product_color(self, product):
        locator_type, locator = DYNAMIC_PRODUCT_COLOR_DROPDOWN
        self.set_dropdown_value(locator_type, locator.format(prod_id=product.id), product.color)

    def set_product_manufacturer(self, product):
        locator_type, locator = DYNAMIC_PRODUCT_MANUFACTURER_DROPDOWN
        self.set_dropdown_value(locator_type, locator.format(prod_id=product.id), product.manufacturer)

    def add_product_to_cart(self):
        add_to_cart_btn = self.browser.find_element(*ADD_TO_CART_BTN)
        add_to_cart_btn.click()
        self.wait_until_element_is_visible(self.browser, PRODUCT_ADDED_TO_CART_SUCCESS_MSG)

    def should_be_correctly_added_product_to_cart(self, product):
        self.should_be_correct_success_message()
        self.should_be_cart_link_info_with_correct_product_added(product)

    def should_be_correct_success_message(self):
        add_to_cart_success_msg = self.wait_until_element_is_visible(self.browser, PRODUCT_ADDED_TO_CART_SUCCESS_MSG)
        actual_msg = add_to_cart_success_msg.get_attribute('textContent').strip()
        expected_msg = pdMsg.PRODUCT_ADDED_TO_CART_SUCCESS_MSG
        assert expected_msg == actual_msg, Err.ELEMENTS_DO_NOT_MATCH_ERR_MSG.format(
            actual=actual_msg, expected=expected_msg, el_name=dpAttr.PRODUCT_ADDED_TO_CART_SUCCESS_MSG)

    def should_be_cart_link_info_with_correct_product_added(self, product):
        self.should_be_correct_quantity_cart_icon(product.quantity)
        self.should_be_correct_flyout_cart_info(product)

    def should_be_correct_quantity_cart_icon(self, exp_quantity):
        act_quantity = self.browser.find_element(*SHOPPING_CART_ICON_QUANTITY).text.strip("()")
        assert exp_quantity == act_quantity, Err.ELEMENTS_DO_NOT_MATCH_ERR_MSG.format(
            actual=act_quantity, expected=exp_quantity, el_name=dpAttr.CART_ICON_QUANTITY)

    def should_be_correct_flyout_cart_info(self, product):
        self.move_cursor_to_element(SHOPPING_CART_ICON)
        self.flyout_cart = self.wait_until_element_is_visible(self.browser, FLYOUT_CART)
        self.should_be_correct_flyout_cart_quantity_message(product.quantity)
        self.should_be_correct_flyout_cart_product_price(product.price)
        self.should_be_correct_flyout_cart_total_price(product.price, product.quantity)
        self.should_be_correct_flyout_cart_title(product.title)
        self.should_be_correct_flyout_cart_product_color(product.color)

    def should_be_correct_flyout_cart_quantity_message(self, product_quantity):
        exp_message = mpMsg.DYNAMIC_FLYOUT_CART_PRODUCT_QUANTITY_MESSAGE.format(quantity=product_quantity)
        act_message = self.flyout_cart.find_element(*FLYOUT_CART_QUANTITY_MESSAGE).get_attribute('textContent').strip()
        assert exp_message == act_message, Err.ELEMENTS_DO_NOT_MATCH_ERR_MSG.format(
            actual=act_message, expected=exp_message, el_name=mpAttr.FLYOUT_CART_PRODUCT_QUANTITY_MESSAGE_ATTR_NAME)

    def should_be_correct_flyout_cart_product_price(self, exp_product_price):
        act_price = self.flyout_cart.find_element(*FLYOUT_CART_PRODUCT_PRICE).get_attribute('textContent').strip()
        assert exp_product_price == act_price, Err.ELEMENTS_DO_NOT_MATCH_ERR_MSG.format(
            actual=act_price, expected=exp_product_price, el_name=mpAttr.FLYOUT_CART_PRODUCT_PRICE_ATTR_NAME)

    def should_be_correct_flyout_cart_total_price(self, product_price, product_quantity):
        exp_price = Decimal(product_price) * int(product_quantity)
        exp_price = f'{exp_price:.2f}'
        act_price = self.flyout_cart.find_element(*FLYOUT_CART_TOTAL_PRICE).get_attribute('textContent').strip()
        assert exp_price == act_price, Err.ELEMENTS_DO_NOT_MATCH_ERR_MSG.format(
            actual=act_price, expected=exp_price, el_name=mpAttr.FLYOUT_CART_TOTAL_PRICE_ATTR_NAME)

    def should_be_correct_flyout_cart_title(self, exp_product_title):
        act_product_title = (self.flyout_cart.find_element(*FLYOUT_CART_PRODUCT_TITLE)
                             .get_attribute('textContent').strip())
        assert exp_product_title == act_product_title, Err.ELEMENTS_DO_NOT_MATCH_ERR_MSG.format(
            actual=act_product_title, expected=exp_product_title, el_name=mpAttr.FLYOUT_CART_PRODUCT_TITLE_ATTR_NAME)

    def should_be_correct_flyout_cart_product_color(self, exp_product_color):
        attrs_raw = self.flyout_cart.find_element(*FLYOUT_CART_PRODUCT_ATTRS).text
        act_product_color = PRODUCT_COLOR_REGEX.search(attrs_raw).group(1).strip()
        assert exp_product_color == act_product_color, Err.ELEMENTS_DO_NOT_MATCH_ERR_MSG.format(
            actual=act_product_color, expected=exp_product_color, el_name=mpAttr.FLYOUT_CART_PRODUCT_COLOR_ATTR_NAME)

    # Needs to be updated for different types of products, containing different specific attributes which need to be set
    _DISPATCH = {
        'quantity': set_product_quantity,
        'color': set_product_color,
        'manufacturer': set_product_manufacturer,
    }
