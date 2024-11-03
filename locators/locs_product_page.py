from selenium.webdriver.common.by import By


class ProductPageLocators:
    SEARCHING_RESULT_HEADER = (By.XPATH, '//*[contains(@class, "b-title__heading")]')
    PRODUCT_TITLE = (By.XPATH, '//*[@class="b-card2-v2__name"]')