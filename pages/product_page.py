import allure
from selenium.webdriver.common.action_chains import ActionChains as AC
from locators.locs_region_page import RegionPageLocators
from elements.base_elements import *
from locators.locs_header_page import HeaderPageLocators
from locators.locs_login_page import LoginPageLocators
from locators.locs_profile_page import ProfilePageLocators
from locators.locs_product_page import ProductPageLocators
from pages.header_page import HeaderPage
from utils.data import *


class ProductPage(HeaderPage):

    def __init__(self, browser, url, timeout=10):
        super().__init__(browser, url, timeout)

        self.buy_button = Button(self.browser, "Кнопка Купить", *ProductPageLocators.BUY_BUTTON)
        self.go_to_cart_button = Button(self.browser, "Кнопка Перейти в корзину",
                                        *ProductPageLocators.GO_TO_CART_BUTTON)

    def should_be_correct_product_title_on_prod_page(self, exp_res):
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
        with allure.step(f"Добавить в корзину товар: {title}"):
            self.scroll_to_element(*ProductPageLocators.BUY_BUTTON, title)
            self.buy_button.click()

    def go_to_cart(self):
        with allure.step("Перейти в корзину"):
            self.go_to_cart_button.click()

    def check_buy_button_text(self, exp_res):
        self.buy_button.check_button_text(exp_res)

    def check_go_to_cart_button_text(self, exp_res):
        self.go_to_cart_button.check_button_text(exp_res)
