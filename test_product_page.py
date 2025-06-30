import pytest
import allure

from pages.productDetailPage import ProductDetailPage
from utils.test_data import ProductDetailPageTestData


@pytest.fixture(scope='function', params=ProductDetailPageTestData.CASES, ids=lambda c: f'prod_id={c["product"].id}')
def case(request):
    return request.param


@pytest.fixture(scope='function')
def product_detail_page(browser, case):
    product_detail_page = ProductDetailPage(browser, case['product'].url)

    return product_detail_page


@allure.story("Product")
@allure.feature("Product list")
@allure.title("Guest can add product to cart")
def test_guest_user_can_add_product_to_cart(product_detail_page, case):
    product = case['product']
    product_detail_page.open()
    product_detail_page.set_product_attributes(product)
    product_detail_page.add_product_to_cart()
    product_detail_page.should_be_correctly_added_product_to_cart(product)
