import allure
from pages.base_page import BasePage
from elements.base_elements import *
from locators.locs_main_page import MainPageLocators



class RegionPage(BasePage):

    def __init__(self, browser, url, timeout=10):
        super().__init__(browser, url, timeout)

        self.choose_region_button = Button(self.browser, "Выбрать регион", *MainPageLocators.CHOOSE_REGION_BUTTON)

    def open_region_modal(self):
        with allure.step("Открыть модалку выбора региона"):
            self.choose_region_button.click()
        with allure.step("Проверить отображение модалки выбора региона"):
            assert self.is_element_visible(*MainPageLocators.CHOOSE_REGION_MODAL), \
                'Не отображается модалка выбора региона!'

    def choose_region(self, name):
        with allure.step(f"Выбрать регион: {name}"):
            region = self.search_element_by_text(name)
            region.click()

    def should_be_correct_region_in_header(self, exp_res):
        with (allure.step("Проверка корректности выбранного региона")):
            self.is_element_visible(*MainPageLocators.REGION_NAME_IN_HEADER)
            act_res = self.browser.find_element(*MainPageLocators.REGION_NAME_IN_HEADER).text
            assert act_res in exp_res, \
                f'В хэдере отображается некорректный регион ОР: {exp_res} ФР: {act_res}'