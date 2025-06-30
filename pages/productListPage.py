from selenium.webdriver.common.by import By

from pages.basePage import BasePage
from utils.attributes import ProductDetailPageAttributes as dpAttr
from utils.messages import ErrorMessages as Err


PRODUCT_LIST_PAGE_TITLE = (By.CSS_SELECTOR, 'div.page-title h1')
DYNAMIC_PRODUCT_ID_AND_TITLE_LOCATOR = (
    By.XPATH,
    '//div[@class="product-grid"]//div[@data-productid="{prod_id}"]'
    '//a[normalize-space(text())="{prod_title}"]',
)
DYNAMIC_LINK_TO_PRODUCT_DETAIL_PAGE = (
    By.CSS_SELECTOR,
    'div.product-grid  div[data-productid="{prod_id}"] h2.product-title a'
)


class ProductListPage(BasePage):
    def should_be_product_list_page(self, expected_url, expected_page_title):
        self.should_be_correct_url(expected_url)
        self.should_be_correct_page_title(expected_page_title)

    def should_be_correct_page_title(self, expected_page_title):
        actual_page_title = self.browser.find_element(*PRODUCT_LIST_PAGE_TITLE).text
        assert expected_page_title == actual_page_title, Err.ELEMENTS_DO_NOT_MATCH_ERR_MSG.format(
            actual=actual_page_title, expected=expected_page_title)

    def should_be_correct_product_on_page(self, product):
        locator_type, locator = DYNAMIC_PRODUCT_ID_AND_TITLE_LOCATOR
        assert self.is_element_present(locator_type, locator.format(prod_id=product.id, prod_title=product.title)), (
            Err.ELEMENT_IS_MISSING_ERR_MSG.format(
                element=f'{dpAttr.PRODUCT_ID_ATTR_NAME}="{product.id}\" with product title \"{product.title}"')
        )

    def go_to_product_detail_page(self, product):
        locator_type, locator = DYNAMIC_LINK_TO_PRODUCT_DETAIL_PAGE
        self.go_to_page_via_link(locator_type, locator.format(prod_id=product.id))
