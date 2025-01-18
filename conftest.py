import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from pages.login_page import LoginPage
from utils.data import *


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome', help='Choose browser: chrome or firefox')
    parser.addoption('--language', action='store', default='ru', help='Choose language: ru or en')
    parser.addoption('--headless', action='store_true', help='Launching the browser in headless mode')
    parser.addoption('--login', action='store_true', help='Launching the browser with pre conditions: login')


@pytest.fixture(scope="session")
def browser(request):
    browser_name = request.config.getoption("browser")
    user_language = request.config.getoption("language")
    headless = request.config.getoption("--headless")
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
            firefox_service = FirefoxService(executable_path="/snap/bin/geckodriver") #если сломается, убрать эту строку
            firefox_options.add_argument("--disable-notifications")
            firefox_options.set_preference('intl.accept_languages', user_language)
            if headless:
                with allure.step("Браузер запущен в фоновом режиме"):
                    firefox_options.add_argument("--headless")
                    firefox_options.add_argument('--disable-gpu')
                    firefox_options.add_argument('--no-sandbox')
                    firefox_options.add_argument('--disable-dev-shm-usage')
            browser = webdriver.Firefox(options=firefox_options, service=firefox_service) # и отсюда убрать service
        else:
            raise pytest.UsageError("--browser_name should be chrome or firefox")

    browser.maximize_window()

    yield browser
    browser.quit()


def login_in_app(browser, link=Url.MAIN_PAGE):
    with allure.step("Предусловия: авторизация"):
        page = LoginPage(browser, link)
        page.open(link)
        page.go_to_login_page()
        page.user_login(*UsersData.USER_1)
        page.should_be_user_link()

@pytest.fixture(autouse=True)
def login(browser, request):
    need_login = request.config.getoption("--login")
    if need_login:
        login_in_app(browser, link=Url.MAIN_PAGE)


@pytest.fixture(scope="function")
def preconditions_login(browser, link=Url.MAIN_PAGE):
    login_in_app(browser, link)


@pytest.fixture(scope="function")
def clear_cookies_after_test(browser, flag=True):
    if flag:
        yield
        with allure.step("Очистить все куки"):
            browser.delete_all_cookies()
