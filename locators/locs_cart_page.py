from selenium.webdriver.common.by import By


class CartPageLocators:
    CART_PATH_PARAM = "order"
    CART = (By.XPATH, '//*[@class="order-basket"]')
    EMPTY_CART_MESSAGE = (By.XPATH, '//*[@class="order-basket__empty-img"]')

    PROD_CARD = (By.XPATH, '//*[@class="order-basket__item-content"]')
    PROD_QUANTITY = (By.XPATH, '//*[@class="order-basket__quantity"]')
    PROD_TITLE = (By.XPATH, '//*[@class="order-basket__item-name"]')
    PROD_PRICE = (By.XPATH, '//*[@class="order-basket__item-price clearfix"]')
    CART_TOTAL_PRICE = (By.XPATH, '//*[@id="cartTotalSum"]')

    @staticmethod
    def construction_delete_position_button(pos_id):
        return (By.XPATH, f'//*[@data-id={pos_id} and contains(@class, "remove-from-cart")]')
