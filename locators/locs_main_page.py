from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.XPATH, '//*[@class="h-user__text"]')
    USER_LINK = (By.XPATH, '//*[@class="h-user__link"]')

    REGION_NAME_IN_HEADER = (By.XPATH, '//*[@class="h-region__city"]')
    CHOOSE_REGION_BUTTON = (By.XPATH, '//*[@class="h-region__link js-region"]')
    CHOOSE_REGION_MODAL = (By.XPATH, '//*[@class="region2 fancybox-content"]')
    REGION_CONTENT = (By.XPATH, 'class="region2__body-content"')
    SEARCH_INPUT_IN_REGION_MODAL = (By.XPATH, '//*[@class="region2__form-input"]')
    SEARCH_BUTTON_IN_REGION_MODAL = (By.XPATH, '//*[@class="region2__form-btn"]')
    CLOSE_BUTTON_CHOOSE_REGION_MODAL = (By.XPATH, '//*[@class="region2__close js-region2-close"]')

    QUKE_LOGO = (By.XPATH, '//*[@class="h-logo__img"]')

    BASKET_BUTTON = (By.XPATH, '//*[@class="header__basket"]')
    BASKET_ORDER_COUNTER = (By.XPATH, '//*[@class="h-basket__counter"]')
    BASKET_ORDER_PRICE = (By.XPATH, '//*[@class="h-basket__value"]')
    BASKET_VALUE_EMPTY = (By.XPATH, '//*[@class="h-basket__empty"]')

    MAIN_SEARCH_INPUT = (By.XPATH, '//*[@id="main-search-input"]')
    SEARCH_BUTTON_IN_MAIN_SEARCH_INPUT = (By.XPATH, '//*[@class="h-search__btn"]')

    CATALOGUE_BUTTON = (By.XPATH, '//*[@class="main-nav-v2__toggle"]')
    CATALOGUE_CLOSE_BUTTON = (By.XPATH, '//*[contains(@class, "__toggle-cross")]')
    CATALOGUE_MODAL = (By.XPATH, '//*[@class="cat-nav__inner"]')