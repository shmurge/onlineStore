import pytest
import allure
from pages.profile_page import ProfilePage
from pages.region_page import RegionPage
from utils.data import *
from time import sleep


@pytest.mark.positive
class TestProfilePagePositive:
    link = Url.PROFILE_PAGE

    @allure.suite("Профиль пользователя")
    @allure.title("В карточке профиля email и имя пользователя должны быть корректными")
    def test_should_be_correct_email_and_username_in_profile_card(self, browser, preconditions_login):
        page = ProfilePage(browser, self.link)
        page.open(self.link)
        page.check_cookie_alert()
        page.should_be_correct_email_in_profile_card()
        page.should_be_correct_username_in_profile_card()

    @allure.suite("Профиль пользователя")
    @allure.title("Пользователь может выйти из аккаунта")
    def test_user_can_logout_of_the_account(self, browser, preconditions_login):
        page = ProfilePage(browser, self.link)
        page.check_cookie_alert()
        page.open(self.link)
        page.logout()
        page.should_be_login_link()

    @allure.suite("Локализация")
    @allure.title("Профиль: Выбор региона")
    @pytest.mark.parametrize('region', ["Москва и МО", "Санкт-Петербург"])
    @pytest.mark.may_be_login
    def test_choose_region_from_profile_page(self, browser, region, preconditions_login):
        page = RegionPage(browser, self.link)
        page.check_cookie_alert()
        page.open(self.link)
        page.open_region_modal()
        page.choose_region(region)
        page.should_be_correct_region_in_header(region)
