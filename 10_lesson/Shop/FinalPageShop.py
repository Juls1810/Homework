from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.support.ui import WebDriverWait


class FinalPage:
    """
           Конструктор класса FinalPage
    """
    def __init__(self, browser):
        self._driver = browser

    @allure.step("Заполение формы заказа")
    def order_form(self):
        self._driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Julia")
        self._driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Sav")
        self._driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("398027")
        self._driver.find_element(By.CSS_SELECTOR, "#continue").click()

    @allure.step("Выводим финальную стоимость")
    def final_page(self):
        total = self._driver.find_element(By.CLASS_NAME, "summary_total_label").text
        # EC.text_to_be_present_in_element(By.CLASS_NAME, 'summary_total_label'), "Total: $58.29"
        # print(total)

        try:
            total = WebDriverWait(10).until(
                EC.presence_of_element_located(By.CLASS_NAME, 'summary_total_label').text
            )
        finally:
            print(total)


    def close_driver(self):
        self._driver.quit()
