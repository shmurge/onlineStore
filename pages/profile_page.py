import allure
from pages.base_page import BasePage
from elements.base_elements import *
from locators.locs_main_page import MainPageLocators
from locators.locs_profile_page import ProfilePageLocators
from utils.data import *


class ProfilePage(BasePage):

    def __init__(self, browser, url, timeout=10):
        super().__init__(browser, url, timeout)

        self.profile_link = Button(self.browser, "Ссылка на профиль юзера", *MainPageLocators.USER_LINK)
        self.logout_button = Button(self.browser, "Кнопка Выйти из аккаунта", *ProfilePageLocators.LOGOUT_BUTTON)

    def go_to_profile_page(self):
        with allure.step("Переход на страницу профиля"):
            self.profile_link.click()

    def should_be_profile_page(self):
        with allure.step("Проверка наличия страницы профиля"):
            self.should_be_correct_url("profile")
            self.should_be_profile_card()

    def should_be_profile_card(self):
        with allure.step("Проверка наличия карточки пользователя"):
            assert self.is_element_visible(*ProfilePageLocators.PROFILE_CARD), "Карточка пользователя не отображается!"

    def should_be_correct_username_in_profile_card(self):
        with allure.step("Проверка корректности имени пользователя в карточке профиля"):
            exp_res = UsersData.USER_1_NAME
            act_res = self.browser.find_element(*ProfilePageLocators.USER_NAME).text
            assert exp_res == act_res, (f'Некорректное имя пользователя в карточке профиля! '
                                        f'ОР: {exp_res}, ФР: {act_res}')

    def should_be_correct_email_in_profile_card(self):
        with allure.step("Проверка корректности email в карточке профиля"):
            exp_res = UsersData.USER_1[0]
            act_res = self.browser.find_element(*ProfilePageLocators.USER_EMAIL).text
            assert exp_res == act_res, (f'Некорректный email в карточке профиля! '
                                        f'ОР: {exp_res}, ФР: {act_res}')
