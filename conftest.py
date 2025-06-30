import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.mainPage import MainPage
from pages.loginPage import LoginPage
from pages.registerPage import RegisterPage
from utils.urls import MAIN_PAGE_URL, LOGIN_URL, REGISTER_URL


def pytest_addoption(parser):
    parser.addoption(
        '--browser_name',
        action='store',
        default='chrome',
        help='Choose browser: chrome or firefox'
    )


@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption('browser_name')

    if browser_name == 'chrome':
        opts = Options()
        opts.add_argument("--window-size=1920,1080")
        opts.add_argument("--headless=new")
        opts.add_argument("--no-sandbox")
        opts.add_argument("--disable-dev-shm-usage")
        browser = webdriver.Chrome(options=opts)
    elif browser_name == 'firefox':
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError('--browser_name should be chrome or firefox')

    yield browser

    browser.quit()


@pytest.fixture(scope='function')
def main_page(browser):
    main_page = MainPage(browser, MAIN_PAGE_URL)

    return main_page


@pytest.fixture(scope='function')
def login_page(browser):
    login_page = LoginPage(browser, LOGIN_URL)

    return login_page


@pytest.fixture(scope='function')
def register_page(browser):
    register_page = RegisterPage(browser, REGISTER_URL)

    return register_page
