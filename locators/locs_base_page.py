from selenium.webdriver.common.by import By


class BasePageLocators:
    COOKIE_ALERT = (By.XPATH, '//*[@class="cookie-policy js-cookie-policy active"]')
    COOKIE_ALERT_APPLY_BUTTON = (By.XPATH, '//*[@class="button js-cookie-accept"]')
