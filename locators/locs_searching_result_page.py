from selenium.webdriver.common.by import By


class SearchingResultPageLocators:
    PRODUCT_CARD = (By.XPATH, '//*[@class="b-card__inner"]')
    PRODUCT_CARD_BUY_BUTTON = (By.XPATH, '//*[@class="b-card__buy add-to-cart"]')
    PRODUCT_CARD_PRODUCT_TITLE = (By.XPATH, '//*[@class="b-card__name"]')
    PRODUCT_CARD_PRICE = (By.XPATH, '//*[@class="b-card__price"]')