import random
import pytest
import allure
from random import *
from pages.header_page import HeaderPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.region_page import RegionPage
from pages.profile_page import ProfilePage
from pages.product_page import ProductPage
from utils.data import *
from time import sleep


@pytest.mark.positive
class TestMainPagePositive:
    link = Url.MAIN_PAGE

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.suite("Авторизация")
    @allure.title("Главная: Пользователь может авторизоваться в приложении")
    def test_user_can_login_in_app_from_main_page(self, browser):
        page = LoginPage(browser, self.link)
        page.open(self.link)
        page.go_to_login_page()
        page.user_login(*UsersData.USER_1)
        page.should_be_user_link()

    @allure.suite("Локализация")
    @allure.title("Главная: Выбор региона")
    @pytest.mark.parametrize('region', ["Москва и МО", "Санкт-Петербург"])
    @pytest.mark.may_be_login
    def test_choose_region_from_main_page(self, browser, region):
        page = RegionPage(browser, self.link)
        page.open(self.link)
        page.open_region_modal()
        page.choose_region(region)
        page.should_be_correct_region_in_header(region)

    @allure.suite("Профиль пользователя")
    @allure.title("Главная: Авторизованный пользователь может перейти в свой профиль")
    def test_authorized_user_can_go_to_profile_page_from_main_page(self, browser, preconditions_login):
        page = ProfilePage(browser, self.link)
        page.go_to_profile_page()
        page.should_be_profile_page()

    @allure.suite("Поиск товара")
    @allure.title("Главная: Пользователь может найти товар через каталог")
    @pytest.mark.may_be_login
    def test_user_can_find_product_by_catalogue_from_main_page(self, browser):
        item_type = choice(list(Catalogue.CATALOGUE))
        item = choice(Catalogue.CATALOGUE[item_type])
        item_link = item[0]
        item_name = item[1]
        page = HeaderPage(browser, self.link)
        page.open(self.link)
        page.open_catalogue()
        page.select_product_in_catalogue(item_type, item_link)
        page = ProductPage(browser, browser.current_url)
        page.check_searching_result(item_name)

    @allure.suite("Поиск товара")
    @allure.title("Главная: Пользователь может найти товар главный инпут поиска")
    @pytest.mark.parametrize("product_name", ["Xiaomi Redmi Note 10 Pro", "iPhone 15", "Huawei Matepad SE 11",
                                              "Samsung Galaxy Tab S9", "Ноутбук Asus Vivobook", "Ноутбук Asus Zenbook",
                                              "Ноутбук HP EliteBook", "Ноутбук HP ProBook", "Xiaomi Mi Smart Band 9"])
    @pytest.mark.may_be_login
    @pytest.mark.test
    def test_user_can_find_product_by_main_search_input(self, browser, product_name):
        page = HeaderPage(browser, self.link)
        page.open(self.link)
        page.search_product_by_main_search_input(product_name)
        page.check_searching_result(product_name)

@pytest.mark.negative
class TestMainPageNegative:
    link = TestMainPagePositive.link

    @allure.suite("Поиск товара")
    @allure.title("Главная: Проверка всех доступных позиций в каталоге")
    @pytest.mark.parametrize("item_type, item_link, item_name",
                             [(key, *item) for key, items in Catalogue.CATALOGUE.items() for item in items])
    @pytest.mark.may_be_login
    @pytest.mark.test
    def test_check_all_positions_in_catalogue_from_main_page(self, browser, item_type, item_link, item_name):
        page = HeaderPage(browser, self.link)
        page.open(self.link)
        page.open_catalogue()
        page.select_product_in_catalogue(item_type, item_link)
        page.check_searching_result(item_name)
