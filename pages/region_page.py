import allure
from pages.heager_page import HeaderPage
from elements.base_elements import *
from locators.locs_header_page import HeaderPageLocators
from locators.locs_region_page import RegionPageLocators


class RegionPage(HeaderPage):

    def __init__(self, browser, url, timeout=10):
        super().__init__(browser, url, timeout)
