import pytest
import allure
from pages.header_page import HeaderPage
from pages.profile_page import ProfilePage
from utils.data import *


@pytest.mark.positive
@pytest.mark.profile_page
class TestProfilePagePositive:
    link = Url.PROFILE_PAGE

    @allure.suite("Профиль пользователя")
    @allure.title("Проверка корректности email и имени пользователя в карточке профиля")
    def test_should_be_correct_email_and_username_in_profile_card(self, browser, preconditions_login,
                                                                  clear_cookies_after_test):
        page = ProfilePage(browser, self.link)
        page.open(self.link)
        page.accept_cookie()
        page.should_be_correct_email_in_profile_card()
        page.should_be_correct_username_in_profile_card()

    @allure.suite("Профиль пользователя")
    @allure.title("Выход из аккаунта")
    def test_user_can_logout_of_the_account(self, browser, preconditions_login, clear_cookies_after_test):
        page = ProfilePage(browser, self.link)
        page.accept_cookie()
        page.open(self.link)
        page.logout()
        page.should_be_login_link()

    @allure.suite("Локализация")
    @allure.title("Профиль: Выбор региона")
    @pytest.mark.parametrize('region', ["Москва и МО", "Санкт-Петербург"])
    def test_choose_region_from_profile_page(self, browser, region, preconditions_login, clear_cookies_after_test):
        page = HeaderPage(browser, self.link)
        page.accept_cookie()
        page.open(self.link)
        page.open_region_modal()
        page.choose_region(region)
        page.should_be_correct_region_in_header(region)
