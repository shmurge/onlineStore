import pytest
import allure
from pages.login_page import LoginPage
from utils.data import *


@pytest.mark.positive
@pytest.mark.login_page
class TestLoginPagePositive:
    link = Url.MAIN_PAGE

    @allure.suite("Авторизация")
    @allure.title("Проверка цвета кнопки Войти")
    def test_check_sign_in_button_color(self, browser, clear_cookies_after_test):
        page = LoginPage(browser, self.link)
        page.open(self.link)
        page.accept_cookie()
        page.go_to_login_page()
        page.sign_in_button_check_original_color(ButtonsData.SIGN_IN_ORIGINAL_COLOR)
        page.move_to_sign_in_button()
        page.sign_in_button_check_hover_color(ButtonsData.SIGN_IN_HOVER_COLOR)

    @allure.suite("Авторизация")
    @allure.title("Проверка плэйсхолдеров в инпутах формы авторизации")
    def test_check_placeholders_in_inputs_on_login_form(self, browser, clear_cookies_after_test):
        page = LoginPage(browser, self.link)
        page.open(self.link)
        page.accept_cookie()
        page.go_to_login_page()
        page.should_be_correct_placeholder_in_login_input()
        page.should_be_correct_placeholder_in_password_input()


@pytest.mark.negative
@pytest.mark.login_page
class TestLoginPageNegative:
    link = Url.MAIN_PAGE

    @allure.suite("Авторизация")
    @allure.title("Проверка валидации инпутов без ввода данных")
    def test_login_page_required_field_message_in_inputs(self, browser, clear_cookies_after_test):
        page = LoginPage(browser, self.link)
        page.open(self.link)
        page.accept_cookie()
        page.go_to_login_page()
        page.click_sign_in_without_input_filling()
        page.should_be_required_field_under_login_input()
        page.should_be_required_field_under_password_input()

    @allure.suite("Авторизация")
    @allure.title("Проверка валидации инпута Логин при вводе невалидного email")
    @pytest.mark.parametrize('email', InputData.INVALID_EMAILS)
    def test_login_page_invalid_email(self, browser, email, clear_cookies_after_test):
        page = LoginPage(browser, self.link)
        page.open(self.link)
        page.accept_cookie()
        page.go_to_login_page()
        page.login_input.clear_input()
        page.login_input.send_keys_in_input(email)
        page.sign_in_button.click()
        page.should_be_invalid_email_under_login_input()

    @allure.suite("Авторизация")
    @allure.title("Проверка отсутствия сообщений об ошибках в инпутах при вводе валидных данных")
    def test_missing_input_errors(self, browser, clear_cookies_after_test):
        page = LoginPage(browser, self.link)
        page.open(self.link)
        page.accept_cookie()
        page.go_to_login_page()
        page.click_sign_in_without_input_filling()
        page.should_be_required_field_under_login_input()
        page.should_be_required_field_under_password_input()
        page.password_input.send_keys_in_input("a")
        page.should_not_be_error_message_under_password_input()
        page.password_input.clear_input()
        page.should_be_required_field_under_password_input()
        page.password_input.send_keys_in_input("QwertY123&")
        page.should_not_be_error_message_under_password_input()
        page.login_input.send_keys_in_input("qwerty@qwerty.qw")
        page.should_not_be_error_message_under_login_input()
        page.login_input.clear_input()
        page.should_be_required_field_under_login_input()
        page.login_input.send_keys_in_input("qwerty")
        page.should_be_invalid_email_under_login_input()
        page.login_input.clear_input()
        page.login_input.send_keys_in_input("qwerty@qwerty.qw")
        page.should_not_be_error_message_under_login_input()
