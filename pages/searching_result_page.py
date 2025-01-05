import allure
from random import *
from selenium.webdriver.common.action_chains import ActionChains as AC
from elements.base_elements import *
from pages.header_page import HeaderPage
from locators.locs_searching_result_page import SearchingResultPageLocators
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
        with allure.step("Выбор произвольной карточки товара со статусом 'В наличии' на странице с результатом поиска"):
            self.is_element_visible(*SearchingResultPageLocators.PRODUCT_CARD)
            prod_card, index = self.get_random_product_card_with_in_stock_status()
            elem_title = self.browser.find_element(*SearchingResultPageLocators.construction_title_locator(index))
            text_title = elem_title.text.strip()
            prod_price = (
                self.browser.find_element(*SearchingResultPageLocators.construction_price_locator(index)).text.strip())
            prod_price = f"{SearchingResultPageLocators.PRICE_PREFIX} {prod_price}"
            self.scroll_to_element(elem_title, text_title)
            with allure.step(f"Клик по карточке товара: {text_title}"):
                if elem_title.is_displayed():
                    elem_title.click()
            return text_title, prod_price

    def get_random_product_card_with_in_stock_status(self):
        prod_cards_list = self.browser.find_elements(*SearchingResultPageLocators.PRODUCT_CARD)
        assert len(prod_cards_list) != 0, \
            "На странице с результатом поиска нет ни одного товара со статусом 'В наличии'"
        prod_card = choice(prod_cards_list)
        index = prod_card.get_attribute('data-index')
        return prod_card, index
