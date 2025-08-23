from allure
from selenium import webdriver
from LoginPageShop import LoginPage
from MainPageShop import MainPage
from CartPageShop import CartPage
from FinalPageShop import FinalPage

@allure.title("Тестирование интернет магазина одежды")
@allure.descriprion("Тест проверяет возможность авторизации на сайте интернет магазина, добавление товара в корзину")
def test_shop():
    """
    Тест проверяет работу интернет магазина одежды. Авторизация на сайте
    """
    browser = webdriver.Firefox()
    log_Page = LoginPage(browser)
    log_Page.log_in()

    main_page = MainPage(browser)
    main_page.add_to_cart()

    cart_page = CartPage(browser)
    cart_page.open_cart()
    cart_page.buy()

    final_page = FinalPage(browser)
    final_page.order_form()
    final_page.final_page()
    final_page.close_driver()
