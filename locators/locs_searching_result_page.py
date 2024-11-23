from selenium.webdriver.common.by import By


class SearchingResultPageLocators:
    PRODUCT_CARD = (By.XPATH, '//*[@class="b-card b-card--discount "]')
    PRODUCT_CARD_BUY_BUTTON = (By.XPATH, '//*[@class="b-card__buy add-to-cart"]')
    PRODUCT_CARD_PRODUCT_TITLE = (By.XPATH, '//*[@class="b-card__name"]')
    PRODUCT_CARD_PRICE = (By.XPATH, '//*[@class="b-card__price"]')
    PRODUCT_CARD_NOT_IN_STOCK = (By.XPATH, '//*[contains(@class, "--not-available")]')

    @staticmethod
    def construction_title_locator(index):
        return (By.XPATH, f'//*[@data-index={index}]/descendant::a[@class="b-card__name"]')

    @staticmethod
    def construction_price_locator(index):
        return (By.XPATH, f'//*[@data-index={index}]/descendant::div[@class="b-card__price"]')

    # динамические локаторы для стягивания наименования и цены
    # //*[@data-index={N}]/descendant::a[@class="b-card__name"]
    # //*[@data-index={N}]/descendant::div[@class="b-card__price"]