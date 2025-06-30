from pages.loginPage import LoginPage
from pages.mainPage import CELLPHONE_PRODUCT_LIST_TOP_MENU_LINK
from pages.registerPage import RegisterPage
from pages.productListPage import ProductListPage
from utils.urls import CELLPHONE_PRODUCT_LIST_URL
from utils.messages import PageLabels as pL


class TestRegisterPageFromMainPage:
    def test_guest_should_see_register_link_on_main_page(self, main_page):
        main_page.open()
        main_page.should_be_register_link()

    def test_guest_can_go_to_register_page_from_main_page(self, browser, main_page):
        main_page.open()
        main_page.go_to_register_page()
        register_page = RegisterPage(browser, browser.current_url)
        register_page.should_be_register_page()


class TestLoginPageFromMainPage:
    def test_guest_should_see_login_link_on_main_page(self, main_page):
        main_page.open()
        main_page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_main_page(self, browser, main_page):
        main_page.open()
        main_page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()


class TestProductListPageFromMainPage:
    def test_guest_should_see_cellphone_product_list_link_on_main_page(self, main_page):
        product_list_link = CELLPHONE_PRODUCT_LIST_TOP_MENU_LINK
        main_page.open()
        main_page.should_be_correct_product_list_link(product_list_link=product_list_link, product_title='Cellphone')

    def test_guest_can_go_to_cellphone_product_list_page_from_main_page(self, browser, main_page):
        main_page.open()
        main_page.go_to_cellphone_product_list_page()
        cellphone_product_list_page = ProductListPage(browser, browser.current_url)
        cellphone_product_list_page.should_be_product_list_page(
            expected_url=CELLPHONE_PRODUCT_LIST_URL,
            expected_page_title=pL.CELLPHONE_PRODUCT_LIST_PAGE_TITLE
        )
