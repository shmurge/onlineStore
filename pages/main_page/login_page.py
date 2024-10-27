import allure
from pages.base_page import BasePage
from elements.base_elements import *
from locators.locs_main_page import MainPageLocators
from locators.locs_login_page import LoginPageLocators
from utils.data import *


class LoginPage(BasePage):

    def __init__(self, browser, url, timeout=10):
        super().__init__(browser, url, timeout)

        self.login_link = Button(self.browser, "Линк на форму логина", *MainPageLocators.LOGIN_LINK)
        self.user_link = Button(self.browser, "Линк на ЛК пользователя", *MainPageLocators.USER_LINK)
        self.login_input = Input(self.browser, "Инпут Логин", *LoginPageLocators.LOGIN_INPUT)
        self.password_input = Input(self.browser, "Инпут Пароль", *LoginPageLocators.PASSWORD_INPUT)
        self.sign_in_button = Button(self.browser, "Кнопка Войти", *LoginPageLocators.SIGN_IN_BUTTON)

    def go_to_login_page(self):
        with allure.step("Переход на страницу логина"):
            self.login_link.click()
        self.should_be_login_form()

    def should_be_login_form(self):
        with allure.step("Проверка наличия формы для авторизации"):
            assert self.is_element_visible(*LoginPageLocators.LOGIN_FRAME), "Форма для авторизации не отображается!"

    def user_login(self, login, password):
        with allure.step("Авторизация пользователя"):
            self.login_input.clear_input()
            self.login_input.send_keys_in_input(login)
            self.password_input.clear_input()
            self.password_input.send_keys_in_input(password)
            self.sign_in_button.click()

    def click_sign_in_without_input_filling(self):
        self.login_input.click()
        self.password_input.click()
        self.sign_in_button.click()

    def sign_in_button_check_original_color(self):
        exp_result = ButtonsData.SIGN_IN_ORIGINAL_COLOR
        act_result = self.sign_in_button.get_button_color()
        with allure.step(f"Проверка исходного цвета: {self.sign_in_button.name}"):
            assert exp_result == act_result, f"Несоответствие исходного цвета! ОР: {exp_result}, ФР: {act_result}"

    def move_to_sign_in_button(self):
        self.move_to_element(*self.sign_in_button.locator, self.sign_in_button.name)

    def sign_in_button_check_hover_color(self):
        exp_result = ButtonsData.SIGN_IN_HOVER_COLOR
        act_result = self.sign_in_button.get_button_color()
        with allure.step(f"Проверка цвета ховера: {self.sign_in_button.name}"):
            assert exp_result == act_result, f"Несоответствие цвета ховера! ОР: {exp_result}, ФР: {act_result}"

    def should_be_user_link(self):
        with allure.step("Проверка наличия ссылки на личный кабинет пользователя"):
            assert self.is_element_visible(*MainPageLocators.USER_LINK), \
                "Ссылка на личный кабинет пользователя не отображается!"

    def should_be_login_link(self):
        with allure.step("Проверка наличия ссылки на страницу авторизации"):
            self.is_element_visible(*MainPageLocators.LOGIN_LINK)

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