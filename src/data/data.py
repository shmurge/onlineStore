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

    TEXT_IN_PROD_PAGE_BUY_BUTTON = "КУПИТЬ"
    TEXT_IN_PROD_PAGE_GO_TO_CART_BUTTON = "ПЕРЕЙТИ В КОРЗИНУ"


class Url:
    MAIN_PAGE = "https://quke.ru/"
    PROFILE_PAGE = "https://quke.ru/profile"
    CART_PAGE = "https://quke.ru/order"


class Catalogue:
    CATALOGUE = {
        "Смартфоны": [["Смартфоны Xiaomi", "Xiaomi"], ["Смартфоны Samsung", "Samsung"], ["Смартфоны Apple", "Apple"],
                      ["Смартфоны Realme", "Realme"], ["Смартфоны Google", "Google"], ["Смартфоны Honor", "Honor"],
                      ["Смартфоны Infinix", "Infinix"], ["Смартфоны OnePlus", "OnePlus"]],
        "Планшеты": [["Планшеты Digma", "Планшет Digma"], ["Планшеты Lenovo", "Планшет Lenovo"]],
        "Аксессуары": [["Чехлы для телефона", "Чехол"], ["Защитные стекла для телефонов", "Защитное стекло"],
                       ["Защитные стекла для камер", "Защитное стекло для камеры"],
                       ["Защитные пленки для телефонов", "Защитная пленка"],
                       ["Зарядные устройства Apple", "Сетевое зарядное устройство Apple"],
                       ["Зарядные устройства Samsung", "Зарядное устройство Samsung"],
                       ["Защитные стекла для планшетов", "Защитное стекло"],
                       ["Защитные пленки для планшетов", "Защитная пленка"]],
        "Наушники и аудиотехника": [["Наушники Xiaomi", "Xiaomi"], ["Наушники Samsung", "Samsung"],
                                    ["Наушники Apple", "Apple"], ["Наушники JBL", "JBL"],
                                    ["Наушники Nothing", "Nothing"], ["Наушники Realme", "Realme"]]}


class ProductName:
    PRODUCT_NAMES_LIST = ["Xiaomi Redmi Note 13 Pro", "iPhone 15", "Ноутбук Apple",
                          "Realme", "Наушники Xiaomi"]
