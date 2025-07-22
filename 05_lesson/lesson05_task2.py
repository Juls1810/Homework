from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get('http://uitestingplayground.com/dynamicid')

button = browser.find_element(By.CLASS_NAME, 'btn-primary')
button.send_keys(Keys.RETURN)

sleep(20)
browser.quit()
