from selenium.webdriver.common.by import By


class ProductAddedModalLocators:
    PRODUCT_ADDED_MODAL = (By.XPATH, '//*[@class="p-cart fancybox-content"]')
    PRODUCT_ADDED_MODAL_PLACE_AN_ORDER_BUTTON = (By.XPATH, '//*[@class="btn main__btn"]')
    PRODUCT_ADDED_MODAL_CONTINUE_SHOPPING_BUTTON = (By.XPATH, '//*[@class="main__continue"]')
