import pytest

from pages.cartPage import CartPage
from pages.productDetailPage import ProductDetailPage
from utils.test_data import CartPageTestData
from utils.urls import CART_PAGE_URL


@pytest.fixture(scope='function', params=CartPageTestData.CASES, ids=lambda c: f'prod_id={c["product"].id}')
def case(request):
    return request.param

def test_correct_product_info_is_displayed_on_cart_page(browser, case):
    product = case['product']
    product_detail_page = ProductDetailPage(browser, product.url)
    product_detail_page.open()
    product_detail_page.set_product_attributes(product)
    product_detail_page.add_product_to_cart()
    cart_page = CartPage(browser, CART_PAGE_URL)
    cart_page.open()
    cart_page.should_be_correct_cart_data(product)
