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

    def should_be_correct_product_title_on_prod_page(self, exp_res):
        with allure.step("Сравнение наименования товара в карточке и на странице товара"):
            act_res = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text
            assert exp_res in act_res, (f"Некорректное наименование товара!"
                                        f"В карточке: {exp_res}, на странице товара: {act_res}")

    def should_be_correct_product_price_on_prod_page(self, exp_res):
        with allure.step("Сравнение стоимости товара в карточке и на странице товара"):
            act_res = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
            assert act_res in exp_res, (f"Некорректная стоимость товара!"
                                        f"В карточке: {exp_res}, на странице товара: {act_res}")

