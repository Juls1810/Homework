from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get("https://the-internet.herokuapp.com/login")


enter_value = browser.find_element(By.CSS_SELECTOR, "#username")
enter_value.send_keys("tomsmith")

enter_value = browser.find_element(By.CSS_SELECTOR, "#password")
enter_value.send_keys("SuperSecretPassword!")
enter_value.send_keys(Keys.RETURN)

(sleep(5))
display_text = browser.find_element(By.CSS_SELECTOR, "#flash").text 

print(display_text)

sleep(10)
browser.quit()
