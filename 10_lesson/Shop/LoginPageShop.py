from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from allure

class LoginPage:

    def __init__(self, driver):
        """
        Конструктор класса LoginPage
        """
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")
        self._driver.implicitly_wait(5)
        self._driver.maximize_window()

    @allure.step("Ввести данные для авторизации и авторизоваться")
    def log_in(self):
        self._driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
        self._driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
        self._driver.find_element(By.CSS_SELECTOR, "#login-button").click()
