from selenium.webdriver.common.by import By


class CartPageLocators:
    CART_PATH_PARAM = "order"
    CART = (By.XPATH, '//*[@class="order-basket"]')
    EMPTY_CART_MESSAGE = (By.XPATH, '//*[@class="order-basket__empty-img"]')

    PROD_CARD = (By.XPATH, '//*[@class="order-basket__item-content"]')
    PROD_QUANTITY = (By.XPATH, '//*[@data-quantity="1"]')
    PROD_NAME = (By.XPATH, '//*[@class="order-basket__item-name"]')
    PROD_PRICE = (By.XPATH, 'class="order-basket__item-price clearfix"')