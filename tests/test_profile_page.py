import pytest
import allure
from pages.profile_page import ProfilePage
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
        page.should_be_correct_email_in_profile_card()
        page.should_be_correct_username_in_profile_card()
