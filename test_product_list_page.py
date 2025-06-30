import pytest

from pages.productDetailPage import ProductDetailPage
from pages.productListPage import ProductListPage
from utils.test_data import ProductListPageTestData


@pytest.fixture(scope='function', params=ProductListPageTestData.CASES, ids=lambda c: f'prod_id={c["product"].id}')
def case(request):
    return request.param

@pytest.fixture(scope='function')
def product_list_page(browser, case):
    product_list_page = ProductListPage(browser, case['prod_list_url'])

    return product_list_page

def test_guest_user_can_see_correct_product_on_product_list_page(product_list_page, case):
    product_list_page.open()
    product = case['product']
    product_list_page.should_be_correct_product_on_page(product)

def test_guest_user_can_go_to_product_detail_page(browser, product_list_page, case):
    product = case['product']
    product_list_page.open()
    product_list_page.go_to_product_detail_page(product)
    product_detail_page = ProductDetailPage(browser, browser.current_url)
    product_detail_page.should_be_correct_product_detail_page(product)
