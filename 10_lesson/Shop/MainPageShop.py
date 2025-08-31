from selenium.webdriver.common.by import By
import allure

class MainPage:
    """
           Конструктор класса MainPage
    """
    def __init__(self, browser):
        self._driver = browser

    @allure.step("Добавляем товар в корзину")
    def add_to_cart(self):
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
