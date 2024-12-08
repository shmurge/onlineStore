import allure
from selenium.webdriver.common.action_chains import ActionChains as AC
from locators.locs_region_page import RegionPageLocators
from elements.base_elements import *
from locators.locs_header_page import HeaderPageLocators
from locators.locs_login_page import LoginPageLocators
from locators.locs_profile_page import ProfilePageLocators
from locators.locs_product_page import ProductPageLocators
from locators.locs_product_added_modal_page import ProductAddedModalLocators
from pages.header_page import HeaderPage
from utils.data import *


class ProductAddedModal(HeaderPage):

    def __init__(self, browser, url, timeout=10):
        super().__init__(browser, url, timeout)

        self.place_an_order_button = Button(self.browser, "Кнопка Оформить заказ",
                                            *ProductAddedModalLocators.PRODUCT_ADDED_MODAL_PLACE_AN_ORDER_BUTTON)
        self.continue_shopping_button = Button(self.browser, "Кнопка Продолжить покупки",
                                               *ProductAddedModalLocators.PRODUCT_ADDED_MODAL_CONTINUE_SHOPPING_BUTTON)

    def should_be_buy_options_modal(self):
        with allure.step('Проверка наличия модалки "Товар добавлен в корзину"'):
            assert self.is_element_visible(*ProductAddedModalLocators.PRODUCT_ADDED_MODAL), \
                'Модалка "Товар добавлен в корзину" не отображается!'

    def place_an_order(self):
        sleep(0.5)
        with allure.step("Перейти в корзину для оформления заказа"):
            self.place_an_order_button.click()

    def continue_shopping(self):
        with allure.step("Продолжить покупки"):
            self.continue_shopping_button.click()
