import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotVisibleException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains as AC
from elements.base_elements import Button
from locators.locs_base_page import BasePageLocators
from time import sleep


class BasePage:

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

        self.cookie_apply_button = Button(self.browser, "Кнопка: Принять куки",
                                          *BasePageLocators.COOKIE_ALERT_APPLY_BUTTON)

    def open(self, url):
        with allure.step(f'Открыть страницу {url}'):
            return self.browser.get(self.url)

    def refresh(self):
        with allure.step('Обновить страницу'):
            return self.browser.refresh()

    def go_back(self):
        """Возврат на предыдущую страницу, через кнопку в браузере!"""
        with allure.step('Вернуться на предыдущую страницу'):
            self.browser.back()

    def is_element_present(self, how, what):
        try:
            WebDriverWait(self.browser, 10, 0.5).until(EC.presence_of_element_located((how, what)))
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=1):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            self.browser.find_element(how, what)
            WebDriverWait(self.browser, timeout, 0.5).until_not(EC.presence_of_element_located((how, what)))
        except NoSuchElementException:
            return False
        return True

    def is_element_visible(self, how, what, timeout=10, freq=0.5):
        try:
            WebDriverWait(self.browser, timeout, freq).until(EC.visibility_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_not_element_visible(self, how, what, timeout=10, freq=0.5):
        try:
            WebDriverWait(self.browser, timeout, freq).until_not(EC.visibility_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def waiting_text_visibility(self, locator: tuple[str, str], text: str, timeout: float = 1.0):
        try:
            WebDriverWait(self.browser, timeout).until(EC.text_to_be_present_in_element(locator, text_=text))
        except TimeoutException:
            return False
        return True

    def waiting_element_clickable(self, locator: tuple[str, str], timeout: float = 5.0):
        try:
            WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            return False
        return True

    def waiting_attribute_in_element(self, locator: tuple[str, str], attribute: str, timeout: float = 1.0):
        try:
            WebDriverWait(self.browser, timeout).until(EC.element_attribute_to_include(locator, attribute))
        except TimeoutException:
            return False
        return True

    def search_element_by_text(self, text):
        with allure.step(f'Поиск элемента: {text}'):
            element = self.browser.find_element(By.XPATH, f"//*[text()='{text}']")
        return element

    def search_element_by_attribute_and_value(self, attribute, value):
        with allure.step(f'Поиск элемента по атрибуту: {attribute} и значению: {value}'):
            element = self.browser.find_element(By.XPATH, f"//*[normalize-space(@{attribute})='{value}']")
        self.is_element_visible(By.XPATH, f"//*[normalize-space(@{attribute})='{value}']")
        return element

    def move_to_element(self, how, what, name):
        with allure.step(f"Навести курсор на элемент: {name}"):
            element = self.browser.find_element(how, what)
            action = AC(self.browser)
            action.move_to_element(element)
            action.perform()

    def scroll_to_element(self, element, name):
        with allure.step(f"Проскроллить страницу до элемента {name}"):
            #element = self.browser.find_element(how, what)
            browser_name = self.get_browser_name(self.browser)
            if browser_name == "firefox":
                self.browser.execute_script("document.documentElement.style.scrollBehavior = 'smooth';")
                self.browser.execute_script("arguments[0].scrollIntoView();", element)
                sleep(0.5)
            elif browser_name == "chrome":
                action = AC(self.browser)
                action.scroll_to_element(element).perform()

    def should_be_correct_url(self, exp_res):
        with allure.step("Проверка корректности url"):
            assert exp_res in self.browser.current_url, (f'Текущий url: {self.browser.current_url} '
                                                         f'должен содержать подстроку: {exp_res}')

    def accept_cookie(self):
        if self.is_element_visible(*BasePageLocators.COOKIE_ALERT, timeout=2):
            with allure.step("Принять куки"):
                self.cookie_apply_button.click()

    def set_cookie(self, *args):
        for arg in args:
            name, value = arg.split("=")
            self.browser.add_cookie({'name': name, 'value': value})

        self.browser.refresh()

    def get_all_cookies(self):
        return self.browser.get_cookies()

    def get_php_sessid(self): # получает куку браузера PHPSESSID
        php_sessid = self.browser.get_cookie('PHPSESSID')
        return f"{php_sessid['name']}={php_sessid['value']}"

    @staticmethod
    def get_browser_name(browser):
        return browser.name
