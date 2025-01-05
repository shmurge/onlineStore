import allure
import requests


class PrepareData:

    # @staticmethod
    # def add_prod_to_cart(php_sessid, prod_id):
    #     with allure.step("Отправка запроса на добавление товара в корзину"):
    #         url = f"https://quke.ru/cart/add/{prod_id}"
    #
    #         headers = {
    #             'Cookie': f'{php_sessid}',
    #             'Accept': '*/*',
    #             'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
    #                           'Chrome/131.0.0.0 Safari/537.36'
    #         }
    #
    #         response = requests.get(url, headers=headers)
    #         assert response.status_code == 200, f"Ошибка: {response.status_code}"

    @staticmethod
    def add_prod_to_cart(jsp, prod_id):
        with allure.step("Отправка запроса на добавление товара в корзину"):
            url = f"https://quke.ru/cart/add/{prod_id}"

            headers = {
                'Cookie': f'{jsp}',
                'Accept': '*/*',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/131.0.0.0 Safari/537.36'
            }

            response = requests.get(url, headers=headers)
            assert response.status_code == 200, f"Ошибка: {response.status_code}"

