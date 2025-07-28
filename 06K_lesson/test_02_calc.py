from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_calc():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    driver.find_element(By.CSS_SELECTOR, "#delay").clear()
    driver.find_element(By.CSS_SELECTOR, "#delay").send_keys(45)
    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()
    driver.implicitly_wait(40)
    waiter = WebDriverWait(driver, 65)
    waiter.until(
    EC.text_to_be_present_in_element( (By.CLASS_NAME, 'screen'), "15")
    )
    res = driver.find_element(By.CLASS_NAME, 'screen').text
    print(res)

    driver.quit()
