class UsersData:
    USER_1 = ("shmurge3@bk.ru", "ZH7FFCcm3jZaL_c")
    USER_1_NAME = "Алекс"


class InputData:
    INVALID_EMAILS = ["jshdckbs.hgcbhkjw.dk", "оврсло23@km.dj", "@#$@#@$!@#!@##", "0000000000000", ":-)@fwfe12"]


class InputErrors:
    LOGIN_REQUIRED = "Введите e-mail"
    PASSWORD_REQUIRED = "Введите пароль"
    INVALID_LOGIN = "Неверный логин или пароль"


class Placeholders:
    LOGIN_INPUT = "Введите логин или E-mail"
    PASSWORD_INPUT = "Введите пароль"


class ButtonsData:
    SIGN_IN_ORIGINAL_COLOR = "rgb(255, 255, 255)"
    SIGN_IN_HOVER_COLOR = "rgb(49, 74, 194)"


class Url:
    MAIN_PAGE = "https://quke.ru/"
    PROFILE_PAGE = "https://quke.ru/profile"


class Catalogue:
    # CATALOGUE = {"Смартфоны": ["Смартфоны Xiaomi", "Смартфоны Samsung", "Смартфоны Apple", "Смартфоны Realme",
    #                            "Смартфоны Google", "Смартфоны Honor", "Смартфоны Infinix", "Смартфоны OnePlus",
    #                            "Смартфоны Huawei", "Смартфоны Tecno", "Смартфоны Vivo", "Смартфоны Blackview",
    #                            "Смартфоны Oppo", "Смартфоны Nothing"],
    #              "Сотовые телефоны и телефония": ["Кнопочные телефоны", "Кнопочный Digma", "Кнопочный Nokia",
    #                                               "Кнопочный Philips", "Телефоны", "Радиотелефоны", "Телефоны для бизнеса",
    #                                               "IP и SIP телефоны", "VoIP-оборудование", "Гарнитуры для телефонов",
    #                                               "Дополнительные трубки DECT", "Шлюзы"],
    #              "Планшеты, ноутбуки и электронные книги": ["Планшеты", "Samsung", "Huawei", "Digma", "Ноутбуки"]}

    CATALOGUE = {
        "Смартфоны": [["Смартфоны Xiaomi", "Xiaomi"], ["Смартфоны Samsung", "Samsung"], ["Смартфоны Apple", "Apple"],
                      ["Смартфоны Realme", "Realme"], ["Смартфоны Google", "Google"], ["Смартфоны Honor", "Honor"],
                      ["Смартфоны Infinix", "Infinix"], ["Смартфоны OnePlus", "OnePlus"], ["Смартфоны Huawei", "Huawei"],
                      ["Смартфоны Tecno", "Tecno"], ["Смартфоны Vivo", "Vivo"], ["Смартфоны Blackview", "Blackview"],
                      ["Смартфоны Oppo", "Oppo"], ["Смартфоны Nothing", "Nothing"]],
        "Сотовые телефоны и телефония": [["Кнопочный Digma", "Digma"], ["Кнопочный Nokia", "Nokia"],
                                         ["Кнопочный Philips", "Philips"], ["Радиотелефоны", "Радиотелефон"]],
        "Планшеты, ноутбуки и электронные книги": [["Планшеты", "Планшет"],["Samsung", "Планшет Samsung"],
                                                   ["Huawei", "Планшет Huawei"], ["Digma", "Планшет Digma"],
                                                   ["Ноутбуки", "Ноутбук"], ["ASUS", "Asus"], ["Lenovo", "Lenovo"],
                                                   ["HP", "HP"], ["Acer", "Acer"]],
        "Аксессуары": [["Чехлы для телефона", "Чехол"], ["Защитные стекла для телефонов", "Защитное стекло"],
                       ["Защитные стекла для камер", "Защитное стекло для камеры"],
                       ["Защитные пленки для телефонов", "Защитная пленка"],
                       ["Зарядные устройства Apple", "Сетевое зарядное устройство Apple"],
                       ["Зарядные устройства Samsung", "Сетевое зарядное устройство Samsung"],
                       ["Чехлы для планшетов", "Чехол"], ["Защитные стекла для планшетов", "Защитное стекло"],
                       ["Защитные пленки для планшетов", "Защитная пленка"]],
        "Умные часы и браслеты": [["Xiaomi Mi Band 8", "Xiaomi Mi Smart Band 8"],
                                  ["Xiaomi Mi Band 9", "Xiaomi Mi Smart Band 9"], ["Honor Band 9", "Honor Band 9"]],
        }
