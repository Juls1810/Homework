from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPageCalc:


def open_mainpage(self, driver):
    self._driver = driver
    self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    self._driver.implicitly_wait(4)
    self._driver.maximize_window()

#изменение времени ожидания
def calc_waits(self, tern):
    self.driver.find_element(By.CSS_SELECTOR, "#delay").clear()
    self.driver.find_element(By.CSS_SELECTOR, "#delay").send_keys(tern)

# ввод значений  ()  
def output_value(self):
    self.driver.find_element(By.XPATH, "//span[text()='7']").click()
    self.driver.find_element(By.XPATH, "//span[text()='+']").click()
    self.driver.find_element(By.XPATH, "//span[text()='8']").click()
    self.driver.find_element(By.XPATH, "//span[text()='=']").click()
    self.driver.implicitly_wait(40)

def waiter(self):
    self.waiter = WebDriverWait(driver, 65)
    self.waiter.until(
    EC.text_to_be_present_in_element( (By.CLASS_NAME, 'screen'), "15")
    )
    res = driver.find_element(By.CLASS_NAME, 'screen').text
    print(res)    
