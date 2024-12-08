from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.common.keys import Keys
import allure
from time import sleep


class Button:

    def __init__(self, browser, name, how, what):
        self.browser = browser
        self.name = name
        self.locator = how, what

    def click(self):
        with allure.step(f"Клик по: {self.name}"):
            button = self.browser.find_element(*self.locator)
            button.click()

    def double_click(self):
        with allure.step(f"Двойной клик по: {self.name}"):
            action = AC(self.browser)
            action.double_click().perform()

    def get_button_color(self):
        sleep(0.5)
        with allure.step(f"Получить цвет: {self.name}"):
            button = self.browser.find_element(*self.locator)
            color = self.browser.execute_script(
                "return window.getComputedStyle(arguments[0]).getPropertyValue('background-color');", button)
        return color

    def check_button_color(self, exp_res):
        act_res = self.get_button_color()
        with allure.step(f"Проверка цвета в: {self.name}"):
            assert act_res == exp_res, f"Несоответствие цвета в {self.name}! ОР: {exp_res}, ФР: {act_res}"

    def get_button_text(self):
        button_text = self.browser.find_element(*self.locator).text
        return button_text

    def check_button_text(self, exp_res):
        with allure.step(f"Проверить текст в {self.name}"):
            act_res = self.get_button_text()
            assert act_res == exp_res, f"Некорректный текст в кнопке! ОР: {exp_res}, ФР: {act_res}"

    def waiting_clickable(self, timeout=5):
        try:
            WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable(self.locator))
        except TimeoutException:
            return False
        return True


class Input:

    def __init__(self, browser, name, how, what):
        self.browser = browser
        self.name = name
        self.locator = how, what

    def click(self):
        with allure.step(f"Клик по: {self.name}"):
            action = AC(self.browser)
            action.click().perform()

    def double_click(self):
        with allure.step(f"Двойной клик по: {self.name}"):
            action = AC(self.browser)
            action.double_click().perform()

    def clear_input(self):
        action = AC(self.browser)
        input_1 = self.browser.find_element(*self.locator)
        input_value = input_1.get_attribute("value")
        with allure.step(f"Очистить: {self.name}"):
            while len(input_value) > 0:
                action.double_click(input_1)
                action.send_keys_to_element(input_1, Keys.BACKSPACE).perform()
                input_value = input_1.get_attribute("value")

    def send_keys_in_input(self, data):
        input_1 = None
        action = AC(self.browser)
        input_1 = self.browser.find_element(*self.locator)
        with allure.step(f"Ввод данных в {self.name}"):
            action.double_click(input_1)
            action.send_keys_to_element(input_1, data).perform()
        input_1_value = input_1.get_attribute("value")
        with allure.step(f"Проверка введенных данный в {self.name}"):
            assert input_1_value == data, f'Некорректные данные в инпуте! ОР: {data}, ФР: {input_1_value}'

    def check_input_error_message(self, how, what, exp_message):
        act_message = None
        try:
            act_message = self.browser.find_element(how, what).text
        except NoSuchElementException:
            f"Сообщение об ошибке в {self.name} не отображается! Сообщение должно отображаться!"
        assert exp_message == act_message, f"Некорректное сообщение об ошибке в {self.name}! " \
                                           f"ОР: {exp_message}, ФР: {act_message}"

    def check_missing_validation_message(self, how, what):
        self.browser.implicitly_wait(0.5)
        error_message = False
        actual_error_message = None
        error_message = self.browser.find_element(how, what).is_displayed()
        if error_message:
            actual_error_message = self.browser.find_element(how, what).text
        assert error_message is False, \
            f"В {self.name} отображается ошибка: {actual_error_message}! Ошибка не должна отображаться!"

    def check_placeholder(self, exp_placeholder):
        act_placeholder = None
        try:
            act_placeholder = self.browser.find_element(*self.locator).get_attribute("placeholder")
        except NoSuchElementException:
            print(f"В {self.name} плэйсхолдер не найден!")
        with allure.step(f"{self.name}: проверка плэйсхолдера"):
            assert act_placeholder == exp_placeholder, \
                f"В {self.name} некорректный плэйсхолдер! ОР: {exp_placeholder}, ФР: {act_placeholder}"
