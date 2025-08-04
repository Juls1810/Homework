from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from MainpageCalc import MainPageCalc

def test_calc():
    browser = webdriver.Chrome()
    MainPageCalc = open_mainpage(browser)
    MainPageCalc.calc_waits(45)
    MainPageCalc.output_value
    MainPageCalc.waiter
    driver.quit()
