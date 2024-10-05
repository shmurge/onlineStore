import allure
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotVisibleException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains as AC

from time import sleep


class BasePage:

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self, url):
        with allure.step(f'Открыть страницу {url}'):
            return self.browser.get(self.url)

    def refresh(self):
        with allure.step('Page refreshing'):
            return self.browser.refresh()

    def go_back(self):
        """Возврат на предыдущую страницу, через кнопку в браузере!"""
        with allure.step('Click go back button in browser'):
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

    def is_element_visible(self, how, what):
        try:
            WebDriverWait(self.browser, 10, 0.5).until(EC.visibility_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_not_element_visible(self, how, what):
        try:
            WebDriverWait(self.browser, 10, 0.5).until_not(EC.visibility_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def waiting_text_visibility(self, locator: tuple[str, str], text: str, timeout: float = 1.0):
        try:
            WebDriverWait(self.browser, timeout).until(EC.text_to_be_present_in_element(locator, text_=text))
        except TimeoutException:
            return True
        return False

    def waiting_element_clickable(self, locator: tuple[str, str], timeout: float = 1.0):
        try:
            WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            return True
        return False

    def waiting_attribute_in_element(self, locator: tuple[str, str], attribute: str, timeout: float = 1.0):
        try:
            WebDriverWait(self.browser, timeout).until(EC.element_attribute_to_include(locator, attribute))
        except TimeoutException:
            return True
        return False

    def send_keys_in_input(self, how, what, data):
        input_1_value = None
        actions = AC(self.browser)
        input_1 = self.browser.find_element(how, what)
        actions.double_click(input_1)
        actions.send_keys_to_element(input_1, data).perform()
        input_1_value = input_1.get_attribute("value")
        assert input_1_value == data, \
            f'Incorrect data in input! Expect: "{data}", but actual: "{input_1_value}"'

    def search_element_by_text(self, text):
        element = None
        with allure.step(f'Поиск элемента: {text}'):
            element = self.browser.find_element(By.XPATH, f"//*[text()='{text}']")
        return element

    def click_action(self, x, y):  # Необходимо передать функции координаты точки, куда нужно кликнуть
        with allure.step(f"Клик по координатам: {x}, {y}"):
            action = AC(self.browser)
            action.move_by_offset(x, y)
            action.click()
            action.perform()

    def move_to_element(self, how, what, name):
        with allure.step(f"Навести курсор на элемент: {name}"):
            element = self.browser.find_element(how, what)
            action = AC(self.browser)
            action.move_to_element(element)
            action.perform()

    def get_searching_result(self, how, what):  # возвращает список элементов после поиска
        results = None
        results = self.browser.find_elements(how, what)
        return results

