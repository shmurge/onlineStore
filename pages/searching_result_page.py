import allure
from random import *
from selenium.webdriver.common.action_chains import ActionChains as AC
from locators.locs_region_page import RegionPageLocators
from elements.base_elements import *
from locators.locs_header_page import HeaderPageLocators
from locators.locs_login_page import LoginPageLocators
from locators.locs_profile_page import ProfilePageLocators
from locators.locs_product_page import ProductPageLocators
from locators.locs_catalogue_page import CataloguePageLocators
from pages.header_page import HeaderPage
from utils.data import *


class SearchingResultPage(HeaderPage):

    def __init__(self, browser, url, timeout=10):
        super().__init__(browser, url, timeout)


