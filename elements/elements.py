from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import allure
from time import sleep


class BaseElement:

    def __init__(self, browser, name, how, what):
        self.browser = browser
        self.name = name
        self.locator = how, what

    def get_element(self):
        self.is_element_visible(*self.locator)
        return self.browser.find_element(*self.locator)

    def get_elements(self):
        self.is_element_visible(*self.locator)
        return self.browser.find_elements(*self.locator)

    def get_element_by_text(self, text):
        with allure.step(f'Поиск элемента: {text}'):
            self.is_element_visible(By.XPATH, f"//*[text()='{text}']")
            element = self.browser.find_element(By.XPATH, f"//*[text()='{text}']")
        return element

    def get_text_of_element(self, element=None):
        element = element if element else self.get_element()

        return element.text

    def select_element_by_text(self, text):
        with allure.step(f'Выбрать элемент: {text}'):
            self.is_element_visible(By.XPATH, f"//*[text()='{text}']")
            element = self.browser.find_element(By.XPATH, f"//*[text()='{text}']")
            element.click()

    def click(self, element=None):
        element = element if element else self.get_element()
        with allure.step(f"Клик по: {self.name}"):
            action = AC(self.browser)
            action.click(element).perform()

    def double_click(self, element=None):
        element = element if element else self.get_element()
        with allure.step(f"Двойной клик по: {self.name}"):
            action = AC(self.browser)
            action.double_click(element).perform()

    def submit(self, element=None):
        element = element if element else self.get_element()
        with allure.step('Подтвердить'):
            with allure.step(f"Подтвердить ввод в {self.name}"):
                element.submit()

    def scroll_to_element(self, element=None):
        element = element if element else self.get_element()
        action = AC(self.browser)
        action.scroll_to_element(element)
        action.perform()

    def move_to_element(self, element=None):
        element = element if element else self.get_element()
        action = AC(self.browser)
        action.move_to_element(element)
        action.perform()

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


class Button(BaseElement):

    def get_button_color(self, element=None):
        sleep(0.5)
        element = element if element else self.get_element()
        with allure.step(f"Получить цвет: {self.name}"):
            color = self.browser.execute_script(
                "return window.getComputedStyle(arguments[0]).getPropertyValue('background-color');", element)

        return color

    def check_button_color(self, exp_color):
        with allure.step(f"Проверка цвета в: {self.name}"):
            sleep(0.5)
            act_color = self.browser.execute_script(
                "return window.getComputedStyle(arguments[0]).getPropertyValue('background-color');",
                self.get_element()
            )
            assert act_color == exp_color, (f"Несоответствие цвета в {self.name}!\n"
                                            f"ОР: {exp_color},\n"
                                            f"ФР: {act_color}")

    def check_button_text(self, exp_res):
        with allure.step(f"Проверить текст в {self.name}"):
            act_res = self.get_text_of_element()
            assert act_res == exp_res, f"Некорректный текст в кнопке! ОР: {exp_res}, ФР: {act_res}"

    def waiting_clickable(self, timeout=5):
        try:
            WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable(self.locator))
        except TimeoutException:
            return False
        return True


class Input(BaseElement):

    def get_input_element(self):
        self.is_element_visible(*self.locator)
        return self.browser.find_element(*self.locator)

    def clear_input(self):
        action = AC(self.browser)
        input_1 = self.get_input_element()
        input_value = input_1.get_attribute("value")
        with allure.step(f"Очистить: {self.name}"):
            while len(input_value) > 0:
                action.double_click(input_1)
                action.send_keys_to_element(input_1, Keys.BACKSPACE).perform()
                input_value = input_1.get_attribute("value")

    def send_keys_in_input(self, data):
        action = AC(self.browser)
        input_1 = self.get_input_element()
        with allure.step(f"Ввод данных в {self.name}"):
            action.double_click(input_1)
            action.send_keys_to_element(input_1, data).perform()
        input_1_value = input_1.get_attribute("value")
        with allure.step(f"Проверка введенных данный в {self.name}"):
            assert input_1_value == data, f'Некорректные данные в инпуте! ОР: {data}, ФР: {input_1_value}'

    def check_input_error_message(self, how, what, exp_message):
        act_message = None
        self.is_element_visible(how, what)
        act_message = self.browser.find_element(how, what).text
        assert exp_message == act_message, f"Некорректное сообщение об ошибке в {self.name}! " \
                                           f"ОР: {exp_message}, ФР: {act_message}"

    def check_missing_validation_message(self, how, what):
        error_message = self.is_not_element_visible(how, what)
        assert error_message, \
            (f"В {self.name} отображается ошибка: {self.browser.find_element(how, what).text}! "
             f"Ошибка не должна отображаться!")

    def check_placeholder(self, exp_placeholder):
        with allure.step(f"{self.name}: проверка плэйсхолдера"):
            act_placeholder = self.get_input_element().get_attribute("placeholder")
            assert act_placeholder == exp_placeholder, \
                f"В {self.name} некорректный плэйсхолдер! ОР: {exp_placeholder}, ФР: {act_placeholder}"
