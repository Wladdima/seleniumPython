import allure

from pages.loginPage import LoginPage
from pages.mainPage import CELLPHONE_PRODUCT_LIST_TOP_MENU_LINK
from pages.registerPage import RegisterPage
from pages.productListPage import ProductListPage
from utils.urls import CELLPHONE_PRODUCT_LIST_URL
from utils.messages import PageLabels as pL


class TestRegisterPageFromMainPage:
    @allure.story("Register")
    @allure.feature("Register guest")
    @allure.title("Guest should see register link")
    def test_guest_should_see_register_link_on_main_page(self, main_page):
        main_page.open()
        main_page.should_be_register_link()

    @allure.story("Register")
    @allure.feature("Register guest")
    @allure.title("Guest can go to register page")
    def test_guest_can_go_to_register_page_from_main_page(self, browser, main_page):
        main_page.open()
        main_page.go_to_register_page()
        register_page = RegisterPage(browser, browser.current_url)
        register_page.should_be_register_page()


class TestLoginPageFromMainPage:
    @allure.story("Login")
    @allure.feature("Login link")
    @allure.title("Guest can see login link")
    def test_guest_should_see_login_link_on_main_page(self, main_page):
        main_page.open()
        main_page.should_be_login_link()

    @allure.story("Login")
    @allure.feature("Login link")
    @allure.title("Guest can go to login page")
    def test_guest_can_go_to_login_page_from_main_page(self, browser, main_page):
        main_page.open()
        main_page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()


class TestProductListPageFromMainPage:
    @allure.story("Product")
    @allure.feature("Cellphone product")
    @allure.title("Guest should see cellphone product list link")
    def test_guest_should_see_cellphone_product_list_link_on_main_page(self, main_page):
        product_list_link = CELLPHONE_PRODUCT_LIST_TOP_MENU_LINK
        main_page.open()
        main_page.should_be_correct_product_list_link(product_list_link=product_list_link, product_title='Cellphone')

    @allure.story("Product")
    @allure.feature("Cellphone product")
    @allure.title("Guest can go to cellphone product list")
    def test_guest_can_go_to_cellphone_product_list_page_from_main_page(self, browser, main_page):
        main_page.open()
        main_page.go_to_cellphone_product_list_page()
        cellphone_product_list_page = ProductListPage(browser, browser.current_url)
        cellphone_product_list_page.should_be_product_list_page(
            expected_url=CELLPHONE_PRODUCT_LIST_URL,
            expected_page_title=pL.CELLPHONE_PRODUCT_LIST_PAGE_TITLE
        )
