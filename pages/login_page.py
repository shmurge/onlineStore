from locators.locs_login_page import LoginPageLocators
from elements.elements import *
from pages.header_page import HeaderPage
from src.data.data import *
from time import sleep


class LoginPage(HeaderPage):

    def __init__(self, browser, url):
        super().__init__(browser, url)

    def click_sign_in_without_input_filling(self):
        sleep(0.5) # sleep добавлен из-за особенности работы firefox (или защиты приложения от автоматизации)
        self.login_input.click()
        self.password_input.click()
        self.sign_in_button.click()

    def sign_in_button_check_original_color(self, exp_res):
        with allure.step(f"Проверка исходного цвета: {self.sign_in_button.name}"):
            self.sign_in_button.check_button_color(exp_res)

    def move_to_sign_in_button(self):
        self.move_to_element(*self.sign_in_button.locator, self.sign_in_button.name)

    def sign_in_button_check_hover_color(self, exp_res):
        with allure.step(f"Проверка цвета ховера: {self.sign_in_button.name}"):
            self.sign_in_button.check_button_color(exp_res)

    def should_be_required_field_under_login_input(self):
        exp_message = InputErrors.LOGIN_REQUIRED
        with allure.step(f"Под {self.login_input.name} должна отображаться ошибка: {InputErrors.LOGIN_REQUIRED}"):
            self.login_input.check_input_error_message(
                *LoginPageLocators.LOGIN_INPUT_VALIDATION_MESSAGE, exp_message)

    def should_be_required_field_under_password_input(self):
        exp_message = InputErrors.PASSWORD_REQUIRED
        with allure.step(f"Под {self.password_input.name} должна отображаться ошибка: {InputErrors.PASSWORD_REQUIRED}"):
            self.password_input.check_input_error_message(
                *LoginPageLocators.PASSWORD_INPUT_VALIDATION_MESSAGE, exp_message)

    def should_be_invalid_email_under_login_input(self):
        exp_message = InputErrors.INVALID_LOGIN
        with allure.step(f"Под {self.login_input.name} должна отображаться ошибка: {InputErrors.INVALID_LOGIN}"):
            self.login_input.check_input_error_message(
                *LoginPageLocators.LOGIN_INPUT_VALIDATION_MESSAGE, exp_message)

    def should_not_be_error_message_under_login_input(self):
        with allure.step(f"Сообщение об ошибке в {self.login_input.name} не должно отображаться!"):
            self.login_input.check_missing_validation_message(
                *LoginPageLocators.LOGIN_INPUT_VALIDATION_MESSAGE)

    def should_not_be_error_message_under_password_input(self):
        with allure.step(f"Сообщение об ошибке в {self.password_input.name} не должно отображаться!"):
            self.password_input.check_missing_validation_message(
                *LoginPageLocators.PASSWORD_INPUT_VALIDATION_MESSAGE)

    def should_be_correct_placeholder_in_login_input(self):
        self.login_input.check_placeholder(Placeholders.LOGIN_INPUT)

    def should_be_correct_placeholder_in_password_input(self):
        self.password_input.check_placeholder(Placeholders.PASSWORD_INPUT)
