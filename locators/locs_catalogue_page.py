from selenium.webdriver.common.by import By


class CataloguePageLocators:

    # Карточка товара
    PRODUCT_CARD = (By.XPATH, '//*[@class="b-card2-v2  js-product-item"]')
    PRODUCT_CARD_BUY_BUTTON = (By.XPATH, '//*[@class="b-card2-v2__buy add-to-cart"]')
    PRODUCT_CARD_PRODUCT_TITLE = (By.XPATH, '//*[@class="b-card2-v2__name"]')
    PRODUCT_CARD_PRICE = (By.XPATH, '//*[@class="b-card2-v2__price"]')
    PRODUCT_CARD_NOT_IN_STOCK = (By.XPATH, 'class="b-card2-v2 b-card2-v2--nonactive js-product-item"')

    @staticmethod
    def construction_title_locator(index):
        return (By.XPATH, f'//*[@data-index={index}]/descendant::a[@class="b-card2-v2__name"]')

    @staticmethod
    def construction_price_locator(index):
        return (By.XPATH, f'//*[@data-index={index}]/descendant::div[@class="b-card2-v2__price"]')

