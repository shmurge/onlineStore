import pytest
import allure
from random import *
from pages.base_page import BasePage
from pages.cart_page import CartPage
from pages.header_page import HeaderPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.region_page import RegionPage
from pages.profile_page import ProfilePage
from pages.catalogue_page import CataloguePage
from pages.searching_result_page import SearchingResultPage
from pages.product_page import ProductPage
from pages.product_added_modal_page import ProductAddedModal
from utils.data import *
from time import sleep


@pytest.mark.positive
@pytest.mark.main_page
class TestMainPagePositive:
    link = Url.MAIN_PAGE
    title_ls = []

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.suite("Авторизация")
    @allure.title("Главная: Авторизация")
    def test_authorize(self, browser, clear_cookies_after_test):
        page = LoginPage(browser, self.link)
        page.open(self.link)
        page.accept_cookie()
        page.go_to_login_page()
        page.user_login(*UsersData.USER_1)
        page.should_be_user_link()

    @allure.suite("Локализация")
    @allure.title("Главная: Выбор региона")
    @pytest.mark.parametrize('region', ["Москва и МО", "Санкт-Петербург"])
    @pytest.mark.may_be_login
    def test_choose_region(self, browser, region, clear_cookies_after_test):
        page = RegionPage(browser, self.link)
        page.open(self.link)
        page.accept_cookie()
        page.open_region_modal()
        page.choose_region(region)
        page.should_be_correct_region_in_header(region)

    @allure.suite("Профиль пользователя")
    @allure.title("Главная: Перход в профиль")
    def test_go_to_profile_page(self, browser, preconditions_login, clear_cookies_after_test):
        page = ProfilePage(browser, self.link)
        page.accept_cookie()
        page.go_to_profile_page()
        page.should_be_profile_page()

    @allure.suite("Поиск товара")
    @allure.title("Главная: Поиск товара через каталог")
    @pytest.mark.may_be_login
    def test_search_by_catalogue(self, browser, clear_cookies_after_test):
        header_page = HeaderPage(browser, self.link)
        catalogue_page = CataloguePage(browser, self.link)
        item_type, item_link, item_title = catalogue_page.get_type_link_and_title_from_prod_catalogue()
        header_page.open(self.link)
        header_page.accept_cookie()
        header_page.open_catalogue()
        header_page.select_product_in_catalogue(item_type, item_link)
        catalogue_page.check_searching_result(item_title)

    @allure.suite("Поиск товара")
    @allure.title("Главная: Переход на страницу товара из каталога")
    @pytest.mark.may_be_login
    @pytest.mark.xfail
    def test_go_to_prod_page_from_catalogue(self, browser, clear_cookies_after_test):
        self.test_search_by_catalogue(browser, False)
        page = CataloguePage(browser, browser.current_url)
        title, price = page.select_random_product_card()
        page = ProductPage(browser, browser.current_url)
        page.should_be_correct_product_title_on_prod_page(title)
        page.should_be_correct_product_price_on_prod_page(price)

    @allure.suite("Поиск товара")
    @allure.title("Главная: Поиск товара через главный инпут поиска")
    @pytest.mark.parametrize("product_name", ProductName.PRODUCT_NAMES_LIST)
    @pytest.mark.may_be_login
    @pytest.mark.xfail
    def test_search_by_main_search_input(self, browser, product_name, clear_cookies_after_test):
        page = HeaderPage(browser, self.link)
        page.open(self.link)
        page.accept_cookie()
        page.search_product_by_main_search_input(product_name)
        page = SearchingResultPage(browser, browser.current_url)
        page.check_searching_result(product_name)

    @allure.suite("Поиск товара")
    @allure.title("Главная: Переход на страницу товара со страницы поиска")
    @pytest.mark.parametrize("product_name", [*ProductName.PRODUCT_NAMES_LIST])
    @pytest.mark.may_be_login
    @pytest.mark.xfail
    def test_go_to_prod_page_from_searching_result_page(self, browser, product_name, clear_cookies_after_test):
        self.test_search_by_main_search_input(browser, product_name, False)
        page = SearchingResultPage(browser, browser.current_url)
        title, price = page.select_random_product_card()
        page = ProductPage(browser, browser.current_url)
        page.should_be_correct_product_title_on_prod_page(title)
        page.should_be_correct_product_price_on_prod_page(price)

    @allure.suite("Корзина")
    @allure.title("Главная: Переход в корзину")
    @pytest.mark.may_be_login
    def test_go_to_cart_page(self, browser, clear_cookies_after_test):
        page = CartPage(browser, self.link)
        page.open(self.link)
        page.accept_cookie()
        page.go_to_cart_page()
        page.should_be_cart_page()

    @allure.suite("Корзина")
    @allure.title("Главная: Проверка наличия сообщения о пустой корзине")
    @pytest.mark.may_be_login
    def test_check_empty_cart_message(self, browser, clear_cookies_after_test):
        page = CartPage(browser, self.link)
        page.open(self.link)
        page.accept_cookie()
        page.go_to_cart_page()
        page.should_be_message_empty_cart()

    @allure.suite("Корзина")
    @allure.title("Главная/каталог: Добавить товар в корзину со станицы товара и продолжить покупки")
    @pytest.mark.may_be_login
    def test_add_to_cart_from_prod_page_from_catalogue_and_continue_shopping(self, browser, clear_cookies_after_test):
        self.test_go_to_prod_page_from_catalogue(browser, False)
        quantity = 0
        product_page = ProductPage(browser, browser.current_url)
        prod_title, prod_price = product_page.get_title_and_price()
        product_page.check_buy_button_text(ButtonsData.TEXT_IN_PROD_PAGE_BUY_BUTTON)
        product_page.add_to_cart(prod_title)
        quantity += 1
        product_added_modal = ProductAddedModal(browser, browser.current_url)
        product_added_modal.should_be_buy_options_modal()
        product_added_modal.continue_shopping()
        product_page.check_go_to_cart_button_text(ButtonsData.TEXT_IN_PROD_PAGE_GO_TO_CART_BUTTON)
        product_page.check_quantity_positions_in_cart(quantity)

    @allure.suite("Корзина")
    @allure.title("Главная/каталог: Добавить товар в корзину со станицы товара и перейти к оформлению")
    @pytest.mark.may_be_login
    def test_add_to_cart_from_prod_page_from_catalogue_and_place_an_order(self, browser, clear_cookies_after_test):
        self.test_go_to_prod_page_from_catalogue(browser, False)
        product_page = ProductPage(browser, browser.current_url)
        cart_page = CartPage(browser, browser.current_url)
        prod_title, prod_price = product_page.get_title_and_price()
        product_page.add_to_cart(prod_title)
        product_added_modal = ProductAddedModal(browser, browser.current_url)
        product_added_modal.should_be_buy_options_modal()
        product_added_modal.place_an_order()
        cart_page.check_quantity_and_price_positions_in_cart()
        cart_page.check_total_price_in_cart_and_in_header()

    @allure.suite("Корзина")
    @allure.title("Главная: Добавить два товара в корзину (через каталог и через поиск)")
    @pytest.mark.may_be_login
    @pytest.mark.xfail
    @pytest.mark.test
    def test_add_to_cart_two_prods_from_catalog_and_from_main_search(self, browser, clear_cookies_after_test):
        self.test_go_to_prod_page_from_catalogue(browser, False)
        product_page = ProductPage(browser, browser.current_url)
        header_page = HeaderPage(browser, browser.current_url)
        search_res_page = SearchingResultPage(browser, browser.current_url)
        cart_page = CartPage(browser, browser.current_url)
        prod_title, prod_price = product_page.get_title_and_price()
        self.title_ls.append(prod_title)
        product_page.check_buy_button_text(ButtonsData.TEXT_IN_PROD_PAGE_BUY_BUTTON)
        product_page.add_to_cart(prod_title)
        product_added_modal = ProductAddedModal(browser, browser.current_url)
        product_added_modal.should_be_buy_options_modal()
        product_added_modal.continue_shopping()
        product_page.check_go_to_cart_button_text(ButtonsData.TEXT_IN_PROD_PAGE_GO_TO_CART_BUTTON)
        header_page.search_product_by_main_search_input(choice(ProductName.PRODUCT_NAMES_LIST))
        search_res_page.select_random_product_card()
        prod_title, prod_price = product_page.get_title_and_price()
        self.title_ls.append(prod_title)
        product_page.check_buy_button_text(ButtonsData.TEXT_IN_PROD_PAGE_BUY_BUTTON)
        product_page.add_to_cart(prod_title)
        product_added_modal = ProductAddedModal(browser, browser.current_url)
        product_added_modal.should_be_buy_options_modal()
        product_added_modal.continue_shopping()
        product_page.check_go_to_cart_button_text(ButtonsData.TEXT_IN_PROD_PAGE_GO_TO_CART_BUTTON)
        product_page.go_to_cart()
        cart_page.check_quantity_and_price_positions_in_cart()
        cart_page.check_total_price_in_cart_and_in_header()

    @allure.suite("Корзина")
    @allure.title("Удалить товар из корзины")
    @pytest.mark.may_be_login
    def test_remove_position_from_cart(self, browser, clear_cookies_after_test):
        self.test_add_to_cart_from_prod_page_from_catalogue_and_place_an_order(browser, False)
        cart_page = CartPage(browser, browser.current_url)
        cart_page.check_quantity_and_price_positions_in_cart()
        cart_page.check_total_price_in_cart_and_in_header()
        cart_page.remove_random_position_from_cart()
        cart_page.should_be_message_empty_cart()

    @allure.suite("Корзина")
    @allure.title("Добавить два товара в корзину и удалить 1 рандомный товар")
    @pytest.mark.may_be_login
    def test_remove_random_position_from_cart(self, browser, clear_cookies_after_test):
        self.test_add_to_cart_two_prods_from_catalog_and_from_main_search(browser, False)
        cart_page = CartPage(browser, browser.current_url)
        deleted_pos = cart_page.remove_random_position_from_cart()
        cart_page.should_not_be_position_in_cart(deleted_pos)


@pytest.mark.negative
@pytest.mark.main_page
class TestMainPageNegative:
    link = TestMainPagePositive.link

    @allure.suite("Поиск товара")
    @allure.title("Главная: Проверка всех доступных позиций в каталоге")
    @pytest.mark.parametrize("item_type, item_link, item_name",
                             [(key, *item) for key, items in Catalogue.CATALOGUE.items() for item in items])
    @pytest.mark.may_be_login
    def test_check_all_positions_in_catalogue_from_main_page(self, browser, item_type, item_link,
                                                             item_name, clear_cookies_after_test):
        page = HeaderPage(browser, self.link)
        page.open(self.link)
        page.accept_cookie()
        page.open_catalogue()
        page.select_product_in_catalogue(item_type, item_link)
        page = CataloguePage(browser, browser.current_url)
        page.check_searching_result(item_name)
