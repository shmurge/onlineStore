from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FRAME = (By.XPATH, '//*[@class="auth fancybox-content"]')
    LOGIN_INPUT = (By.XPATH, '//*[@id="auth-email"]')
    PASSWORD_INPUT = (By.XPATH, '//*[@id="auth-pass"]')
    SIGN_IN_BUTTON = (By.XPATH, '//*[@type="submit" and contains(text(), "Войти")]')
    LOGIN_INPUT_VALIDATION_MESSAGE = (By.XPATH, '//*[@id="auth-email-error"]')
    PASSWORD_INPUT_VALIDATION_MESSAGE = (By.XPATH, '//*[@id="auth-pass-error"]')
