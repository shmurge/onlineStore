import allure
import requests


class PrepareData:

    # @staticmethod
    # def add_prod_to_cart(php_sessid, prod_id):
    #     with allure.step("Отправка запроса на добавление товара в корзину"):
    #         url = f"https://quke.ru/cart/add/{prod_id}"
    #
    #         headers = {
    #             'Cookie': f'cookie_quke_policy=1, {php_sessid}',
    #             'Accept': '*/*',
    #             'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
    #                           'Chrome/131.0.0.0 Safari/537.36'
    #         }
    #
    #         response = requests.get(url, headers=headers)
    #         assert response.status_code == 200, f"Ошибка: {response.status_code}"

    @staticmethod
    def add_prod_to_cart(cookies, prod_id):
        with allure.step("Отправка запроса на добавление товара в корзину"):
            url = f"https://quke.ru/cart/add/{prod_id}"

            cookie_dict = {cookie['name']: cookie['value'] for cookie in cookies}

            headers = {
                'Accept': '*/*',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/131.0.0.0 Safari/537.36'
            }

            response = requests.get(url, headers=headers, cookies=cookie_dict)
            assert response.status_code == 200, f"Ошибка: {response.status_code}"
