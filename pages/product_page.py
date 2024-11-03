import allure
from selenium.webdriver.common.action_chains import ActionChains as AC
from locators.locs_region_page import RegionPageLocators
from elements.base_elements import *
from locators.locs_header_page import HeaderPageLocators
from locators.locs_login_page import LoginPageLocators
from locators.locs_profile_page import ProfilePageLocators
from locators.locs_product_page import ProductPageLocators
from pages.heager_page import HeaderPage
from utils.data import *


class ProductPage(HeaderPage):

    def __init__(self, browser, url, timeout=10):
        super().__init__(browser, url, timeout)

    def check_searching_result(self, exp_res):
        with allure.step("Проверка результатов поиска"):
            self.check_searching_result_header(exp_res)
            self.check_product_list(exp_res)

    def check_searching_result_header(self, exp_res):
        with allure.step(f"Проверка наличия подстроки: {exp_res} в хедере результатов поиска"):
            act_res = self.browser.find_element(*ProductPageLocators.SEARCHING_RESULT_HEADER).text
            assert exp_res.lower() in act_res.lower(), (f"Некорректный результат поиска в хедере! Хедер: {act_res} "
                                                        f"не содержит подстроки {exp_res}")

    def check_product_list(self, exp_res):
        with allure.step(f"Проверка результатов поиска товара: {exp_res}"):
            product_list = self.browser.find_elements(*ProductPageLocators.PRODUCT_TITLE)
            for el in product_list:
                assert exp_res.lower() in el.text.lower(), (f"Некорректный результат поиска в списке товаров! "
                                                            f"Товар: {el.text} не содержит подстроки: {exp_res}")
