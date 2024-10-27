from selenium.webdriver.common.by import By


class ProfilePageLocators:
    PROFILE_CARD = (By.XPATH, '//*[@class="pa__menu"]')
    USER_NAME = (By.XPATH, '//*[@class="pa__user-name"]')
    USER_EMAIL = (By.XPATH, '//*[@class="pa-user__email"]')
    LOGOUT_BUTTON = (By.XPATH, '//*[@href="/logout"]')
