from selenium.webdriver.common.by import By
import allure

class CartPage:
    """
           Конструктор класса CartPage
    """
    def __init__(self, browser):
        self._driver = browser

    @allure.step("Открываем корзину")
    def open_cart(self):
        self._driver.get("https://www.saucedemo.com/cart.html")

    @allure.step("Покупаем товары в корзине")
    def buy(self):
        self._driver.find_element(By.CSS_SELECTOR, "#checkout").click()
