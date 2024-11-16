import allure
from random import *
from selenium.webdriver.common.action_chains import ActionChains as AC
from elements.base_elements import *
from pages.header_page import HeaderPage
from locators.locs_region_page import RegionPageLocators
from locators.locs_header_page import HeaderPageLocators
from locators.locs_login_page import LoginPageLocators
from locators.locs_profile_page import ProfilePageLocators
from locators.locs_product_page import ProductPageLocators
from locators.locs_searching_result_page import SearchingResultPageLocators
from locators.locs_catalogue_page import CataloguePageLocators
from utils.data import *


class SearchingResultPage(HeaderPage):

    def __init__(self, browser, url, timeout=10):
        super().__init__(browser, url, timeout)

    def check_searching_result(self, exp_res):
        with allure.step(f"Проверка результатов поиска товара: {exp_res}"):
            product_list = self.browser.find_elements(*SearchingResultPageLocators.PRODUCT_CARD_PRODUCT_TITLE)
            for el in product_list:
                assert exp_res.lower() in el.text.lower(), (f"Некорректный результат поиска в списке товаров! "
                                                            f"Товар: {el.text} не содержит подстроки: {exp_res}")

    def select_random_product_card(self):
        prod_card = self.get_random_product_card_with_in_stock_status()
        prod_title = self.get_product_title(prod_card)
        prod_price = self.get_product_price(prod_card)
        self.scroll_to_card(prod_card, prod_title)
        sleep(3)
        with allure.step(f"Клик по карточке товара: {prod_title}"):
            prod_card.click()
        return prod_title, prod_price

    def get_random_product_card_with_in_stock_status(self):
        with allure.step("Выбор произвольной карточки товара со статусом 'В наличии'"):
            self.is_element_visible(*SearchingResultPageLocators.PRODUCT_CARD)
            prod_cards_list = self.browser.find_elements(*SearchingResultPageLocators.PRODUCT_CARD)
            flag = True
            count = 0
            while flag:
                prod_card = choice(prod_cards_list)
                info_list_in_prod_card = self.get_info_from_prod_card(prod_card)
                for info in info_list_in_prod_card:
                    if info.lower() == "купить":
                        flag = False
                        break
                count += 1
                if count == 100:
                    flag = False
            return prod_card

    @staticmethod
    def get_info_from_prod_card(element):
        info_list = element.text.split("\n")
        return info_list

    def get_product_title(self, element):
        title = self.get_info_from_prod_card(element)[1]
        return title.strip()

    def get_product_price(self, element): # актуальная цена товара
        prod_info = self.get_info_from_prod_card(element)
        price = f"Цена {prod_info[4]}"
        return price.strip()

    def scroll_to_card(self, card, name):
        self.is_element_visible(*SearchingResultPageLocators.PRODUCT_CARD)
        with allure.step(f"Проскроллить до товара: {name}"):
            action = AC(self.browser)
            action.scroll_to_element(card)
            action.perform()