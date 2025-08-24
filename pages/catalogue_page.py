from random import *
from elements.elements import *
from locators.locs_catalogue_page import CataloguePageLocators
from pages.header_page import HeaderPage
from src.data.data import *


class CataloguePage(HeaderPage):

    def __init__(self, browser, url):
        super().__init__(browser, url)

    def check_searching_result(self, exp_res):
        with allure.step(f"Проверка результатов поиска товара: {exp_res}"):
            product_list = self.get_elements_list(*CataloguePageLocators.PRODUCT_CARD_PRODUCT_TITLE)
            for el in product_list:
                assert exp_res.lower() in el.text.lower(), (f"Некорректный результат поиска в списке товаров! "
                                                            f"Товар: {el.text} не содержит подстроки: {exp_res}")

    def select_random_product_card(self):
        with allure.step("Выбор произвольной карточки товара со статусом 'В наличии'"):
            prod_card, index = self.get_random_product_card_with_in_stock_status()
            elem_title = self.get_element(*CataloguePageLocators.construction_title_locator(index))
            text_title = elem_title.text.strip()
            # парсим цену без точки в конце
            prod_price = self.get_element(*CataloguePageLocators.construction_price_locator(index)).text.strip()[:-1]
            self.scroll_to_element(elem_title, text_title)
            with allure.step(f"Клик по карточке товара: {text_title}"):
                if elem_title.is_displayed():
                    prod_card.click()
            return text_title, prod_price

    def get_random_product_card_with_in_stock_status(self):
        prod_cards_list = self.get_elements_list(*CataloguePageLocators.PRODUCT_CARD)
        assert len(prod_cards_list) != 0, "На странице каталога нет ни одного товара со статусом 'В наличии'"
        prod_card = choice(prod_cards_list)
        index = prod_card.get_attribute('data-index')
        return prod_card, index

    @staticmethod
    def get_type_link_and_title_from_prod_catalogue():
        item_type = choice(list(Catalogue.CATALOGUE))
        item = choice(Catalogue.CATALOGUE[item_type])
        item_link = item[0]
        item_title = item[1]
        return item_type, item_link, item_title
