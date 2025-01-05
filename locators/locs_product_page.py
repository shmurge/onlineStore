from selenium.webdriver.common.by import By


class ProductPageLocators:
    PRODUCT_TITLE = (By.XPATH, '//*[@class="product__title-heading-h1"]')
    PRODUCT_PRICE = (By.XPATH, '//*[@class="product__main-price"]/child::div[@class="price"]')
    BUY_BUTTON = (By.XPATH, '//*[contains(@class, "main-buy-btn js-product")]')
    GO_TO_CART_BUTTON = (By.XPATH, '//*[@class="btn btn--green btn--green-glow product__main-buy-btn"]')

    # модалка подтверждения покупки (не отображается в firefox)
    PRODUCT_ADDED_MODAL = (By.XPATH, '//*[@class="p-cart fancybox-content"]')
    PRODUCT_ADDED_MODAL_PLACE_AN_ORDER_BUTTON = (By.XPATH, '//*[@class="btn main__btn"]')
    PRODUCT_ADDED_MODAL_CONTINUE_SHOPPING_BUTTON = (By.XPATH, '//*[@class="main__continue"]')
