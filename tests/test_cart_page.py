from time import sleep
import allure
import pytest
from random import *
from pages.base_page import BasePage
from pages.cart_page import CartPage
from utils.api_features import *
from utils.data import *
from utils.data_for_api import *


@pytest.mark.positive
@pytest.mark.cart_page
class TestCartPagePositive:
    link = Url.CART_PAGE

    @allure.suite("Корзина")
    @allure.title("Удалить единственный товар из корзины")
    @pytest.mark.may_be_login
    def test_remove_only_position_from_cart(self, browser, clear_cookies_after_test):
        page = CartPage(browser, self.link)
        page.open(self.link)
        prod_id = choice(ProductsData.ID)
        page.precond_add_prods_to_cart(prod_id)
        page.refresh()
        page.accept_cookie()
        page.remove_random_position_from_cart()
        page.should_be_message_empty_cart()


    @allure.suite("Корзина")
    @allure.title("Удалить один товар из корзины, когда в корзине несколько товаров")
    @pytest.mark.may_be_login
    def test_remove_random_position_from_cart(self, browser, clear_cookies_after_test):
        page = CartPage(browser, self.link)
        page.open(self.link)
        page.precond_add_prods_to_cart(*ProductsData.ID)
        page.refresh()
        page.accept_cookie()
        deleted_pos = page.remove_random_position_from_cart()
        page.should_not_be_position_in_cart(deleted_pos)