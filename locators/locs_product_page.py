from selenium.webdriver.common.by import By


class ProductPageLocators:
    SEARCHING_RESULT_HEADER = (By.XPATH, '//*[contains(@class, "b-title__heading")]')
    PRODUCT_TITLE = (By.XPATH, '//*[contains(@class, "b-card") and contains(@class, "__name")]')