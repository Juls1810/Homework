from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class FinalPage:
    def __init__(self, browser):
        self._driver = browser

    def order_form(self):
        self._driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Julia")
        self._driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Sav")
        self._driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("398027")
        self._driver.find_element(By.CSS_SELECTOR, "#continue").click()

    def final_page(self):
        total = self._driver.find_element(By.CLASS_NAME, "summary_total_label").text
        EC.text_to_be_present_in_element(By.CLASS_NAME, 'summary_total_label'), "Total: $58.29"
        print(total)

    def close_driver(self):
        self._driver.quit()
