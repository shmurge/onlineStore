from selenium.webdriver.common.by import By


class CataloguePageLocators:
    CATALOGUE_CLOSE_BUTTON = (By.XPATH, '//*[contains(@class, "__toggle-cross")]')
    CATALOGUE_MODAL = (By.XPATH, '//*[@class="cat-nav__inner"]')
