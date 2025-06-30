from decimal import Decimal
from selenium.webdriver.common.by import By

from pages.basePage import BasePage
from utils.messages import ErrorMessages as Err
from utils.attributes import CartPageAttributes as cptAttr
from utils.regex import PRODUCT_COLOR_REGEX


CART_PRODUCT_ROW = (By.CSS_SELECTOR, '.cart .cart-item-row')
CART_PRODUCT_ATTRS = (By.CSS_SELECTOR, '.cart-item-row .attributes')
CART_PRODUCT_TITLE = (By.CSS_SELECTOR, '.product-name')
CART_PRODUCT_PRICE = (By.CSS_SELECTOR, '.product-unit-price')
CART_PRODUCT_QUANTITY = (By.CSS_SELECTOR, '.qty-input')
CART_SUB_TOTAL_PRICE = (By.XPATH, ("//td[@class='cart-total-left'] "
                                        "[span/text()='Sub-Total:'] "
                                        "/following-sibling::td[@class='cart-total-right'] "
                                        "//span[@class='product-price']"))



class CartPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)
        self.product_row = None

    def should_be_correct_cart_data(self, product):
        self.should_be_correct_product_in_cart(product)
        self.should_be_correct_subtotal_price(product.price, product.quantity)

    def should_be_correct_product_in_cart(self, product):
        self.product_row = self.wait_until_element_is_visible(self.browser, CART_PRODUCT_ROW)

        self.should_be_correct_product_title(product.title)
        self.should_be_correct_product_price(product.price)
        self.should_be_correct_product_color(product.color)
        self.should_be_correct_product_quantity(product.quantity)


    def should_be_correct_product_title(self, exp_product_title):
        act_product_title = self.product_row.find_element(*CART_PRODUCT_TITLE).text.strip()
        assert exp_product_title == act_product_title, Err.ELEMENTS_DO_NOT_MATCH_ERR_MSG.format(
            actual=act_product_title, expected=exp_product_title, el_name=cptAttr.CART_PRODUCT_TITLE_ATTR_NAME)

    def should_be_correct_product_price(self, exp_product_price):
        act_product_price = self.product_row.find_element(*CART_PRODUCT_PRICE).text.strip()
        assert exp_product_price == act_product_price, Err.ELEMENTS_DO_NOT_MATCH_ERR_MSG.format(
            actual=act_product_price, expected=exp_product_price, el_name=cptAttr.CART_PRODUCT_PRICE_ATTR_NAME)

    def should_be_correct_product_color(self, exp_product_color):
        attrs_raw = self.product_row.find_element(*CART_PRODUCT_ATTRS).text
        act_product_color = PRODUCT_COLOR_REGEX.search(attrs_raw).group(1).strip()
        assert exp_product_color == act_product_color, Err.ELEMENTS_DO_NOT_MATCH_ERR_MSG.format(
            actual=act_product_color, expected=exp_product_color, el_name=cptAttr.CART_PRODUCT_COLOR_ATTR_NAME)

    def should_be_correct_product_quantity(self, exp_product_quantity):
        act_product_quantity = self.product_row.find_element(*CART_PRODUCT_QUANTITY).get_attribute('value').strip()
        assert exp_product_quantity == act_product_quantity, Err.ELEMENTS_DO_NOT_MATCH_ERR_MSG.format(
            actual=act_product_quantity, expected=exp_product_quantity, el_name=cptAttr.CART_PRODUCT_QUANTITY_ATTR_NAME)

    def should_be_correct_subtotal_price(self, exp_product_price, exp_product_quantity):
        exp_subtotal_price = Decimal(exp_product_price) * int(exp_product_quantity)
        exp_subtotal_price = f'{exp_subtotal_price:,.2f}'
        act_subtotal_price = self.browser.find_element(*CART_SUB_TOTAL_PRICE).text.strip()
        assert exp_subtotal_price == act_subtotal_price, Err.ELEMENTS_DO_NOT_MATCH_ERR_MSG.format(
            actual=act_subtotal_price, expected=exp_subtotal_price, el_name=cptAttr.CART_SUBTOTAL_PRICE_ATTR_NAME)
