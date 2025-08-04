from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


def test_shop():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "#login-button").click()
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
    driver.get("https://www.saucedemo.com/cart.html")
    driver.find_element(By.CSS_SELECTOR, "#checkout").click()
    driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Julia")
    driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Sav")
    driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("398027")
    driver.find_element(By.CSS_SELECTOR, "#continue").click()
    total = driver.find_element(By.CLASS_NAME, "summary_total_label").text
    EC.text_to_be_present_in_element(By.CLASS_NAME, 'summary_total_label'), "Total: $58.29"
    print(total)

    driver.quit()
