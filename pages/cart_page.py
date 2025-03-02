from random import *
from re import *
from pages.header_page import HeaderPage
from elements.base_elements import *
from locators.locs_header_page import HeaderPageLocators
from locators.locs_cart_page import CartPageLocators
from utils.api_features import PrepareData


class CartPage(HeaderPage):

    def __init__(self, browser, url):
        super().__init__(browser, url)

    def should_be_cart_page(self):
        with allure.step("Проверить отображение страницы корзины"):
            self.should_be_correct_url(CartPageLocators.CART_PATH_PARAM)
            assert self.is_element_visible(*CartPageLocators.CART), "Не отображается страница корзины!"

    def should_be_message_empty_cart(self):
        with allure.step("Проверить отображение сообщения о пустой корзине"):
            message = self.get_element(*CartPageLocators.EMPTY_CART_MESSAGE).is_displayed()
            assert message, "Не отображается сообщение 'Корзина пуста'!"

    def check_product_position_in_cart(self, *args):
        with allure.step("Проверка списка товаров в корзине"):
            title_list = [elem.text.strip() for elem in self.get_elements_list(*CartPageLocators.PROD_TITLE)]
            for arg in args:
                assert arg in title_list, (f"Добавленный товар: {arg} не отображается в корзине! "
                                           f"Список товаров в корзине: {title_list}")

    def should_not_be_position_in_cart(self, title):
        with allure.step("Проверка: товар отсутствует в корзине"):
            title_list = [elem.text.strip() for elem in self.get_elements_list(*CartPageLocators.PROD_TITLE)]
            assert title not in title_list, (f"Позиция: {title} отображается в корзине, но должна быть удалена! "
                                             f"Содержимое корзины: {title_list}")

    # Подсчет стоимости каждой позиции в корзине и сравнение с итоговой стоимостью корзины
    def check_quantity_and_price_positions_in_cart(self):
        with allure.step("Проверить стоимость всех товаров в корзине"):
            price_list = [elem.text.replace(" ", "") for elem in self.get_elements_list(*CartPageLocators.PROD_PRICE)]
            summ = 0
            total_cart_sum = self.get_total_cart_price()
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

    # def get_total_cart_price(self):  # Преобразовывает строковое значение в целочисленное и возвращает его
    #     self.is_element_visible(*CartPageLocators.CART_TOTAL_PRICE)
    #     total_cart_price = self.browser.find_element(*CartPageLocators.CART_TOTAL_PRICE).text.replace(" ", "")
    #     if total_cart_price.isdigit():
    #         return int(total_cart_price)
    #     return None

    def get_total_cart_price(self):  # Преобразовывает строковое значение в целочисленное и возвращает его
        self.is_element_visible(*CartPageLocators.CART_TOTAL_PRICE)
        total_cart_price = self.get_element(*CartPageLocators.CART_TOTAL_PRICE).text.replace(" ", "")
        if total_cart_price.isdigit():
            return int(total_cart_price)
        return None

    def check_total_price_in_cart_and_in_header(self):
        with allure.step("Проверить общую стоимость корзины и стоимость в заголовке"):
            total_cart_price = self.get_element(*CartPageLocators.CART_TOTAL_PRICE).text
            price_in_header = self.get_element(*HeaderPageLocators.CART_ORDER_PRICE).text
            assert total_cart_price == price_in_header, (f"Несоответствие стоимости в корзине и в хэдере!"
                                                         f"В корзине: {total_cart_price}, в хэдере: {price_in_header}")

    def get_position_id_and_title(self):
        id_list = [elem.get_attribute('data-id') for elem in
                   self.get_elements_list(*CartPageLocators.PROD_QUANTITY)]
        title_list = [elem.text.strip() for elem in self.get_elements_list(*CartPageLocators.PROD_TITLE)]
        prod_dict = {id_list[i]: title_list[i] for i in range(len(id_list))}
        return prod_dict

    def remove_random_position_from_cart(self):
        id_and_title = self.get_position_id_and_title()
        rand_id = choice(list(id_and_title.keys()))
        with allure.step(f"Удалить из корзины позицию {id_and_title[rand_id]}"):
            rm_button = self.get_element(*CartPageLocators.construction_delete_position_button(rand_id))
            self.scroll_to_element(rm_button, "Кнопка Удалить")
            rm_button.click()
            return id_and_title[rand_id]

    def precond_add_prods_to_cart(self, *prod_id):
        with allure.step(f"Предусловия: добавление товаров корзину через API"):
            self.is_element_visible(*HeaderPageLocators.CART_BUTTON)
            func = PrepareData()
            cookies = self.get_all_cookies()
            for id in prod_id:
                func.add_prod_to_cart(cookies, id)
