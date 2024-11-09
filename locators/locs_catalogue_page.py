from selenium.webdriver.common.by import By


class CataloguePageLocators:
    SEARCHING_RESULT_HEADER = (By.XPATH, '//*[contains(@class, "b-title__heading")]')

    # Карточка товара
    PRODUCT_CARD = (By.XPATH, '//*[@data-index]')
    PRODUCT_CARD_ADD_TO_CART_BUTTON = (By.XPATH, '//*[contains(@class, "add-to-cart")]')
    PRODUCT_CARD_PRODUCT_TITLE = (By.XPATH, '//*[contains(@class, "b-card") and contains(@class, "__name")]')
    PRODUCT_CARD_PRICE = (By.XPATH, '//*[contains(@class, "__price")]')
    # PRODUCT_CARD_PRICE_VER_1 = (By.XPATH, '//*[@class="b-card__price"]')
    # PRODUCT_CARD_PRICE_VER_2 = (By.XPATH, '//*[@class="b-card2-v2__price"]')
