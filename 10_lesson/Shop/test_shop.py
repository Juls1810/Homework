import allure
from selenium import webdriver
from LoginPageShop import LoginPage
from MainPageShop import MainPage
from CartPageShop import CartPage
from FinalPageShop import FinalPage

@allure.title("Тестирование интернет магазина одежды")
@allure.description("Тест проверяет возможность авторизации на сайте интернет магазина, добавление товара в корзину")
@allure.feature("интернет магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop():
    """
    Тест проверяет работу интернет магазина одежды. Авторизация на сайте
    """
    with allure.step("Открытие браузера"):
        browser = webdriver.Firefox()

    with allure.step("Обьявляем переменную"):
        log_page = LoginPage(browser)

    with allure.step("Ввести данные для авторизации и авторизоваться"):
        log_page.log_in()

    with allure.step("Обьявляем переменную"):
        main_page = MainPage(browser)

    with allure.step("Добавляем товар в корзину"):
        main_page.add_to_cart()

    with allure.step("Обьявляем переменную"):
        cart_page = CartPage(browser)

    with allure.step("Открываем корзину"):
        cart_page.open_cart()

    with allure.step("Покупаем товары в корзине"):
        cart_page.buy()

    with allure.step("Обьявляем переменную"):
        final_page = FinalPage(browser)

    with allure.step("Заполение формы заказа"):
        final_page.order_form()

    with allure.step("Выводим финальную стоимость"):
        final_page.final_page()

    with allure.step("Закрываем браузер"):
        final_page.close_driver()
