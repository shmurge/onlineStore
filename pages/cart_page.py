import allure
from random import *
from selenium.webdriver.common.action_chains import ActionChains as AC
from pages.header_page import HeaderPage
from elements.base_elements import *
from locators.locs_region_page import RegionPageLocators
from locators.locs_header_page import HeaderPageLocators
from locators.locs_login_page import LoginPageLocators
from locators.locs_profile_page import ProfilePageLocators
from locators.locs_product_page import ProductPageLocators
from locators.locs_catalogue_page import CataloguePageLocators
from locators.locs_cart_page import CartPageLocators
from utils.data import *


class CartPage(HeaderPage):

    def should_be_cart_page(self):
        with allure.step("Проверить отображение страницы корзины"):
            self.should_be_correct_url(CartPageLocators.CART_PATH_PARAM)
            assert self.is_element_visible(*CartPageLocators.CART), "Не отображается страница корзины!"

    def should_be_message_empty_cart(self):
        with allure.step("Проверить отображение сообщения о пустой корзине"):
            message = self.browser.find_element(*CartPageLocators.EMPTY_CART_MESSAGE).is_displayed()
            assert message, "Не отображается сообщение 'Корзина пуста'!"

    def check_product_position_in_cart(self, *args):
        title_list =[elem.text for elem in self.browser.find_elements(*CartPageLocators.PROD_TITLE)]
        for arg in args:
            assert arg not in title_list, f"Добавленный товар: {arg} не отображается в корзине!"
