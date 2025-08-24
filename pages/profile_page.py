from pages.header_page import HeaderPage
from elements.elements import *
from locators.locs_profile_page import ProfilePageLocators
from src.data.data import *


class ProfilePage(HeaderPage):

    def __init__(self, browser, url):
        super().__init__(browser, url)

        self.logout_button = Button(self.browser, "Кнопка Выйти из аккаунта", *ProfilePageLocators.LOGOUT_BUTTON)

    def should_be_profile_page(self):
        with allure.step("Проверка наличия страницы профиля"):
            self.should_be_correct_url(ProfilePageLocators.PROFILE_PATH_PARAM)
            self.should_be_profile_card()

    def should_be_profile_card(self):
        with allure.step("Проверка наличия карточки пользователя"):
            assert self.is_element_visible(*ProfilePageLocators.PROFILE_CARD), "Карточка пользователя не отображается!"

    def should_be_correct_username_in_profile_card(self):
        with allure.step("Проверка корректности имени пользователя в карточке профиля"):
            exp_res = UsersData.USER_1_NAME
            act_res = self.get_element(*ProfilePageLocators.USER_NAME).text
            assert exp_res == act_res, (f'Некорректное имя пользователя в карточке профиля! '
                                        f'ОР: {exp_res}, ФР: {act_res}')

    def should_be_correct_email_in_profile_card(self):
        with allure.step("Проверка корректности email в карточке профиля"):
            exp_res = UsersData.USER_1[0]
            act_res = self.get_element(*ProfilePageLocators.USER_EMAIL).text
            assert exp_res == act_res, (f'Некорректный email в карточке профиля! '
                                        f'ОР: {exp_res}, ФР: {act_res}')

    def logout(self):
        with allure.step("Выход из аккаунта"):
            self.logout_button.click()
