from selenium import webdriver
from mainpageCalc import MainPageCalc

def test_calc():
    browser = webdriver.Chrome()
    MainPageCalc = open_mainpage(browser)
    MainPageCalc.calc_waits(45)
    MainPageCalc.output_value
    MainPageCalc.waiter
    driver.quit()
