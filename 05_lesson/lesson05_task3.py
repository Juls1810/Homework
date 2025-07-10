from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get("https://the-internet.herokuapp.com/inputs")

search_button = 'input'

enter_value = browser.find_element(By.CSS_SELECTOR, search_button)
enter_value.send_keys("Sky")
enter_value.send_keys(Keys.RETURN)

enter_value.clear()

enter_value.send_keys("Pro")
enter_value.send_keys(Keys.RETURN)

sleep(15)
browser.quit()
