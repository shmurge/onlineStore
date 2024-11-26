from selenium.webdriver.common.by import By


class SearchingResultPageLocators:
    PRODUCT_CARD = (By.XPATH, '//*[@class="b-card b-card--discount "]')
    # PRODUCT_CARD_BUY_BUTTON = (By.XPATH, '//*[@class="b-card__buy add-to-cart"]')
    PRODUCT_CARD_PRODUCT_TITLE = (By.XPATH, '//*[@class="b-card__name"]')
    PRICE_PREFIX = "Цена"
    # PRODUCT_CARD_PRICE = (By.XPATH, '//*[@class="b-card__price"]')
    # PRODUCT_CARD_NOT_IN_STOCK = (By.XPATH, '//*[contains(@class, "--not-available")]')
    DROPDOWN_WITH_PRODUCTS = (By.XPATH, '//*[@class="s-res"]')

    @staticmethod
    def construction_title_locator(index):
        return (By.XPATH, f'//*[@data-index={index}]/descendant::a[@class="b-card__name"]')

    @staticmethod
    def construction_price_locator(index):
        return (By.XPATH, f'//*[@data-index={index}]/descendant::div[@class="b-card__price"]')

    @staticmethod
    def construction_add_to_cart_button(index):
        return (By.XPATH, f'//*[@data-index={index}]/descendant::a[@class="b-card__buy add-to-cart"]')

    @staticmethod
    def construction_current_prod_card_locator(index):
        return (By.XPATH, f'//*[@data-index={index}]')

