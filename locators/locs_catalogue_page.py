from selenium.webdriver.common.by import By


class CataloguePageLocators:

    # Карточка товара
    PRODUCT_CARD = (By.XPATH, '//*[@class="b-card2-v2__inner"]')
    PRODUCT_CARD_BUY_BUTTON = (By.XPATH, '//*[@class="b-card2-v2__buy add-to-cart"]')
    PRODUCT_CARD_PRODUCT_TITLE = (By.XPATH, '//*[@class="b-card2-v2__name"]')
    PRODUCT_CARD_PRICE = (By.XPATH, '//*[@class="b-card2-v2__price"]')
