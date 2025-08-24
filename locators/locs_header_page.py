from selenium.webdriver.common.by import By


class HeaderPageLocators:
    QUKE_LOGO = (By.XPATH, '//*[@class="h-logo__img h-logo-decor"]')

    LOGIN_LINK = (By.XPATH, '//*[@class="h-user__text"]')
    USER_LINK = (By.XPATH, '//*[@class="h-user__link"]')

    REGION_NAME_IN_HEADER = (By.XPATH, '//*[@class="h-region__city"]')
    CHOOSE_REGION_BUTTON = (By.XPATH, '//*[@class="h-region__link js-region"]')

    CART_BUTTON = (By.XPATH, '//*[@class="header__basket"]')
    CART_ORDER_COUNTER = (By.XPATH, '//*[@class="h-basket__counter"]')
    CART_ORDER_PRICE = (By.XPATH, '//*[@class="h-basket__value"]')
    CART_VALUE_EMPTY = (By.XPATH, '//*[@class="h-basket__empty"]')

    MAIN_SEARCH_INPUT = (By.XPATH, '//*[@id="main-search-input"]')
    MAIN_SEARCH_AUTOCOMPLETE_INPUT = (By.XPATH, '//*[@id="autocomplete-v2-search"]')
    SEARCH_BUTTON_IN_MAIN_SEARCH_INPUT = (By.XPATH, '//*[@class="h-search__btn"]')

    CATALOGUE_BUTTON = (By.XPATH, '//*[contains(@class, "main-nav-v2__catalog--desc")]')
    CATALOGUE_CLOSE_BUTTON = (By.XPATH, '//*[contains(@class, "__toggle-cross")]')
    CATALOGUE_MODAL = (By.XPATH, '//*[@class="cat-nav__inner"]')
    CATALOGUE_LEFT_SIDEBAR = (By.XPATH, '//*[@class="cat-nav__list"]')
    CATALOGUE_LEFT_SIDEBAR_ITEMS = (By.XPATH, '//*[@class="cat-nav__list-link"]')
    CATALOGUE_RIGHT_SIDEBAR = (By.XPATH, '')
    CATALOGUE_SUB_CATEGORY_ATTRIBUTE = 'data-ga-value'
