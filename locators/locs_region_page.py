from selenium.webdriver.common.by import By


class RegionPageLocators:
    CHOOSE_REGION_MODAL = (By.XPATH, '//*[@class="region2 fancybox-content"]')
    REGION_CONTENT = (By.XPATH, 'class="region2__body-content"')
    SEARCH_INPUT_IN_REGION_MODAL = (By.XPATH, '//*[@class="region2__form-input"]')
    SEARCH_BUTTON_IN_REGION_MODAL = (By.XPATH, '//*[@class="region2__form-btn"]')
    CLOSE_BUTTON_CHOOSE_REGION_MODAL = (By.XPATH, '//*[@class="region2__close js-region2-close"]')
