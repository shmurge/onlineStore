import allure
from selenium.webdriver.common.action_chains import ActionChains as AC
from locators.locs_product_page import ProductPageLocators
from pages.header_page import HeaderPage
from elements.base_elements import *
from time import sleep
from utils.data import *


class ProductPage(HeaderPage):

    def __init__(self, browser, url, timeout=10):
        super().__init__(browser, url, timeout)

        self.buy_button = Button(self.browser, "Кнопка Купить", *ProductPageLocators.BUY_BUTTON)
        self.go_to_cart_button = Button(self.browser, "Кнопка Перейти в корзину",
                                        *ProductPageLocators.GO_TO_CART_BUTTON)
        self.place_an_order_button = Button(self.browser, "Кнопка Оформить заказ",
                                            *ProductPageLocators.PRODUCT_ADDED_MODAL_PLACE_AN_ORDER_BUTTON)

    def should_be_correct_product_title_on_prod_page(self, exp_res):
        self.is_element_visible(*ProductPageLocators.PRODUCT_TITLE)
        with allure.step("Сравнение наименования товара в карточке и на странице товара"):
            act_res = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text.strip()
            assert exp_res.lower() in act_res.lower(), (f"Некорректное наименование товара!"
                                                        f"В карточке: {exp_res}, на странице товара: {act_res}")

    def should_be_correct_product_price_on_prod_page(self, exp_res):
        with allure.step("Сравнение стоимости товара в карточке и на странице товара"):
            act_res = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text.strip()
            assert act_res.lower() in exp_res.lower(), (f"Некорректная стоимость товара!"
                                                        f"В карточке: {exp_res}, на странице товара: {act_res}")

    def get_title_and_price(self):
        prod_title = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text
        prod_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        return prod_title, prod_price

    def add_to_cart(self, title):
        with allure.step(f"Добавить в корзину товар: {title} и перейти в корзину"):
            self.buy_button.click()
            try:
                self.browser.implicitly_wait(1)
                sleep(0.5) # sleep добавлен из-за особенности работы модального окна
                self.place_an_order_button.click()
            except:
                pass

    def go_to_cart(self):
        with allure.step("Перейти в корзину"):
            self.scroll_to_element(self.go_to_cart_button, self.go_to_cart_button.name)
            self.go_to_cart_button.click()
