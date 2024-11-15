import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from pages.login_page import LoginPage
from utils.data import *


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome', help='Choose browser: chrome or firefox')
    parser.addoption('--language', action='store', default='ru', help='Choose language: ru or en')
    parser.addoption('--headless', action='store_true', help='Launching the browser in headless mode')
    parser.addoption('--login', action='store_true', help='Launching the browser with pre conditions: login')


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser")
    user_language = request.config.getoption("language")
    headless = request.config.getoption("--headless")
    need_login = request.config.getoption("--login")
    browser = None

    with allure.step(f"Запуск браузера: {browser_name}.  Язык браузера: {user_language}"):
        if browser_name == "chrome":
            chrome_options = ChromeOptions()
            chrome_options.add_argument("--disable-notifications")
            chrome_options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
            if headless:
                with allure.step("Браузер запущен в фоновом режиме"):
                    chrome_options.add_argument('--headless')
                    chrome_options.add_argument('--disable-gpu')
                    chrome_options.add_argument('--no-sandbox')
                    chrome_options.add_argument('--disable-dev-shm-usage')
            browser = webdriver.Chrome(options=chrome_options)
        elif browser_name == "firefox":
            firefox_options = FirefoxOptions()
            firefox_options.set_preference('intl.accept_languages', user_language)
            if headless:
                with allure.step("Браузер запущен в фоновом режиме"):
                    firefox_options.headless = True
            browser = webdriver.Firefox(options=firefox_options)
        else:
            raise pytest.UsageError("--browser_name should be chrome or firefox")

    browser.maximize_window()

    if need_login:
        login_in_app(browser)

    yield browser
    browser.quit()

def login_in_app(browser, link=Url.MAIN_PAGE):
    with allure.step("Предусловия: авторизация"):
        page = LoginPage(browser, link)
        page.open(link)
        page.check_cooke_alert()
        page.go_to_login_page()
        page.user_login(*UsersData.USER_1)
        page.should_be_user_link()

@pytest.fixture(scope="function")
def preconditions_login(browser, link=Url.MAIN_PAGE):
    login_in_app(browser, link)

@pytest.fixture(scope="function")
def get_browser_language(browser):
    browser_language = browser.execute_script("return navigator.language").upper()
    return browser_language
