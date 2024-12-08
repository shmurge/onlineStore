from selenium.webdriver.common.by import By


class ProductPageLocators:
    PRODUCT_TITLE = (By.XPATH, '//*[@class="product__title-heading-h1"]')
    PRODUCT_PRICE = (By.XPATH, '//*[@class="product__main-price"]/child::div[@class="price"]')
    # NOT_CURRENT_PRICE = (By.XPATH, '//*[@class="price price--grey"]')
    # STATUS_NOT_IN_STOCK = (By.XPATH, '//*[@class="status__text status__not-in-stock"]')
    BUY_BUTTON = (By.XPATH, '//*[contains(@class, "main-buy-btn js-product")]')
    GO_TO_CART_BUTTON = (By.XPATH, '//*[@class="btn btn--green btn--green-glow product__main-buy-btn"]')
