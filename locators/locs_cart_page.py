from selenium.webdriver.common.by import By


class CartPageLocators:
    CART_PATH_PARAM = "order"
    CART = (By.XPATH, '//*[@class="order-basket"]')
    EMPTY_CART_MESSAGE = (By.XPATH, '//*[@class="order-basket__empty-img"]')