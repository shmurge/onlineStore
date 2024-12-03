import allure
from random import *
from re import *
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
        title_list = [elem.text for elem in self.browser.find_elements(*CartPageLocators.PROD_TITLE)]
        for arg in args:
            assert arg in title_list, (f"Добавленный товар: {arg} не отображается в корзине! "
                                       f"Список товаров в корзине: {title_list}")

    # Подсчет стоимости каждой позиции в корзине и сравнение с итоговой стоимостью корзины
    def check_quantity_and_price_positions_in_cart(self):
        price_list = [elem.text.replace(" ", "") for elem in self.browser.find_elements(*CartPageLocators.PROD_PRICE)]
        summ = 0
        total_cart_sum = self.get_total_cart_price()
        with allure.step("Проверить стоимость всех товаров в корзине"):
            for p in price_list:
                quantity, price, total_price = self.get_quantity_price_total_price_of_product(p)
                assert quantity * price == total_price, (f"Некорректная стоимость: {p}!"
                                                         f"ОР: {total_price}, ФР: {quantity * price}")
                summ += total_price
        with allure.step("Проверить итоговую стоимость корзины"):
            assert summ == total_cart_sum, f"Некорректная стоимость корзины! ОР: {summ}, ФР: {total_cart_sum}"

    @staticmethod
    def get_quantity_price_total_price_of_product(string):  # Парсит стоимость из строки и возвращает целые числа
        numbers = findall(r'\d+', string)
        parsed_numbers = [int(num.replace(' ', '')) for num in numbers]
        quantity, price, total_price = parsed_numbers
        return quantity, price, total_price

    def get_total_cart_price(self):  # Преобразовывает строковое значение в целочисленное и возвращает его
        total_cart_price = self.browser.find_element(*CartPageLocators.CART_TOTAL_PRICE).text.replace(" ", "")
        if total_cart_price.isdigit():
            return int(total_cart_price)
        return None
