from os.path import split

import allure
from selenium.webdriver.common.action_chains import ActionChains as AC
from locators.locs_region_page import RegionPageLocators
from elements.base_elements import *
from locators.locs_header_page import HeaderPageLocators
from locators.locs_login_page import LoginPageLocators
from locators.locs_profile_page import ProfilePageLocators
from locators.locs_product_page import ProductPageLocators
from locators.locs_catalogue_page import CataloguePageLocators
from pages.header_page import HeaderPage
from utils.data import *


class CataloguePage(HeaderPage):

    def __init__(self, browser, url, timeout=10):
        super().__init__(browser, url, timeout)

    def check_searching_result(self, exp_res):
        with allure.step(f"Проверка результатов поиска товара: {exp_res}"):
            product_list = self.browser.find_elements(*CataloguePageLocators.PRODUCT_CARD_PRODUCT_TITLE)
            for el in product_list:
                assert exp_res.lower() in el.text.lower(), (f"Некорректный результат поиска в списке товаров! "
                                                            f"Товар: {el.text} не содержит подстроки: {exp_res}")

    def get_product_card(self, index):
        product_cards_list = self.browser.find_elements(*CataloguePageLocators.PRODUCT_CARD)
        card_1 = product_cards_list[index]
        price = self.get_product_price(card_1)
        print()
        print(price)

    def get_product_price(self, locator):
        price_data_list = self.get_price_data(locator)
        price = None
        if len(price_data_list) == 1:
            price = f"Цена {price_data_list[0]}"
        elif len(price_data_list) == 4:
            price = price_data_list[1][:-1]
        return price

    def get_price_data(self, locator):
        try:
            price = locator.find_element(*CataloguePageLocators.PRODUCT_CARD_PRICE).text
            price = price.split("\n")
        except NoSuchElementException:
            return None
        return price
