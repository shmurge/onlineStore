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
        with (allure.step(
            "Выбор произвольной карточки товара со статусом 'В наличии' на странице с результатом поиска")):
            prod_card, index = self.get_random_product_card_with_in_stock_status()
            prod_title = self.browser.find_element(*SearchingResultPageLocators.construction_title_locator(index))
            prod_price = (
                self.browser.find_element(*SearchingResultPageLocators.construction_price_locator(index)).text.strip())
            self.scroll_to_card(prod_card, prod_title.text.strip())
            with allure.step(f"Клик по карточке товара: {prod_title.text.strip()}"):
                self.waiting_element_clickable(prod_title)
                prod_title.click()
            return prod_title.text.strip(), f"Цена {prod_price}"

    def get_random_product_card_with_in_stock_status(self):
        self.is_element_visible(*SearchingResultPageLocators.PRODUCT_CARD)
        prod_cards_list = self.browser.find_elements(*SearchingResultPageLocators.PRODUCT_CARD)
        assert len(prod_cards_list) != 0, \
            "На странице с результатом поиска нет ни одного товара со статусом 'В наличии'"
        index = randrange(0, len(prod_cards_list))
        prod_card = prod_cards_list[index]
        return prod_card, index+1

    def scroll_to_card(self, card, name):
        self.is_element_visible(*SearchingResultPageLocators.PRODUCT_CARD)
        with allure.step(f"Проскроллить до товара: {name}"):
            action = AC(self.browser)
            action.scroll_to_element(card)
            action.perform()
